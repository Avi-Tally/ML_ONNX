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

ae = AnalyticsEngine()

rec_total = 0.0
rec_under = 0.0
rec_over = 0.0

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
        is_creditor = client.is_group_under(parent_group, "Sundry Creditors", group_map)
        is_debtor = client.is_group_under(parent_group, "Sundry Debtors", group_map)
        
        b_val = 0.0
        if is_debtor:
            b_val = val # positive is positive, negative (advance) is negative
        elif is_creditor:
            if val < 0:
                b_val = -val # negative is positive (receivable)
                
        rec_total += b_val
        if age < 30:
            rec_under += b_val
        else:
            rec_over += b_val
            
        if "reliance" in b.get("party", "").lower():
            print(f"Reliance parsed: Bill={b.get('name')}, val={val}, b_val={b_val}, is_debtor={is_debtor}, age={age}")

print("\nCalculated Receivables:")
print(f" - Total Pending Overdue: ₹ {rec_total:,.2f}")
print(f" - Overdue < 30 days: ₹ {rec_under:,.2f}")
print(f" - Overdue > 30 days: ₹ {rec_over:,.2f}")
