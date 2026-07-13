import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
from analytics_engine import AnalyticsEngine
from nlp_engine import NLPEngine

client = TallyClient()
engine = AnalyticsEngine()
nlp = NLPEngine(client)

# Parse query parameters
params = nlp.parse_query("Total overdue payable till 26-11-25")["parameters"]
print("Parameters:", params)

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Fetch ALL bills without date filters from Tally
all_bills = client.fetch_bills(company_name, port, "Payable", from_date=None, to_date=None)
print(f"Total raw bills fetched from Tally: {len(all_bills)}")

# Now run the filter manually and check which bills are excluded
final_bills = []
excluded_reasons = {}

import datetime

for b in all_bills:
    try:
        raw_amt = float(b["amount"])
    except:
        raw_amt = 0.0
    abs_amt = abs(raw_amt)
    b["abs_amount"] = abs_amt
    
    # Calculate age relative to 26-Nov-2025
    today = datetime.datetime(2025, 11, 26)
    b["parsed_date"] = engine._parse_date(b.get("date", ""))
    
    due_str = b.get("due_date", "").strip()
    if "day" in due_str.lower():
        try:
            days_to_add = int(due_str.lower().split("day")[0].strip())
            if b["parsed_date"] != datetime.datetime.min:
                b["parsed_due_date"] = b["parsed_date"] + datetime.timedelta(days=days_to_add)
            else:
                b["parsed_due_date"] = datetime.datetime.min
        except:
            b["parsed_due_date"] = engine._parse_date(due_str)
    else:
        b["parsed_due_date"] = engine._parse_date(due_str)
        
    b_due = b["parsed_due_date"] if b["parsed_due_date"] != datetime.datetime.min else b["parsed_date"]
    b["age_days"] = (today - b_due).days if b_due != datetime.datetime.min else 0
    b["is_cleared"] = (b.get("cleared_on", "").strip() != "" or raw_amt == 0)
    
    include = True
    reason = []
    
    if params.get("overdue_only") and b["age_days"] <= 0:
        include = False
        reason.append(f"Not overdue (age_days={b['age_days']})")
        
    # Date filter "till_today" (up to 26-Nov-2025)
    target_date = b["parsed_due_date"] if params.get("date_target") == "due_date" else b["parsed_date"]
    if target_date != datetime.datetime.min:
        if target_date > today:
            include = False
            reason.append(f"Target date {target_date.strftime('%Y-%m-%d')} > {today.strftime('%Y-%m-%d')}")
            
    if include:
        final_bills.append(b)
    else:
        excluded_reasons[b["name"]] = (b, ", ".join(reason))

# Sum of final_bills
sum_abs = sum(b["abs_amount"] for b in final_bills)
print(f"Total processed absolute bills: {len(final_bills)}, Sum: ₹ {sum_abs:,.2f}")

# Look for the discrepancy bills in excluded_reasons
discrepancies = []
for name, (b, r) in excluded_reasons.items():
    if b["parsed_date"] != datetime.datetime.min and b["parsed_date"] <= today:
        if b["age_days"] > 0:
            discrepancies.append((b, r))

print(f"\nDiscrepancy bills that are actually overdue before 26-Nov-2025 but excluded:")
for b, r in discrepancies[:20]:
    print(f" - Bill: {b.get('name')}, Date: {b.get('date')}, Due: {b.get('due_date')}, Party: {b.get('party')}, Amount: {b.get('amount')}, Age: {b.get('age_days')}d, Reason: {r}")
