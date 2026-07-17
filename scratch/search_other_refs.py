import sys
import os
sys.path.append(os.path.abspath('.'))
from tally_client import TallyClient

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

bills = client.fetch_bills(company, port, "All", exclude_pdc=False)
print(f"Total bills in active Tally DB: {len(bills)}")

target_refs = ["MODI/25-26/440", "MODI/25-26/439", "MODI/25-26/438", "MODI/25-26/426"]
for ref in target_refs:
    matching = [b for b in bills if ref in b["name"]]
    print(f"Found {len(matching)} bills matching '{ref}':")
    for m in matching:
        print(f"  - Party: {m['party']} | Ref: {m['name']} | Date: {m['date']} | Amt: {m['amount']}")
