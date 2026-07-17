import sys
import os
sys.path.append(os.path.abspath('.'))
from tally_client import TallyClient

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Query Receivables on 29-Nov-2025
bills = client.fetch_bills(company, port, "Receivable", reference_date="20251129", exclude_pdc=True)
print(f"Total receivables on 2025-11-29 (exclude_pdc=True): {len(bills)}")

matching = [b for b in bills if b["party"] in ["Thermax Ltd", "Aquatech System"]]
print(f"Found {len(matching)} receivables for Thermax & Aquatech:")
for m in matching:
    print(f"Party: {m['party']} | Ref: {m['name']} | Date: {m['date']} | Amt: {m['amount']}")
