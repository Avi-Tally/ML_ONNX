import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
from analytics_engine import AnalyticsEngine
import datetime
import itertools

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000
today = datetime.datetime(2025, 11, 26)

bills = client.fetch_bills(company_name, port, "All", from_date=None, to_date=None, status_filter=None)
ae = AnalyticsEngine()

# Let's rebuild the old logic's bills:
# open_val > 0 means is_creditor
old_creditor_bills = []
all_other_bills = []

for b in bills:
    date_str = b.get("date") or ""
    due_str = b.get("due_date") or date_str
    amt = b.get("amount") or "0"
    open_amt = b.get("opening_amount") or "0"
    cleared_on = b.get("cleared_on") or ""
    
    try:
        val = float(amt.strip())
    except:
        val = 0.0
        
    try:
        open_val = float(open_amt.strip())
    except:
        open_val = 0.0
        
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
    
    info = {"party": b.get("party"), "bill": b.get("name"), "val": val, "open_val": open_val, "age": age}
    
    is_old_creditor = (open_val > 0)
    if is_old_creditor:
        old_creditor_bills.append(info)
    else:
        all_other_bills.append(info)

# Let's check sums for old_creditor_bills:
under_30 = sum(b["val"] for b in old_creditor_bills if b["age"] < 30)
over_30 = sum(b["val"] for b in old_creditor_bills if b["age"] > 30)

print(f"Old logic matches for age < 30: {under_30:,.2f}")
print(f"Old logic sum for age > 30: {over_30:,.2f}")

target_diff = 4468899.13
print(f"Target Diff: {target_diff:,.2f}")

# Search for subsets of all_other_bills or negative old_creditor_bills that sum to target_diff
candidates = []
# Include absolute value of negative bills from old_creditors:
for b in old_creditor_bills:
    if b["val"] < 0:
        candidates.append({"desc": f"OldCredNeg:{b['party']}:{b['bill']}", "val": abs(b["val"])})
# Include positive bills from all_other_bills:
for b in all_other_bills:
    if b["val"] > 0:
        candidates.append({"desc": f"OtherPos:{b['party']}:{b['bill']}", "val": b["val"]})
# Include absolute value of negative bills from all_other_bills:
for b in all_other_bills:
    if b["val"] < 0:
        candidates.append({"desc": f"OtherNeg:{b['party']}:{b['bill']}", "val": abs(b["val"])})

print(f"Total candidates: {len(candidates)}")

# Search for small combinations:
found = False
for r in [1, 2, 3]:
    for comb in itertools.combinations(candidates, r):
        s = sum(item["val"] for item in comb)
        if abs(s - target_diff) < 10.0:
            print(f"Match (size {r}): {[item['desc'] + '=' + str(item['val']) for item in comb]} = {s}")
            found = True

if not found:
    print("No combination of up to 3 candidates matched.")
