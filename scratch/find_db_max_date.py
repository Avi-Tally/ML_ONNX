import sys
import os
sys.path.append(os.path.abspath('.'))
from tally_client import TallyClient

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

bills = client.fetch_bills(company, port, "All", exclude_pdc=False)
dates = [b["date"] for b in bills if b["date"]]
print(f"Total bills in active Tally DB: {len(bills)}")
if dates:
    print(f"Latest bill date in DB: {max(dates)}")
    print(f"Earliest bill date in DB: {min(dates)}")
