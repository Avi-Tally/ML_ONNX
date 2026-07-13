Here is a detailed breakdown of the architecture, design constraints, and components we have implemented so far for the TallyPrime Local NLP Bridge:

1. Architectural Design & Constraints
100% Offline Execution: All components run locally without any external API dependencies, protecting local financial data privacy.
Sleek Memory Footprint (Target 
≤
200
≤200 MB): Avoids heavyweight dependencies like Pandas, PyTorch, or Hugging Face. The active MCP server operates at ~73.5 MB RAM, leaving a huge safety margin.
Massive Stream Processing: Uses sequential XML streaming to parse reports containing over 100,000+ entries (e.g. 100MB+ bills list) in less than a second without memory overflows.
2. Core Components & Implementations
📡 Tally Client (tally_client.py)
Port Prober & Routing Table: Scans configured ports (e.g., 9000 and 9001) on startup, fetches the active company details (name, active fiscal period, working date), and registers them dynamically in a local routing cache.
Stream-Based XML Sanitizer & Parser:
Strips out illegal XML characters (such as hex control codes like &#4;) byte-by-byte on the fly, preventing XML parser crashes.
Employs xml.etree.ElementTree.iterparse to sequentially read, clean, and discard XML nodes after processing, preventing memory consumption spikes.
Julian Date (JD) Parser: Detects and decodes raw Tally Julian Date attributes (e.g. JD="46021") in <BILLCREDITPERIOD> tags to compute correct, absolute bill due dates.
🧠 NLP & Parameter Parsing Engine (nlp_engine.py)
Pure NumPy Classifier: Uses a TF-IDF vectorizer + Logistic Regression intent classifier. Inference is written entirely in pure NumPy and loads pre-trained weights from intent_model.json. It classifies queries into 9 distinct intents:
LIST_COMPANIES
GET_TRIAL_BALANCE
GET_STOCK_SUMMARY
GET_RECENT_VOUCHERS
GET_LEDGER_BALANCE
GET_RECEIVABLES (Dues/Outstanding bills)
GET_PAYABLES (Outstanding liabilities)
GET_AGEING (Bucketed ageing analysis)
GET_TOP_DEBTORS / GET_TOP_CREDITORS (Top customer/vendor balances)
Fuzzy Entity Resolver (RapidFuzz): Matches colloquial user names (e.g., "modi chem") to official ledger accounts in Tally (e.g., "Modi Chemplast Materials Pvt Ltd") with dynamic ambiguity handling (returns a selection menu if two matches are too close).
Heuristic Parameter Extractor:
Amounts: Identifies numeric filters (e.g., > 1L, < 55k) and translates shorthand like L (Lakh), cr (Crore), k (Thousands).
Limits & Order: Extracts parameters like "10 oldest" or "top 5" and sets up sort configurations.
Relative Timeframes: Detects conditions like "due in next 10 days" or "last 30 days".
Aggregation Flags: Identifies quantitative requests ("how many", "total value") to toggle summary math.
Status Filters: Identifies "cleared" / "settled" vs. "pending" / "outstanding".
Context-Bound Period Router: If a query mentions a specific date or month (e.g., feb 2025) but omits the company name, the engine cross-references the transaction month against all registered companies' active fiscal periods, routing the request to the correct port automatically.
📊 Analytics Engine (analytics_engine.py)
Pure Python Aggregation & Sorting: Computes grouping, sorting (e.g. by amount, bill date), and ageing bucket calculations dynamically.
Context-Anchored Time Calculations: Uses the working date (##SVCurrentDate) extracted from Tally as the "today" reference point, ensuring historical datasets (e.g., transactions in 2017 or 2024) calculate age brackets and relative deadlines relative to the dataset's timeframe instead of system wall-clock time.
Status Filter Application: Filters transactions using is_cleared states (derived from Tally's <CLEAREDON> tag) to isolate outstanding vs. settled bills.
🔌 MCP Server & Interactive CLI (mcp_server.py & cli_query.py)
FastMCP Server: Exposes the bridge functionality to the tool schema via query_tally(query: str).
Diagnostic Reporting: Integrates microsecond execution timers inside query responses.
Markdown Generator: Formats final outputs (Trial Balances, Stock Summaries, filtered receivables tables) into clean, readable Markdown tables.
Context Headers: Prepends a header block containing the current company name, its Tally current date, and active working period above every response.
Manual Test CLI (cli_query.py): An interactive terminal interface where you can enter natural language queries and immediately view outputs, active ports, and connection logs.
3. Verification Results
Port 9000 (Bella Casa Data): Successfully probes, connects, and parses historical data (active period: 2017).
Port 9001 (Modi Chemplast Materials): Probes and connects successfully (active period: 2024-2026).
Auto-Routing: Queries like "What are the payables to top 5 companies in feb 2025?" successfully auto-routed to Port 9001 (Modi Chemplast) since February 2025 falls within its active period, while Port 9000 was skipped.
Quantitative Queries: Queries like "How many bills due in next 10 days..." successfully return a summary header: **Total Bills:** 5 | **Total Value:** ₹ 2,000,000.00.