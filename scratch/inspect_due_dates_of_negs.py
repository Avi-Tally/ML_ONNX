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

bills = client.fetch_bills(company_name, port, "All")
group_map = client.get_group_hierarchy_map(company_name, port)

# Let's count how many negative bills have due_date != date, or are not "On Account"
active_negatives = []
for b in bills:
    date_str = b.get("date") or ""
    due_str = b.get("due_date") or date_str
    amt = b.get("amount") or "0"
    cleared_on = b.get("cleared_on") or ""
    
    try:
        val = float(amt.strip())
    except:
        val = 0.0
        
    if val < 0 and not cleared_on:
        # Check if it has a valid age > 30
        ae = AnalyticsEngine()
        dt = ae._parse_date(date_str)
        if dt != datetime.datetime.min and dt <= today:
            due_dt = ae._parse_date(due_str)
            due_dt_used = due_dt if due_dt != datetime.datetime.min else dt
            age = (today - due_dt_used).days
            if age > 30:
                active_negatives.append({
                    "party": b.get("party"),
                    "name": b.get("name"),
                    "val": val,
                    "date": date_str,
                    "due_date": due_str
                })

print(f"Total active negatives with age > 30: {len(active_negatives)}")
print("First 20 active negatives with age > 30:")
for b in active_negatives[:20]:
    print(f"  - Party: {b['party']}, Bill: {b['name']}, Amt: {b['val']}, Date: {b['date']}, Due: {b['due_date']}")
