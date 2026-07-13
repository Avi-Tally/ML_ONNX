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

pos_sum = 0.0
neg_sum = 0.0

for b in bills:
    if "reliance new solar" in b.get("party", "").lower():
        date_str = b.get("date") or ""
        due_str = b.get("due_date") or date_str
        amt = b.get("amount") or "0"
        cleared_on = b.get("cleared_on") or ""
        
        try:
            val = float(amt.strip())
        except:
            val = 0.0
            
        dt = ae._parse_date(date_str)
        if dt == datetime.datetime.min or dt > today:
            continue
        if cleared_on.strip() != "" or val == 0:
            continue
            
        if val > 0:
            pos_sum += val
        else:
            neg_sum += abs(val)

print(f"Reliance Positive Sum: ₹ {pos_sum:,.2f}")
print(f"Reliance Negative Sum: ₹ {neg_sum:,.2f}")
print(f"Reliance Net: ₹ {pos_sum - neg_sum:,.2f}")
