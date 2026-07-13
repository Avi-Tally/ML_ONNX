import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Let's fetch using the client's official fetch_bills method
bills_client = client.fetch_bills(company_name, port, "Payable", from_date=None, to_date="26-Nov-2025")
print(f"Client fetch_bills count: {len(bills_client)}")

sum_client = sum(abs(float(b["amount"])) for b in bills_client)
print(f"Client fetch_bills sum: {sum_client:,.2f}")

# Let's print the first 10 bills from the client fetch
for b in bills_client[:5]:
    print(f" - Bill: {b['name']}, Party: {b['party']}, Amt: {b['amount']}, ParentGroup: {b.get('parent_group')}")
