import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
from datetime import datetime, timedelta

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Fetch bills as of 29-Oct-2025
bills = client.fetch_bills(company, port, "Payable", reference_date="29-Oct-2025")
print(f"Total Payables fetched as of 29-Oct-2025: {len(bills)}")

ref_dt = datetime(2025, 10, 29)
start_dt = ref_dt - timedelta(days=40)

found = []
for b in bills:
    # parse date
    p_date = datetime.min
    d_str = b.get("date", "")
    if len(d_str) == 8 and d_str.isdigit():
        p_date = datetime.strptime(d_str, "%Y%m%d")
        
    # parse due date
    due_str = b.get("due_date", "").strip()
    p_due = datetime.min
    if "day" in due_str.lower():
        try:
            days_to_add = int(due_str.lower().split("day")[0].strip())
            if p_date != datetime.min:
                p_due = p_date + timedelta(days=days_to_add)
        except:
            pass
    else:
        if len(due_str) == 8 and due_str.isdigit():
            p_due = datetime.strptime(due_str, "%Y%m%d")
            
    if p_due == datetime.min:
        p_due = p_date
        
    age = (ref_dt - p_due).days
    
    # Check if bill is pending (ClosingBalance != 0)
    try:
        cb = float(b.get("amount", "0"))
    except:
        cb = 0.0
        
    if start_dt <= p_due <= ref_dt:
        found.append((b, p_due, age, cb))

print(f"\nFound {len(found)} payables in due date range [{start_dt.strftime('%Y-%m-%d')}, {ref_dt.strftime('%Y-%m-%d')}]:")
for b, p_due, age, cb in sorted(found, key=lambda x: x[1], reverse=True):
    print(f"  Party: {b.get('party'):<30} | Bill: {b.get('name'):<20} | Date: {b.get('date')} | Due: {b.get('due_date')} (Computed: {p_due.strftime('%Y-%m-%d')}) | Age: {age}d | Pending Amt: {cb}")
