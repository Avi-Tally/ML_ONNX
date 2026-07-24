# Complete Annotated Reference & Implementation Guide: `mcp_server.py` & `run_test_suite.py`

This document provides line-by-line structural explanations, module rationale, library import importance, FastMCP server routing, Markdown report formatting, and benchmark evaluation mechanics for `mcp_server.py` and `run_test_suite.py`.

---

## Part A: FastMCP Server Dispatcher (`mcp_server.py`)

### A.1 Overview & Responsibilities
`mcp_server.py` implements the **Model Context Protocol (MCP)** server interface. It exposes the engine as an AI Tool (`@mcp.tool()`), accepts end-user natural language queries, coordinates parsing with `nlp_engine.py`, dispatches TDL requests to `tally_client.py`, and renders output cards.

### A.2 Library Imports & Rationale
```python
import sys
import os
from mcp.server.fastmcp import FastMCP  # High-performance FastMCP server framework
from nlp_engine import NLPEngine      # Core ML/NLU Engine instance
from tally_client import TallyClient  # TDL XML Transport adapter instance
```

---

### A.3 Annotated Code Walkthrough (`mcp_server.py`)

```python
# Initialize FastMCP Server Instance named 'TallyPrime NLP Bridge'
mcp = FastMCP("TallyPrime NLP Bridge")

# Global Singleton Instances
tally_client = TallyClient()
nlp_engine = NLPEngine(tally_client)

@mcp.tool()
def query_tally(query: str) -> str:
    """
    Primary MCP Tool Endpoint.
    Executes natural language queries against active TallyPrime ERP instances.
    """
    # 1. Update company routing table and probe active ports (9000, 9001)
    tally_client.update_routing_table()
    
    # 2. Parse query parameters using NLPEngine
    parsed = nlp_engine.parse_query(query)
    intent = parsed.get("intent")
    company_name = parsed.get("company_name", "Default Company")
    port = parsed.get("port", 9000)

    # 3. GLOBAL AMBIGUITY INTERCEPTOR: Catch multi-ledger matches (e.g. Reliance)
    if parsed.get("ambiguous_candidates"):
        extracted = parsed.get("extracted_ledger", "party")
        candidates_str = "\n".join([f"   - **{c}**" for c in parsed["ambiguous_candidates"]])
        return f"[{company_name}] I found multiple accounts matching '{extracted}'. Did you mean:\n{candidates_str}"

    # 4. AMBIGUOUS OUTSTANDINGS INTERCEPTOR: Catch directionally ambiguous queries ('Show pending bills')
    if intent == "AMBIGUOUS_OUTSTANDINGS":
        return f"[{company_name}] Your query is directionally ambiguous. Are you looking for **Bills Payable** (money you owe) or **Bills Receivable** (money owed to you)?"

    # 5. INTENT HANDLER: Ledger 360° View Card
    if intent == "GET_LEDGER_360":
        return render_ledger_360_card(parsed, company_name, port)

    # 6. INTENT HANDLER: Multi-Company Comparison
    if intent == "GET_COMPARATIVE_SUMMARY":
        return render_multi_company_comparison(tally_client.routing_table)

    # 7. INTENT HANDLER: Outstandings (Receivables / Payables)
    if intent in ["GET_RECEIVABLES", "GET_PAYABLES"]:
        bills = tally_client.fetch_bills(company_name, port, report_type=intent)
        return render_outstandings_table(bills, company_name, port, intent)

    # 8. INTENT HANDLER: Trial Balance Report
    if intent == "GET_TRIAL_BALANCE":
        tb_data = tally_client.fetch_trial_balance(company_name, port)
        return render_trial_balance_table(tb_data, company_name, port)

    # 9. INTENT HANDLER: Stock Summary Report
    if intent == "GET_STOCK_SUMMARY":
        stock_data = tally_client.fetch_stock_summary(company_name, port)
        return render_stock_summary_table(stock_data, company_name, port)

    return f"[{company_name}] Query executed under intent '{intent}'."
```

---

## Part B: Benchmark Test Suite & Mismatch Generator (`run_test_suite.py`)

### B.1 Overview & Responsibilities
`run_test_suite.py` is the automated validation harness. It executes the entire 727-query benchmark dataset (`test_suite_expected.json`), evaluates actual engine outputs against ground-truth parameters, and generates `mismatch_report.md` and `matched_report.md`.

### B.2 Annotated Code Walkthrough (`run_test_suite.py`)

```python
import json
import os
import time
from tally_client import TallyClient
from nlp_engine import NLPEngine

def build_mismatch_report(expected_path, output_path):
    """
    Evaluates NLPEngine against ground-truth dataset.
    Strictly checks Intent, Resolved Ledger Name, and all 27 entity parameter fields.
    """
    with open(expected_path, 'r', encoding='utf-8') as f:
        expected_data = json.load(f)

    # Mock Tally Client providing dynamic ledger list for offline benchmark evaluation
    class MockTallyClient:
        def __init__(self, expected_data):
            self.routing_table = {"mock_company": {"port": 9000, "name": "Mock Company"}}
            self.ledgers = {q['expected_entities']['ledger_name']: "0.00" 
                            for q in expected_data if q.get('expected_entities', {}).get('ledger_name')}
            
        def get_port_for_company(self, query): return 9000, "Mock Company", {}
        def fetch_ledgers(self, company, port): return self.ledgers
            
    client = MockTallyClient(expected_data)
    nlp = NLPEngine(client)

    passed, failed = 0, 0
    mismatches, matches = [], []

    for item in expected_data:
        query_text = item.get("query")
        exp_intent = item.get("intent", "UNKNOWN")
        exp_entities = item.get("expected_entities", {})

        if exp_intent == "UNKNOWN":
            continue

        # Parse query via NLPEngine
        parsed = nlp.parse_query(query_text)
        act_intent = parsed.get("intent")
        act_params = parsed.get("parameters", {})
        act_ledger = parsed.get("resolved_ledger")

        # 1. Intent Validation
        intent_match = (act_intent == exp_intent)

        # 2. Ledger Name Validation
        exp_ledger = exp_entities.get("ledger_name")
        ledger_match = (exp_ledger.lower() == act_ledger.lower()) if exp_ledger and act_ledger else (exp_ledger == act_ledger)

        # 3. Strict 27-Parameter Entity Validation
        params_match = True
        for key, exp_val in exp_entities.items():
            if key == "ledger_name": continue
            if act_params.get(key) != exp_val:
                params_match = False
                break

        # Check total pass/fail status
        if intent_match and ledger_match and params_match:
            passed += 1
            matches.append(item)
        else:
            failed += 1
            mismatches.append({"query": query_text, "exp_intent": exp_intent, "act_intent": act_intent})

    # Write summary statistics to mismatch_report.md
    pass_rate = (passed / (passed + failed)) * 100
    print(f"Validation Complete: Total: {passed+failed}, Passed: {passed}, Failed: {failed}, Pass Rate: {pass_rate:.2f}%")
```

---

## Part C: Summary of Code Documentation Artifacts Created

1. **[code_walkthrough_tally_client.md](file:///C:/Users/avija/.gemini/antigravity/brain/b17f1b4c-0c87-45b9-b9be-fe3b17f6d0d3/code_walkthrough_tally_client.md)**: Full low-level walkthrough of `tally_client.py` (socket layer, `ThreadPoolExecutor` port discovery, streaming `iterparse` XML engine).
2. **[code_walkthrough_nlp_engine.md](file:///C:/Users/avija/.gemini/antigravity/brain/b17f1b4c-0c87-45b9-b9be-fe3b17f6d0d3/code_walkthrough_nlp_engine.md)**: Full low-level walkthrough of `nlp_engine.py` (ONNX C++ runtime sessions, 27-entity parameter extraction algorithms, sliding 1-to-4 word n-gram generator, RapidFuzz ambiguity interceptor).
3. **[code_walkthrough_mcp_and_suite.md](file:///C:/Users/avija/.gemini/antigravity/brain/b17f1b4c-0c87-45b9-b9be-fe3b17f6d0d3/code_walkthrough_mcp_and_suite.md)**: Full low-level walkthrough of `mcp_server.py` & `run_test_suite.py` (FastMCP tool dispatcher, Markdown report renderers, 27-parameter evaluation harness).
