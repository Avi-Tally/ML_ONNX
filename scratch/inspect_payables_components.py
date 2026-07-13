import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
from mcp_server import _query_tally_internal
from analytics_engine import AnalyticsEngine
import datetime

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000
today = datetime.datetime(2025, 11, 26)

bills = client.fetch_bills(company_name, port, "Payable")
ae = AnalyticsEngine()

total_val = 0.0
under_30 = 0.0
over_30 = 0.0

special_cases = []

for b in bills:
    date_str = b.get("date") or ""
    due_str = b.get("due_date") or date_str
    cleared_on = b.get("cleared_on") or ""
    
    dt = ae._parse_date(date_str)
    if dt == datetime.datetime.min or dt > today:
        continue
    if cleared_on.strip() != "":
        continue
        
    # Calculate age
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
    
    if age > 0:
        val = b.get("normalized_payables_amount", 0.0)
        total_val += val
        if age < 30:
            under_30 += val
        else:
            over_30 += val
            
        if val == 401106.0 or val == 401105.25 or "4011" in str(val):
            special_cases.append(b)
        # Check if amount is negative in XML
        try:
            raw = float(b.get("amount", "0"))
            if raw < 0:
                print(f"Included negative bill: {b.get('party')} : {b.get('name')} = {val} (age: {age})")
        except:
            pass

print(f"\nCalculated Total: ₹ {total_val:,.2f}")
print(f"Calculated < 30: ₹ {under_30:,.2f}")
print(f"Calculated > 30: ₹ {over_30:,.2f}")
print(f"Special cases matching 401k: {special_cases}")
