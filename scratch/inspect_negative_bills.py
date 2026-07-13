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

# Use date bounds 1-Apr-2024 to 26-Nov-2025 (matching the screenshot period!)
# This is incredibly fast because Tally indexes BillDate!
bills = client.fetch_bills(company_name, port, "All", from_date="20240401", to_date="20251126")
print(f"Total raw bills fetched: {len(bills)}")

ae = AnalyticsEngine()

negative_bills = []
for b in bills:
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
        
    if val < 0:
        if "day" in due_str.lower():
            try:
                days_to_add = int(due_str.lower().split("day")[0].strip())
                due_dt = dt + datetime.timedelta(days=days_to_add)
            except:
                due_dt = ae._parse_date(due_str)
        else:
            due_dt = ae._parse_date(due_str)
            
        due_dt_used = due_dt if due_dt != datetime.datetime.min else dt
        age = (today - due_dt_used).days
        
        negative_bills.append({
            "name": b.get("name"),
            "party": b.get("party"),
            "amount": val,
            "parent_group": b.get("parent_group"),
            "age_days": age
        })

# Sort by absolute amount descending
negative_bills.sort(key=lambda x: abs(x["amount"]), reverse=True)

print("\nNegative Bills (Sorted by absolute amount descending):")
for idx, b in enumerate(negative_bills[:30], 1):
    print(f" {idx:2d}. Bill: {b['name']}, Party: {b['party']}, Amt: {b['amount']}, Group: {b['parent_group']}, Age: {b['age_days']}d")
