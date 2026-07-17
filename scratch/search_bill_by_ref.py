import sys
import os
sys.path.append(os.path.abspath('.'))
from tally_client import TallyClient

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

bills = client.fetch_bills(company, port, "All", exclude_pdc=False)
print(f"Total bills in active Tally DB: {len(bills)}")

matching = [b for b in bills if "231" in b["name"]]
print(f"Found {len(matching)} bills matching '231':")
for m in matching:
    print(f"Party: {m['party']} | Ref: {m['name']} | Date: {m['date']} | Amt: {m['amount']}")
