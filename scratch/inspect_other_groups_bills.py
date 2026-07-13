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

other_bills = {}
for b in bills:
    parent_group = b.get("parent_group") or ""
    is_creditor = client.is_group_under(parent_group, "Sundry Creditors", group_map)
    is_debtor = client.is_group_under(parent_group, "Sundry Debtors", group_map)
    
    if not is_creditor and not is_debtor:
        party = b.get("party")
        amt = b.get("amount")
        if parent_group not in other_bills:
            other_bills[parent_group] = []
        other_bills[parent_group].append(f"{party}: {amt}")

print(f"Other groups count: {len(other_bills)}")
for group, blist in other_bills.items():
    print(f"Group: {group} ({len(blist)} bills):")
    for b_info in blist[:10]:
        print(f"  - {b_info}")
