import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Set status_filter=None to disable the slow TDL formula filter!
bills = client.fetch_bills(company_name, port, "Payable", from_date=None, to_date=None, status_filter=None)
print(f"Total raw bills fetched: {len(bills)}")

print("Searching for Grauer bill 792 in client payables:")
found = False
for b in bills:
    if b.get("name") == "792" or "grauer" in b.get("party", "").lower():
        print(f" - Bill: {b.get('name')}, Party: {b.get('party')}, Amt: {b.get('amount')}, Opening: {b.get('opening_amount')}, Group: {b.get('parent_group')}, Cleared: {b.get('cleared_on')}")
        found = True

if not found:
    print("Not found in 'Payable' bills!")
