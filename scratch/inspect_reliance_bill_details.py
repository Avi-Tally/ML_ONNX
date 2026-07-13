import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

bills = client.fetch_bills(company_name, port, "All")
print(f"Total bills fetched: {len(bills)}")

for b in bills:
    if "reliance new solar" in b.get("party", "").lower():
        print(f"Reliance Bill: {b}")
