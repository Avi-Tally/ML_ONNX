import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
from datetime import datetime, timedelta

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

bills = client.fetch_bills(company, port, "Payable", reference_date="29-Nov-2025")
print(f"Total Payables: {len(bills)}")

parsed_bills = []
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
        
    parsed_bills.append((b, p_due))

# Sort by due date descending, but only those <= 29-Nov-2025
filtered_past = [(b, p_due) for b, p_due in parsed_bills if p_due <= datetime(2025, 11, 29)]
filtered_past_sorted = sorted(filtered_past, key=lambda x: x[1], reverse=True)

print("\nTop 40 most recent payables with due date <= 29-Nov-2025:")
for b, p_due in filtered_past_sorted[:40]:
    print(f"  Party: {b.get('party'):<30} | Bill: {b.get('name'):<20} | Date: {b.get('date')} | Due: {b.get('due_date')} (Computed: {p_due.strftime('%Y-%m-%d')}) | Amt: {b.get('amount')}")
