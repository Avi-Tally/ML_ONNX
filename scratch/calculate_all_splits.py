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

splits = {
    "creditor_pos": {"sum": 0.0, "count": 0},
    "creditor_neg": {"sum": 0.0, "count": 0},
    "debtor_pos": {"sum": 0.0, "count": 0},
    "debtor_neg": {"sum": 0.0, "count": 0},
    "other_pos": {"sum": 0.0, "count": 0},
    "other_neg": {"sum": 0.0, "count": 0}
}

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
        
        if is_creditor:
            key = "creditor_pos" if val > 0 else "creditor_neg"
        elif is_debtor:
            key = "debtor_pos" if val > 0 else "debtor_neg"
        else:
            key = "other_pos" if val > 0 else "other_neg"
            
        splits[key]["sum"] += abs(val)
        splits[key]["count"] += 1

print("Database Splits (age > 0):")
for k, v in splits.items():
    print(f" - {k:12s}: Sum = ₹ {v['sum']:,.2f} ({v['count']} bills)")
