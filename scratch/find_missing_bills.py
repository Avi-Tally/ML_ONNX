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

# Fetch all raw bills
bills = client.fetch_bills(company_name, port, "All", from_date=None, to_date=None, status_filter=None)
print(f"Total bills: {len(bills)}")

ae = AnalyticsEngine()

# Group 1: Sundry Creditors negative bills
creditor_neg_sum = 0.0
creditor_neg_count = 0

# Group 2: Sundry Debtors negative bills
debtor_neg_sum = 0.0
debtor_neg_count = 0

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
    
    if age > 30 and val < 0:
        is_creditor = client.is_group_under(parent_group, "Sundry Creditors", group_map)
        is_debtor = client.is_group_under(parent_group, "Sundry Debtors", group_map)
        
        if is_creditor:
            creditor_neg_sum += abs(val)
            creditor_neg_count += 1
            print(f"Creditor Neg: Party={b.get('party')}, Bill={b.get('name')}, Amt={val}, Age={age}")
        elif is_debtor:
            debtor_neg_sum += abs(val)
            debtor_neg_count += 1
            print(f"Debtor Neg: Party={b.get('party')}, Bill={b.get('name')}, Amt={val}, Age={age}")

print(f"\nSummary for age > 30:")
print(f" - Creditor Negative Bills Sum: ₹ {creditor_neg_sum:,.2f} ({creditor_neg_count} bills)")
print(f" - Debtor Negative Bills Sum: ₹ {debtor_neg_sum:,.2f} ({debtor_neg_count} bills)")
