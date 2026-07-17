import sys
import os
sys.path.append(os.path.abspath('.'))
from tally_client import TallyClient

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Fetch bills with reference_date="20251129"
bills = client.fetch_bills(company, port, "All", reference_date="20251129", exclude_pdc=True)
print(f"Total bills on 2025-11-29 (exclude_pdc=True): {len(bills)}")

matching = [b for b in bills if "231" in b["name"]]
print(f"Found {len(matching)} bills matching '231' on 2025-11-29:")
for m in matching:
    print(f"Party: {m['party']} | Ref: {m['name']} | Date: {m['date']} | Amt: {m['amount']}")
