import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

bills = client.fetch_bills(company, port, "All", reference_date="29-Nov-2025")
print(f"Total raw bills: {len(bills)}")

nov_bills = []
for b in bills:
    date_str = b.get("date", "")
    if date_str.startswith("202511"):
        nov_bills.append(b)

print(f"\nFound {len(nov_bills)} bills dated in November 2025:")
for b in nov_bills:
    print(f"  Party: {b.get('party'):<30} | Bill: {b.get('name'):<20} | Date: {b.get('date')} | Due: {b.get('due_date')} | Amt: {b.get('amount')} | Group: {b.get('parent_group')}")
