import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Let's fetch all bills and find the exact raw TDL/XML data for Va Tech Wabag bill MODI/25-26/1235
# We can do this by using a custom TDL collection or inspect the response XML
# Let's just run a query using fetch_bills and print the full dict first:
bills = client.fetch_bills(company_name, port, "All", from_date=None, to_date=None)
for b in bills:
    if "wabag" in b.get("party", "").lower() or "1235" in b.get("name", ""):
        print(f"Bill details: {json.dumps(b, indent=2) if 'json' in globals() else b}")
