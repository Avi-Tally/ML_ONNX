import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
from datetime import datetime

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

try:
    group_map = client.get_group_hierarchy_map(company, port)
    bills = client.fetch_bills(company, port, "All")
    
    payables = []
    for b in bills:
        pg_lower = b.get("parent_group", "").strip().lower()
        party_lower = b.get("party", "").strip().lower()
        is_creditor = (
            client.is_group_under(pg_lower, "sundry creditors", group_map) or
            client.is_group_under(pg_lower, "trade payables", group_map) or
            any(w in pg_lower for w in ["creditor", "payable", "supplier", "vendor"]) or
            any(w in party_lower for w in ["creditor", "supplier", "vendor"])
        )
        is_debtor = (
            client.is_group_under(pg_lower, "sundry debtors", group_map) or
            client.is_group_under(pg_lower, "trade receivables", group_map) or
            any(w in pg_lower for w in ["debtor", "receivable", "customer", "client", "sales"]) or
            any(w in party_lower for w in ["debtor", "customer", "client"])
        )
        
        is_payable = False
        if is_creditor and not is_debtor:
            is_payable = True
        elif is_debtor and not is_creditor:
            is_payable = False
        else:
            try:
                amt = float(b.get("amount", 0))
            except:
                amt = 0.0
            is_payable = amt > 0
            
        if is_payable:
            payables.append(b)
            
    print(f"Total payables: {len(payables)}")
    
    # Check date parsing
    def parse_dt(d_str):
        if not d_str: return datetime.min
        try: return datetime.strptime(d_str, "%Y%m%d")
        except: return datetime.min
        
    dates = [parse_dt(p.get("date")) for p in payables if p.get("date")]
    due_dates = [parse_dt(p.get("due_date")) for p in payables if p.get("due_date")]
    
    print(f"Invoice Date range: {min(dates).strftime('%Y-%m-%d') if dates else 'N/A'} to {max(dates).strftime('%Y-%m-%d') if dates else 'N/A'}")
    print(f"Due Date range: {min(due_dates).strftime('%Y-%m-%d') if due_dates else 'N/A'} to {max(due_dates).strftime('%Y-%m-%d') if due_dates else 'N/A'}")
    
    # Check how many are invoiced on or before 26-Nov-2025
    ref_dt = datetime(2025, 11, 26)
    invoiced_before_ref = [p for p in payables if parse_dt(p.get("date")) <= ref_dt]
    print(f"Invoiced on or before 26-Nov-2025: {len(invoiced_before_ref)}")
    
    # Print dates of some invoiced before ref
    print("\nSample payables invoiced on or before 26-Nov-2025:")
    for p in invoiced_before_ref[:10]:
        print(f"  Party: {p.get('party'):<30} | Invoice Date: {p.get('date')} | Due Date: {p.get('due_date')} | Amount: {p.get('amount')}")
        
    # Check age calculation relative to 26-Nov-2025
    matching_age_bills = []
    # Print 50 most recent due dates before 26-Nov-2025
    recent_due_dates = sorted([parse_dt(p.get("due_date")) for p in invoiced_before_ref if parse_dt(p.get("due_date")) <= ref_dt], reverse=True)
    print("\n50 most recent due dates <= 26-Nov-2025:")
    for d in recent_due_dates[:50]:
        print(f"  {d.strftime('%Y-%m-%d')}")
except Exception as e:
    print("Error:", e)
