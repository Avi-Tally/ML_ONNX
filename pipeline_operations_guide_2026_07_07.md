# TallyPrime NLP Bridge: Operations & Verification Guide

This guide provides a detailed breakdown of the active NLP query pipeline, step-by-step instructions to manually spin up and operate the system, and diagnostic check commands to verify health.

---

## 1. Pipeline Working Details

The query pipeline executes in six distinct stages when a natural language request is received:

```
[ User Query ]
      │
      ▼
1. Preprocessing (Normalization & Stopphrase Stripping)
      │
      ▼
2. ML Inference (ONNX Classifiers) ────────► Intent, Status, Date Target, Is Bill Flags
      │
      ▼
3. Fuzzy Entity Matching ──────────────────► Resolves shorthand to Tally Ledger Names
      │
      ▼
4. Port Routing & Period Lookup ───────────► Finds Company Port & Current Fiscal Date Context
      │
      ▼
5. XML Data Fetching (SOAP TDL) ───────────► Retrieves Raw Collections from TallyPrime
      │
      ▼
6. Analytics Processing (AnalyticsEngine) ─► Applies Filters, Sorts, and Limits in Python
      │
      ▼
[ Structured Markdown / JSON Output ]
```

### Stage 1: Preprocessing
The input query is cleaned by converting it to lowercase and removing punctuation. Known stop-words (like "what is the outstanding for", "show balance") are extracted to isolate potential ledger names.

### Stage 2: Parallel ONNX Inference
The normalized query is evaluated by four parallel scikit-learn Logistic Regression pipelines exported to ONNX:
- `intent_model.onnx` (Determines the operation: receivables, payables, stock, day book, trial balance, etc.)
- `status_filter_model.onnx` (Extracts status: pending, cleared, or neutral)
- `date_target_model.onnx` (Determines whether to filter by `due_date` or `bill_date`)
- `is_bill_query_model.onnx` (Flags if this is invoice/bill level)

### Stage 3: Fuzzy Ledger Matching
Strips non-ledger text from the query and matches the remaining noun chunk against the active Tally ledger list using `rapidfuzz` `token_set_ratio`. Short ledger names are protected by sorting candidates by length descending prior to comparison.

### Stage 4: Port & Context Routing
`TallyClient` queries active local ports (9000/9001) to read loaded company names. If a query mentions a specific company, it routes the request to that company's active port. It also fetches the company's current date context (e.g. `01-Jan-2026`) to serve as the relative "today" anchor for ageing reports.

### Stage 5: TDL XML Retrieval
A SOAP request wrapping a custom TDL collection is dispatched to Tally. For example, `fetch_bills` uses a TDL collection querying `Bills Outstanding` to retrieve matching bills with attributes like invoice date, due date, party name, amount, and clearing status.

### Stage 6: Python Filtering & Formatting
`AnalyticsEngine` parses the XML response, converts Tally's custom date strings to Python datetime objects, calculates age days relative to Tally's system date, applies amount/date/age range filters, sorts the lists, and restricts outcomes to requested Limits. The output is then formatted as a clean Markdown table.

---

## 2. Step-by-Step Manual Operations Guide

To run the pipeline manually, follow these four setup steps:

### **Step 1: Start TallyPrime HTTP Interface**
Ensure TallyPrime is running locally and HTTP API access is enabled:
1. Open TallyPrime.
2. Go to **F1: Help** > **Settings** > **Connectivity**.
3. Set **Client/Server Configuration** to:
   - *TallyPrime acts as:* **Both** or **Server**
   - *Port:* **9000** (or **9001** for a second instance)
4. Ensure the companies (e.g., `Modi Chemplast` or `Bella Casa`) are loaded.

### **Step 2: Start the FastAPI Server**
Open a terminal in the project directory (`c:\Users\avija\projects\ML_ONNX`) and spin up the ASGI web server:
```powershell
python -m uvicorn api_server:app --host 127.0.0.1 --port 8000
```
*(This loads the retrained ONNX classifiers and starts listening on port 8000).*

### **Step 3: Start the FastMCP Server (For AI Agents/Obsidian)**
If integrating the bridge with Claude Desktop or cursor-mcp hosts, start the stdio server:
```powershell
python mcp_server.py
```

### **Step 4: Run CLI Query Interface**
To test queries directly without a browser or REST client, run the CLI query test script:
```powershell
python test_mcp_bill.py
```

---

## 3. Verification & Diagnostics Protocol

Run the following checks to ensure every layer of the system is functioning correctly:

### **Check 1: Check FastAPI Server Status**
Run a GET request to the `/health` and `/companies` endpoints:
```powershell
# Check health (should return status: healthy and active company count)
curl http://127.0.0.1:8000/health

# Check active company connections
curl http://127.0.0.1:8000/companies
```

### **Check 2: Run the Global Test Suite**
Execute the 355-query test validation gauntlet. If the pipeline is working correctly, the pass rate will be exactly **100.00%**:
```powershell
python run_test_suite.py
```

### **Check 3: Test ONNX Model Loading**
Run a Python one-liner to verify that the ONNX Runtime sessions initialize correctly and load the intent model:
```powershell
python -c "import onnxruntime as ort; session = ort.InferenceSession('models/intent_model.onnx'); print('ONNX Session loaded successfully. Inputs:', [i.name for i in session.get_inputs()])"
```

### **Check 4: Expose and Verify ONNX/Heuristic JSON Outputs**
To debug how the `NLPEngine` parses a query (including the ONNX model classifications and extracted entities) without executing it against the TallyPrime database:

#### **Method A: Use the FastAPI `/parse` Endpoint**
With the FastAPI server running on port 8000, post a request to `/parse`:
```powershell
# In PowerShell:
$body = @{ query = "Pending bills on 1-dec-2025 with age less than 80 days" } | ConvertTo-Json
Invoke-RestMethod -Uri http://127.0.0.1:8000/parse -Method Post -Body $body -ContentType "application/json" | ConvertTo-Json -Depth 5

# In command prompt / bash:
curl http://127.0.0.1:8000/parse -X POST -H "Content-Type: application/json" -d "{\"query\": \"Pending bills on 1-dec-2025 with age less than 80 days\"}"
```

#### **Method B: CLI Direct Invocation**
Run a Python one-liner directly in the workspace terminal:
```powershell
python -c "import json; from nlp_engine import NLPEngine; print(json.dumps(NLPEngine().parse_query('Pending bills on 1-dec-2025 with age less than 80 days'), indent=2))"
```

---

## 4. Troubleshooting Common Issues

| Symptom | Root Cause | Resolution |
|---|---|---|
| `Error: No active TallyPrime instances detected` | TallyPrime HTTP server is disabled or not running on port 9000/9001. | Open TallyPrime, verify port settings in Help > Settings > Connectivity, and make sure the target company is loaded. |
| `invalid perl operator: (?u)` | ONNX model was trained using an incompatible regex pattern. | Re-train models using `merge_and_train.py` which forces the compatible token pattern: `token_pattern=r"[a-zA-Z0-9]+"`. |
| `Ledger balance mismatch: resolved to None` | The ledger name requested does not exist in the active TallyPrime database. | Query `/companies` to verify which company is loaded and list its active accounts. |
