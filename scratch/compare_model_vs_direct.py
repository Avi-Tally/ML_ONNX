import sys
import os
import json
from datetime import datetime
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
from analytics_engine import AnalyticsEngine
from nlp_engine import NLPEngine

def main():
    company = "Modi Chemplast Materials Pvt Ltd"
    port = 9000
    query_str = "List outstanding payables whose age < 40 days on 29-nov-2025"
    
    client = TallyClient()
    analytics = AnalyticsEngine()
    nlp = NLPEngine()
    
    # Context (simulating what mcp_server does)
    context_dict = {
        "current_date": "26-Nov-2025",
        "from_date": "01-Apr-2025",
        "to_date": "31-Mar-2026",
        "company_name": company
    }
    
    print("Fetching Payable bills from Tally as of 29-Nov-2025...")
    raw_bills = client.fetch_bills(company, port, "Payable", reference_date="29-Nov-2025")
    print(f"Total raw bills fetched: {len(raw_bills)}\n")
    
    # Let's inspect the raw bills for any due date in [29-Nov-2025 - 40 days, 29-Nov-2025]
    print("Scanning raw bills for due dates in [20-Oct-2025, 29-Nov-2025]...")
    from datetime import datetime, timedelta
    ref_dt = datetime(2025, 11, 29)
    start_dt = ref_dt - timedelta(days=40)
    
    def parse_dt(d_str):
        if not d_str: return datetime.min
        try: return datetime.strptime(d_str, "%Y%m%d")
        except: return datetime.min
        
    found_any = False
    for b in raw_bills:
        due_dt = parse_dt(b.get("due_date"))
        if due_dt == datetime.min:
            due_dt = parse_dt(b.get("date"))
        if start_dt <= due_dt <= ref_dt:
            print(f"  FOUND: Party={b.get('party')} | Bill={b.get('name')} | Date={b.get('date')} | Due={b.get('due_date')} | Amt={b.get('amount')} | Group={b.get('parent_group')}")
            found_any = True
    if not found_any:
        print("  No raw bills found in this due date window at all!")
    print("")
    
    # ---------------------------------------------------------
    # 1. DIRECT TO TALLY (Without Model)
    # ---------------------------------------------------------
    print("--- 1. DIRECT TO TALLY (Without Model) ---")
    direct_params = {
        "date_filter": None,
        "age_filter": {"operator": "<", "days": 40},
        "amount_filter": None,
        "reference_date": "29-Nov-2025",
        "overdue_only": False,
        "is_bill_query": False,
        "date_target": "due_date"
    }
    print(f"Direct Parameters: {json.dumps(direct_params)}")
    
    direct_bills = analytics.process_bills(raw_bills, "GET_PAYABLES", direct_params, today_str="29-Nov-2025")
    
    direct_total = sum(b["abs_amount"] for b in direct_bills)
    
    print(f"Direct Output -> Bills count: {len(direct_bills)} | Total Amount: {direct_total:.2f}")
    
    print("\nSample of Direct Bills:")
    for b in sorted(direct_bills, key=lambda x: x.get("age_days", 0))[:5]:
        print(f"  Party: {b.get('party')} | Age: {b.get('age_days')}d | Amount: {b.get('amount')}")
    print("...")
        
    # ---------------------------------------------------------
    # 2. THROUGH NLP MODEL
    # ---------------------------------------------------------
    print("\n--- 2. THROUGH NLP MODEL ---")
    parsed_res = nlp.parse_query(query_str)
    
    # The NLP engine returns {"status": "success", "parameters": {...}}
    model_params = parsed_res.get("parameters", {})
    print(f"Model Parsed Parameters: {json.dumps(model_params)}")
    
    model_bills = analytics.process_bills(raw_bills, "GET_PAYABLES", model_params, today_str="29-Nov-2025")
    
    model_total = sum(b["abs_amount"] for b in model_bills)
    
    print(f"Model Output -> Bills count: {len(model_bills)} | Total Amount: {model_total:.2f}")
    
    print("\nSample of Model Bills:")
    for b in sorted(model_bills, key=lambda x: x.get("age_days", 0))[:5]:
        print(f"  Party: {b.get('party')} | Age: {b.get('age_days')}d | Amount: {b.get('amount')}")
    print("...")

    # ---------------------------------------------------------
    # 3. COMPARISON
    # ---------------------------------------------------------
    print("\n--- 3. COMPARISON ---")
    if direct_total == model_total and len(direct_bills) == len(model_bills):
        print("SUCCESS: The direct manual parameters and the model-parsed parameters yield EXACTLY the same results.")
    else:
        print("MISMATCH DETECTED!")
        print(f"Direct Total: {direct_total:.2f} | Model Total: {model_total:.2f}")
        print(f"Direct Count: {len(direct_bills)} | Model Count: {len(model_bills)}")

if __name__ == "__main__":
    main()
