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

bills = client.fetch_bills(company_name, port, "All", from_date=None, to_date=None, status_filter=None)
group_map = client.get_group_hierarchy_map(company_name, port)
ae = AnalyticsEngine()

debtor_negs = []
for b in bills:
    parent_group = b.get("parent_group") or ""
    is_debtor = client.is_group_under(parent_group, "Sundry Debtors", group_map)
    amt = b.get("amount") or "0"
    cleared_on = b.get("cleared_on") or ""
    
    try:
        val = float(amt.strip())
    except:
        val = 0.0
        
    if is_debtor and val < 0:
        debtor_negs.append(b)

print(f"Total debtor negatives found: {len(debtor_negs)}")
print("First 15 debtor negatives:")
for b in debtor_negs[:15]:
    print(f"  - Party: {b.get('party')}, Bill: {b.get('name')}, Amt: {b.get('amount')}, Cleared: {b.get('cleared_on')}")
