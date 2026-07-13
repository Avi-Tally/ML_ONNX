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

# Fetch all raw bills
bills = client.fetch_bills(company_name, port, "All", from_date=None, to_date=None, status_filter=None)
print(f"Total bills: {len(bills)}")

ae = AnalyticsEngine()

# Let's compute payables using the following combinations:
# Payables = (is_creditor_ledger and val > 0) OR (is_debtor_ledger and val < 0)
# But wait! Do we net out (is_creditor_ledger and val < 0) OR (is_debtor_ledger and val > 0)?
# Let's test BOTH netted and non-netted!

p_only_sum = 0.0
p_only_under = 0.0
p_only_over = 0.0

netted_sum = 0.0
netted_under = 0.0
netted_over = 0.0

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
    if cleared_on.strip() != "" or val == 0:
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
        
        # Scenario A: Non-netted (only Credit/payable items)
        if (is_creditor and val > 0) or (is_debtor and val < 0):
            p_val = val if is_creditor else -val
            p_only_sum += p_val
            if age < 30:
                p_only_under += p_val
            else:
                p_only_over += p_val
                
        # Scenario B: Netted (Credit - Debit)
        # We net out debit notes from creditors, and debit balances from debtors
        if is_creditor or is_debtor:
            if is_creditor:
                n_val = val # positive is credit/payable, negative is debit/advance
            else: # is_debtor
                n_val = -val # negative is credit/payable, positive is debit/receivable
            
            # Wait, if we net everything, do we get the exact number?
            netted_sum += n_val
            if age < 30:
                netted_under += n_val
            else:
                netted_over += n_val

print("Scenario A: Non-Netted Payables (Only Credit balances):")
print(f" - Total Pending Overdue: ₹ {p_only_sum:,.2f}")
print(f" - Overdue < 30 days: ₹ {p_only_under:,.2f}")
print(f" - Overdue > 30 days: ₹ {p_only_over:,.2f}")

print("\nScenario B: Fully Netted Payables (Credit - Debit):")
print(f" - Total Pending Overdue: ₹ {netted_sum:,.2f}")
print(f" - Overdue < 30 days: ₹ {netted_under:,.2f}")
print(f" - Overdue > 30 days: ₹ {netted_over:,.2f}")
