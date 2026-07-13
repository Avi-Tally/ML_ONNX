import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient
from analytics_engine import AnalyticsEngine
import datetime

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000
today = datetime.datetime(2025, 11, 26)

# 1. Fetch group map locally
def get_group_hierarchy_map(company, port):
    payload = f"""<ENVELOPE>
        <HEADER>
            <VERSION>1</VERSION>
            <TALLYREQUEST>Export</TALLYREQUEST>
            <TYPE>Collection</TYPE>
            <ID>GroupList</ID>
        </HEADER>
        <BODY>
            <DESC>
                <STATICVARIABLES>
                    <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                    <SVCURRENTCOMPANY>{company}</SVCURRENTCOMPANY>
                </STATICVARIABLES>
                <TDL>
                    <TDLMESSAGE>
                        <COLLECTION NAME="GroupList">
                            <TYPE>Group</TYPE>
                            <FETCH>Name, Parent</FETCH>
                        </COLLECTION>
                    </TDLMESSAGE>
                </TDL>
            </DESC>
        </BODY>
    </ENVELOPE>"""
    res = client.execute_xml_request(port, payload)
    root = ET.fromstring(res)
    groups = root.findall(".//GROUP")
    group_parents = {}
    for g in groups:
        name = g.findtext("NAME") or g.attrib.get("NAME", "")
        parent = g.findtext("PARENT") or ""
        if name:
            group_parents[name.strip().lower()] = parent.strip().lower()
    return group_parents

group_map = get_group_hierarchy_map(company_name, port)

# 2. Fetch all raw bills
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>CustomBillCollection</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="CustomBillCollection">
                        <TYPE>Bill</TYPE>
                        <FETCH>Name, BillDate, BillCreditPeriod, ClosingBalance, OpeningBalance, Parent, ClearedOn</FETCH>
                        <COMPUTE>ParentGroup: $Parent:Ledger:$Parent</COMPUTE>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

res = client.execute_xml_request(port, payload)
root = ET.fromstring(res)
bills = root.findall(".//BILL")

ae = AnalyticsEngine()

# Helpers
def is_group_under(group_name, target_parent, g_map):
    curr = group_name.strip().lower()
    target = target_parent.strip().lower()
    visited = set()
    while curr and curr not in visited:
        if curr == target:
            return True
        visited.add(curr)
        curr = g_map.get(curr)
    return False

payables = []
for elem in bills:
    name = elem.findtext("NAME") or ""
    party = elem.findtext("PARENT") or ""
    date_str = elem.findtext("BILLDATE") or ""
    due_str = elem.findtext("BILLCREDITPERIOD") or date_str
    amt = elem.findtext("CLOSINGBALANCE") or "0"
    parent_group = elem.findtext("PARENTGROUP") or ""
    cleared_on = elem.findtext("CLEAREDON") or ""
    
    try:
        val = float(amt.strip())
    except:
        val = 0.0
        
    dt = ae._parse_date(date_str)
    if dt == datetime.datetime.min or dt > today:
        continue
        
    is_cleared = (cleared_on.strip() != "" or val == 0)
    if is_cleared:
        continue
        
    # Classify by hierarchy
    if is_group_under(parent_group, "Sundry Creditors", group_map):
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
        
        payables.append({
            "name": name,
            "party": party,
            "amount": val,
            "age_days": age
        })

print(f"Total payables matched in Python: {len(payables)}")

# Calculate the totals:
total_pending = 0.0
under_30 = 0.0
over_30 = 0.0

for p in payables:
    # In Tally:
    # - Credit is represented as a NEGATIVE number in CLOSINGBALANCE.
    # - Debit is represented as a POSITIVE number in CLOSINGBALANCE.
    # But in Payables, a Credit balance means we owe them (positive outstanding).
    # So we do: outstanding_val = -p["amount"]
    net_val = -p["amount"]
    age = p["age_days"]
    
    # Overdue means age > 0.
    # In Tally UI, is the "Pending Amount" column only showing overdue, or all pending?
    # The screenshot title says: "Details of: Overdue Bills".
    # And at the bottom it shows:
    # - Pending Amount: 19,65,01,413.37
    # - (< 30 days) : 15,62,757.58
    # - (> 30 days) : 19,49,38,655.79
    # Wait, the sum of <30 and >30 is exactly 19,65,01,413.37!
    # So the "Pending Amount" column only shows OVERDUE bills (age > 0)!
    if age > 0:
        total_pending += net_val
        if age < 30:
            under_30 += net_val
        else:
            over_30 += net_val

print(f"Total Pending Amount (Credit - Debit): ₹ {total_pending:,.2f}")
print(f"Pending Overdue Amount (age < 30 days): ₹ {under_30:,.2f}")
print(f"Pending Overdue Amount (age >= 30 days): ₹ {over_30:,.2f}")
