import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
from analytics_engine import AnalyticsEngine
import datetime

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000
today = datetime.datetime(2025, 11, 26)

group_map = client.get_group_hierarchy_map(company_name, port)
bills = client.fetch_bills(company_name, port, "All", from_date=None, to_date=None, status_filter=None)

ae = AnalyticsEngine()

# Helper to trace group nature
# Tally's primary groups:
# Credit nature: "Current Liabilities", "Sundry Creditors", "Provisions", "Duties & Taxes", "Loans (Liability)", "Suspense A/c", "Capital Account"
# Debit nature: "Current Assets", "Sundry Debtors", "Loans & Advances (Asset)", "Investments", "Fixed Assets", "Branch / Divisions"

def get_natural_balance(group_name, g_map):
    curr = group_name.strip().lower()
    visited = set()
    while curr and curr not in visited:
        # Check credit primary groups
        if curr in ["sundry creditors", "current liabilities", "provisions", "duties & taxes", "loans (liability)", "capital account"]:
            return "Credit"
        # Check debit primary groups
        if curr in ["sundry debtors", "current assets", "loans & advances (asset)", "investments", "fixed assets", "branch / divisions"]:
            return "Debit"
        visited.add(curr)
        curr = g_map.get(curr)
    # Default fallback
    return "Credit" if "creditor" in group_name.lower() or "liability" in group_name.lower() else "Debit"

payables_total = 0.0
payables_under = 0.0
payables_over = 0.0

for b in bills:
    date_str = b.get("date") or ""
    due_str = b.get("due_date") or date_str
    amt = b.get("amount") or "0"
    parent_group = b.get("parent_group") or ""
    cleared_on = b.get("cleared_on") or ""
    
    try:
        val = float(amt.strip())
    except:
        val = 0.0
        
    dt = ae._parse_date(date_str)
    if dt == datetime.datetime.min or dt > today:
        continue
    if cleared_on.strip() != "" or val == 0:
        continue
        
    # Calculate age
    if "day" in due_str.lower():
        try:
            days_to_add = int(due_str.lower().split("day")[0].strip())
            due_dt = dt + datetime.timedelta(days=days_to_add)
        except:
            due_dt = ae._parse_date(due_str)
    else:
        due_dt = ae._parse_date(due_str)
        
    due_dt_used = due_dt if due_dt != datetime.datetime.min else dt
    age = (today - due_dt_used).days
    
    if age > 0:
        nature = get_natural_balance(parent_group, group_map)
        
        is_payable = False
        if nature == "Credit" and val > 0:
            is_payable = True
            p_val = val
        elif nature == "Debit" and val < 0:
            is_payable = True
            p_val = -val
            
        if is_payable:
            payables_total += p_val
            if age < 30:
                payables_under += p_val
            else:
                payables_over += p_val

print("Calculated Payables by Natural Balance:")
print(f" - Total Pending Overdue: ₹ {payables_total:,.2f}")
print(f" - Overdue < 30 days: ₹ {payables_under:,.2f}")
print(f" - Overdue > 30 days: ₹ {payables_over:,.2f}")
