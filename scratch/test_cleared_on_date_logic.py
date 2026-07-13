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

group_map = client.get_group_hierarchy_map(company_name, port)
bills = client.fetch_bills(company_name, port, "All", from_date=None, to_date=None, status_filter=None)

ae = AnalyticsEngine()

# Let's count and sum under the correct date-aware cleared logic!
# A bill is cleared as of 'today' if cleared_on is not empty AND cleared_date <= today.
# Otherwise, it is pending!

rec_total = 0.0
rec_under = 0.0
rec_over = 0.0

for b in bills:
    date_str = b.get("date") or ""
    due_str = b.get("due_date") or date_str
    amt = b.get("amount") or "0"
    parent_group = b.get("parent_group") or ""
    cleared_on = b.get("cleared_on") or ""
    
    try:
        val = float(amt.strip())
    except:
        val = 0.0
        
    dt = ae._parse_date(date_str)
    if dt == datetime.datetime.min or dt > today:
        continue
        
    # Check if cleared as of today
    is_cleared_as_of_today = False
    if cleared_on.strip() != "":
        cleared_dt = ae._parse_date(cleared_on)
        if cleared_dt != datetime.datetime.min and cleared_dt <= today:
            is_cleared_as_of_today = True
            
    if is_cleared_as_of_today or val == 0:
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
        is_creditor = client.is_group_under(parent_group, "Sundry Creditors", group_map)
        is_debtor = client.is_group_under(parent_group, "Sundry Debtors", group_map)
        
        # Let's test if the screenshot is Receivables (Receivables = debtor_pos + creditor_neg - debtor_neg)
        # But wait! Let's check Strategy 1 (all positive bills, regardless of group)
        # Wait, let's just compute Strategy 1 with the new cleared logic:
        # Strategy 1 is: val > 0
        if val > 0:
            rec_total += val
            if age < 30:
                rec_under += val
            else:
                rec_over += val

print("Strategy 1 (Positive XML amounts) with date-aware cleared logic:")
print(f" - Total Overdue: ₹ {rec_total:,.2f}")
print(f" - Overdue < 30 days: ₹ {rec_under:,.2f}")
print(f" - Overdue > 30 days: ₹ {rec_over:,.2f}")
