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
    "debtor_neg": {"sum": 0.0, "count": 0}
}

for b in bills:
    date_str = b.get("date") or ""
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
        
    is_creditor = client.is_group_under(parent_group, "Sundry Creditors", group_map)
    is_debtor = client.is_group_under(parent_group, "Sundry Debtors", group_map)
    
    if is_creditor:
        key = "creditor_pos" if val > 0 else "creditor_neg"
    elif is_debtor:
        key = "debtor_pos" if val > 0 else "debtor_neg"
    else:
        continue
        
    splits[key]["sum"] += abs(val)
    splits[key]["count"] += 1

print("Pending Splits (regardless of age, but dt <= today):")
for k, v in splits.items():
    print(f" - {k:12s}: Sum = ₹ {v['sum']:,.2f} ({v['count']} bills)")
