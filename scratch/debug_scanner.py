import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
from datetime import datetime

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

bills = client.fetch_bills(company, port, "All", reference_date="29-Nov-2025")

print("Let's look at all bills of 'Ion Exchange' or 'Thermax':")
for b in bills:
    if "ion exchange" in b.get("party", "").lower() or "thermax" in b.get("party", "").lower():
        print(f"Party: {b.get('party')} | Bill: {b.get('name')} | Date: {b.get('date')} | Due: {b.get('due_date')} | Amt: {b.get('amount')}")
