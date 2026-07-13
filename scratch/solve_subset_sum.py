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

# Get all negative bills with age > 30 and group them by group type (Creditor vs Debtor)
creditor_negatives = []
debtor_negatives = []

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
    
    if age > 30 and val < 0:
        is_creditor = "creditor" in parent_group.lower()
        is_debtor = "debtor" in parent_group.lower()
        
        info = {"party": b.get("party"), "bill": b.get("name"), "val": abs(val)}
        if is_creditor:
            creditor_negatives.append(info)
        elif is_debtor:
            debtor_negatives.append(info)

target_diff = 4923295.75

print(f"Target Difference: {target_diff:,.2f}")

# Let's find any single bill or pair of bills in creditor_negatives or debtor_negatives that matches!
# Search in Creditor negatives:
print("\nChecking single creditor negatives:")
for b in creditor_negatives:
    if abs(b["val"] - target_diff) < 1.0:
        print(f"Match found! Creditor bill: {b}")

print("\nChecking single debtor negatives:")
for b in debtor_negatives:
    if abs(b["val"] - target_diff) < 1.0:
        print(f"Match found! Debtor bill: {b}")

# Checking pairs:
print("\nChecking pairs in creditor negatives:")
for i in range(len(creditor_negatives)):
    for j in range(i+1, len(creditor_negatives)):
        s = creditor_negatives[i]["val"] + creditor_negatives[j]["val"]
        if abs(s - target_diff) < 1.0:
            print(f"Match: {creditor_negatives[i]} + {creditor_negatives[j]}")

print("\nChecking pairs in debtor negatives:")
for i in range(len(debtor_negatives)):
    for j in range(i+1, len(debtor_negatives)):
        s = debtor_negatives[i]["val"] + debtor_negatives[j]["val"]
        if abs(s - target_diff) < 1.0:
            print(f"Match: {debtor_negatives[i]} + {debtor_negatives[j]}")
            
# Let's do a general subset sum search using dynamic programming or basic backtracking for small subset size
# We will check if any combination of up to 4 elements matches.
all_items = creditor_negatives + debtor_negatives
print(f"\nSearching all combinations up to 3 elements among {len(all_items)} negatives:")
import itertools
found = False
for r in [1, 2, 3]:
    for comb in itertools.combinations(all_items, r):
        s = sum(item["val"] for item in comb)
        if abs(s - target_diff) < 10.0: # allow 10 rs margin
            print(f"Match (size {r}): {[item['party'] + ':' + item['bill'] + '=' + str(item['val']) for item in comb]} = {s}")
            found = True
            
if not found:
    print("No combination of up to 3 items matched.")
