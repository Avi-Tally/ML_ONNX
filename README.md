# 📊 TallyPrime Local NLP Bridge: Query Financial Data Offline! 🤖

**Query your local TallyPrime instances offline using natural language queries!**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastMCP](https://img.shields.io/badge/FastMCP-orange?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![ONNX Runtime](https://img.shields.io/badge/ONNX--Runtime-blue?style=for-the-badge)


**[IMPORTANT NOTE: This bridge runs completely locally and offline on your machine. No financial data is sent to external servers, guaranteeing complete privacy, regulatory compliance, and near-zero latency.]**

The **TallyPrime Local NLP Bridge** translates unstructured natural language queries (e.g., *"Show ageing for Aarkay Enterprises based on due date"*) into structured TDL (Tally Definition Language) XML requests, executes them against local running TallyPrime instances, post-processes the results using an analytical engine, and formats the output into clean, human-readable Markdown tables.

---

## 🧠 Detailed NLP & Parameter Extraction Pipeline

The NLP pipeline translates unstructured English questions into concrete queries using a hybrid of deep learning transformer model inference (via ONNX Runtime) and high-performance fuzzy text matching.

### 1. The ONNX Classification & Feature Models
The pipeline utilizes **5 local ONNX sessions** inside `nlp_engine.py` to classify and extract query intents and variables:

*   **Core Embedding Model (`model.onnx` & `tokenizer.json`)**:
    *   **Role**: A MiniLM/BERT-style transformer that tokenizes raw text inputs and maps them into 384-dimensional dense semantic vectors. 
    *   **Purpose**: Used to calculate semantic embeddings for queries and benchmark phrase similarity for fallback intent matching.
*   **Intent Classifier (`intent_model.onnx`)**:
    *   **Role**: Multi-class text classification model.
    *   **Purpose**: Classifies queries into primary accounting intents:
        *   `LIST_COMPANIES` (e.g., *"Which companies are running?"*)
        *   `GET_LEDGER_BALANCE` (e.g., *"What is the balance of Aarkay?"*)
        *   `GET_TRIAL_BALANCE` (e.g., *"Get trial balance report"*)
        *   `GET_STOCK_SUMMARY` (e.g., *"What inventory do I have?"*)
        *   `GET_RECENT_VOUCHERS` (e.g., *"Show today's vouchers"*)
        *   `GET_RECEIVABLES` / `GET_PAYABLES` (e.g., *"Who owes me money?"*)
        *   `GET_AGEING` (e.g., *"Ageing analysis for relaxo"*)
        *   `GET_TOP_DEBTORS` / `GET_TOP_CREDITORS` (e.g., *"Top 10 outstanding bills"*)
*   **Status Filter Model (`status_filter_model.onnx`)**:
    *   **Role**: Sequence-to-parameter classification.
    *   **Purpose**: Detects if the query targets a specific bill state (`pending`, `cleared`, or `None` for mixed queries).
*   **Date Target Model (`date_target_model.onnx`)**:
    *   **Role**: Sequence-to-parameter classification.
    *   **Purpose**: Classifies whether ageing and filtering should calculate durations relative to the **Invoice Date** (`bill_date`) or the **Expected Due Date** (`due_date`).
*   **Is Bill Query Classifier (`is_bill_query_model.onnx`)**:
    *   **Role**: Binary sequence classification.
    *   **Purpose**: Classifies whether a query asks for bill/outstanding reports to determine downstream routing.

### 2. Entity Resolution & Fuzzy Matching
Once the query is classified, the target ledger or company must be resolved against live lists fetched from TallyPrime:

*   **Windowing Process**: `nlp_engine.py` extracts word sequences (windows of 1 to 4 contiguous words) from the query, discarding digits and common stop-words.
*   **Fuzzy Token Set Ratio**: Each candidate word window is compared to the fetched ledger names using `rapidfuzz` with `scorer=fuzz.token_set_ratio`.
    *   **Why Token Set Ratio?**: The *Token Set Ratio* splits strings into tokens, extracts intersection and differences, and scores them. This provides extremely high robustness against word order variations, punctuation, and extra qualifiers (e.g., matching *"Aarkay"* to *"Aarkay Enterprises Pvt Ltd"*, or *"Relaxo"* to *"Relaxo Group"*).
    *   **Confidence Threshold**: If the best match across all windows scores above **`85.0`**, it is resolved as the targeted ledger entity.

---

## 🔄 End-to-End Pipeline Workflow Example

Here is the end-to-end workflow of the pipeline demonstrated using a complex, realistic analytical query:

### Sample Query
`"List top 5 outstanding payables of Grauer and Weil above Rs. 1 lakh sorted by bill date as of 29-nov-2025"`

#### Step 1: Request Ingestion (`mcp_server.py`)
The entry point of the pipeline is the FastAPI or FastMCP server.
* The server receives the raw text string.
* It initializes the pipeline context and passes the query to the NLP Engine.

#### Step 2: NLP Intent Classification & Param Extraction (`nlp_engine.py`)
The NLP engine uses a hybrid machine-learning and heuristic approach:
* **Intent Classification (ONNX Model)**: Tokenizes the query and passes it to `intent_model.onnx`. It classifies the intent as `GET_PAYABLES`.
* **Date Target Prediction (ONNX Model)**: Predicts `date_target = "bill_date"` because the query explicitly mentions "sorted by bill date".
* **Status Filter Prediction (ONNX Model)**: Predicts `status_filter = "pending"` because the query contains the keyword "outstanding".
* **Heuristic Parameter Extraction (Regex)**:
    * **Reference Date**: Scans the text for date formats and captures `"as of 29-nov-2025"`, parsing it to `29-Nov-2025`.
    * **Limit**: Scans for keywords like "top" or "first" followed by a number, setting `limit = 5`.
    * **Amount Filter**: Recognizes `"above Rs. 1 lakh"`, setting `amount_filter = { "operator": ">", "value": 100000.0 }`.
    * **Sort Order**: Recognizes `"sorted by bill date"`, setting `sort = { "field": "bill_date", "order": "desc" }`.
    * **Ledger Candidate Name**: Identifies the candidate noun phrase: `"Grauer and Weil"`.

#### Step 3: Fuzzy Ledger Name Resolution & Routing (`nlp_engine.py`)
The pipeline must resolve "Grauer and Weil" to an official accounting ledger:
* It retrieves all ledger names from Tally across both ports (9000 and 9001).
* Discards common grammar stop-words (like "of", "above", "sorted") using a sliding window.
* Computes the similarity score using RapidFuzz against the remaining tokens.
* Resolves the name to `Grauer & Weil (I) Ltd`.
* **Port Routing**: Since `Grauer & Weil (I) Ltd` is a ledger under the Modi Chemplast database, the query router automatically targets **Port 9000** (Modi Chemplast) instead of Port 9001 (Bella Casa).

#### Step 4: Raw Tally XML Fetching (`tally_client.py`)
The pipeline talks to TallyPrime via XML HTTP requests:
* **TDL Collection Construction**: It crafts an XML payload asking for the `CustomBillCollection` (representing Tally's Bill table objects).
* **Current Date Anchoring**: It injects `<SVCURRENTDATE>29-Nov-2025</SVCURRENTDATE>` to evaluate outstandings historically up to that date.
* **Performance Optimization**: Because `status_filter` is `"pending"`, it appends a TDL collection filter formula `$ClosingBalance != 0`. This stops Tally from serializing thousands of cleared bills.
* **Streaming & Cleaning (`SanitizedStream`)**: It posts the XML to `http://localhost:9000` and parses the response chunk-by-chunk.
* **Multicurrency Amount Parser**: If it encounters a foreign transaction value (e.g., `? 13000.00 @ Rs 100.00/? = Rs 1300000.00`), it splits by `=` to extract the base currency amount (`1300000.00`) as a float.

#### Step 5: Analytical Filtering & Calculation (`analytics_engine.py`)
The pipeline post-processes the raw bills returned from the database:
* **Sign-Based Filtering**: Since the intent is `GET_PAYABLES`, it filters strictly for Credit balances (amount > 0). Debit advances or adjustments are filtered out.
* **Date Boundaries**: Excludes any bills invoiced after `29-Nov-2025` or due in the future (`age < 0`).
* **Amount Filter**: Applies `amount > 100000.0` (filtering out any bills below ₹1 Lakh).
* **Sorting**: Sorts the remaining list by `bill_date` in descending order.
* **Limiting**: Crops the list to return only the first 5 elements.

#### Step 6: Markdown Generation & Delivery (`mcp_server.py`)
The final array is formatted into a clean markdown table:
* Calculates the age of the bills relative to `29-Nov-2025` (e.g., `32d`).
* Generates a header showcasing the active company, target date, and port.
* Outputs the final markdown table back to your chat window.

---

## 🧩 Component Breakdown & Roles

This section details the architectural role and implementation logic of each core code file.

### 1. `mcp_server.py` (The FastMCP Host)
*   **Role**: Acts as the central orchestrator and public interface of the bridge.
*   **Responsibilities**:
    *   Exposes the `query_tally(query: str)` tool to Model Context Protocol (MCP) clients using FastMCP.
    *   Coordinates the chronological query pipeline: invoking the **NLP Engine** to extract intent, fetching raw reports through the **Tally Client**, executing post-processing through the **Analytics Engine**, and structuring the final markdown output.

### 2. `nlp_engine.py` (NLU & Entity Resolution Engine)
*   **Role**: Transforms unstructured natural language strings into machine-interpretable command parameters.
*   **Responsibilities**:
    *   Loads tokenizer files and executes the 5 local ONNX runtime sessions.
    *   Runs date parsing and maps periods like *"this quarter"*, *"next 7 days"*, *"last 30 days"*.
    *   Performs windowing and fuzzy entity mapping against live active ledger tables.

### 3. `tally_client.py` (XML & TDL Communication Client)
*   **Role**: Communicates with the local TallyPrime HTTP server.
*   **Responsibilities**:
    *   **Dynamic Port Discovery**: Concurrently probes ports `9000` and `9001` using thread pools (`concurrent.futures`) to discover loaded companies and cache their routing details.
    *   **Payload Construction**: Builds complex XML envelopes incorporating inline TDL (Tally Definition Language) collections to query exact data fields.
    *   **XML Sanitization**: Filters out control characters and invalid XML decimal/hex entities from Tally's response streams before parser handoff.

### 4. `analytics_engine.py` (Analytics & Reporting Engine)
*   **Role**: Implements business and accounting logic on top of raw Tally data.
*   **Responsibilities**:
    *   Calculates absolute value amounts and cleans currency indicators.
    *   Determines bill ageing delays relative to target dates and anchors.
    *   Organizes outstanding receivables/payables into ageing brackets (`0-30`, `31-60`, etc.) and formats tabular output.

### 5. `api_server.py` (REST API Gateway)
*   **Role**: Exposes the bridge functionality via standard HTTP endpoints.
*   **Responsibilities**:
    *   Provides FastAPI endpoints (`/query`, `/parse`, `/companies`, `/health`) for web integrations and dashboards.
    *   Returns structured JSON metadata along with the rendered markdown response.

### 6. `cli_query.py` (Interactive Testing Command Line)
*   **Role**: A lightweight developer tool for local debugging.
*   **Responsibilities**:
    *   Provides an interactive loop (`Query >`) to test NLU mapping, fuzzy match performance, and Tally responses directly in the terminal without spawning a full MCP host.

---

## 🛠️ Technology Stack & Dependencies

*   **FastMCP / MCP**: Model Context Protocol interface.
*   **FastAPI / Pydantic**: Async REST gateway server and payload validation.
*   **ONNX Runtime (`onnxruntime`)**: Executes deep learning intent and classification models locally.
*   **RapidFuzz**: Performs rapid fuzzy string matching for company/ledger name resolution.
*   **Requests**: Executes synchronous XML POST requests to TallyPrime.
*   **ElementTree**: Core XML traversal and tag extraction library.

---

## 🚀 Getting Started

### 1. Configure TallyPrime HTTP Connectivity
Ensure TallyPrime is open on the machine, and configure its local HTTP port:
1.  Navigate to **F1: Help** > **Settings** > **Connectivity**.
2.  Set **Client/Server Configuration** to *Both* or *Server*.
3.  Set the port to `9000` or `9001`.

### 2. Install Python Dependencies
```bash
pip install requests rapidfuzz mcp fastmcp fastapi uvicorn onnxruntime tokenizers numpy
```

### 3. Run the Interactive Test CLI
Verify connection and query resolution:
```bash
python cli_query.py
```

### 4. Start the FastAPI Gateway
Launch the REST API:
```bash
uvicorn api_server:app --host 127.0.0.1 --port 8000 --reload
```

---

## 🤝 Contributions

Contributions to this project are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes.
4.  Push to the branch.
5.  Submit a pull request.

---


---

## 📧 Contact

*   **E-mail**: [aviral.jain@tallysolutions.com](mailto:aviral.jain@tallysolutions.com)
*   **LinkedIn**: [Aviral Jain](https://www.linkedin.com/in/aviral-jain-27018331b)
