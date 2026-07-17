import sys
import os
sys.path.append(os.path.abspath('.'))
from tally_client import TallyClient

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

bills = client.fetch_bills(company, port, "All", exclude_pdc=False)
targets = ["Thermax Ltd", "Aquatech System"]
matching = [b for b in bills if b["party"] in targets]
print(f"Total matching bills: {len(matching)}")
# Sort by date descending
matching.sort(key=lambda x: x["date"], reverse=True)
for m in matching[:50]:
    print(f"Party: {m['party']} | Ref: {m['name']} | Date: {m['date']} | Amt: {m['amount']}")
