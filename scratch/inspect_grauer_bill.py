import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
from analytics_engine import AnalyticsEngine
import datetime

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000
today = datetime.datetime(2025, 11, 26)

bills = client.fetch_bills(company_name, port, "All", from_date=None, to_date=None, status_filter=None)
ae = AnalyticsEngine()

for b in bills:
    if "grauer" in b.get("party", "").lower():
        date_str = b.get("date") or ""
        due_str = b.get("due_date") or date_str
        amt = b.get("amount") or "0"
        
        dt = ae._parse_date(date_str)
        due_dt = ae._parse_date(due_str)
        due_dt_used = due_dt if due_dt != datetime.datetime.min else dt
        age = (today - due_dt_used).days
        
        print(f"Grauer Bill: Name={b.get('name')}, Date={date_str}, Due={due_str}, Amt={amt}, Age={age}d")
