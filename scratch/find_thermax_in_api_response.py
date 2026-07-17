import sys
import os
sys.path.append(os.path.abspath('.'))
from tally_client import TallyClient
import json

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Fetch all bills with exclude_pdc=True
bills_with_pdc = client.fetch_bills(company, port, "All", exclude_pdc=True)
print(f"Total bills fetched (exclude_pdc=True): {len(bills_with_pdc)}")

targets = ["Thermax Ltd", "Aquatech System"]
found = [b for b in bills_with_pdc if b["party"] in targets]
print(f"Found {len(found)} bills for Thermax & Aquatech:")
for f in found:
    print(f"Party: {f['party']} | Ref: {f['name']} | Date: {f['date']} | Amt: {f['amount']} | Settled: {f['is_settled']}")
