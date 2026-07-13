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
    if cleared_on.strip() != "" or val == 0:
        continue
        
    is_creditor = is_group_under(parent_group, "Sundry Creditors", group_map)
    is_debtor = is_group_under(parent_group, "Sundry Debtors", group_map)
    
    if is_creditor or is_debtor:
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
        
        # Calculate net_val based on group type and sign
        if is_creditor:
            net_val = val
        else: # is_debtor
            net_val = -val
            
        # We only want to include payables in this list (where net_val > 0)
        # Wait, if net_val < 0 (an advance/debit note), we still want to keep it to net it out!
        payables.append({
            "name": elem.findtext("NAME"),
            "party": elem.findtext("PARENT"),
            "net_val": net_val,
            "age_days": age
        })

print(f"Total payables: {len(payables)}")

total_pending = 0.0
under_30 = 0.0
over_30 = 0.0

for p in payables:
    net_val = p["net_val"]
    age = p["age_days"]
    
    # Overdue means age > 0
    if age > 0:
        total_pending += net_val
        if age < 30:
            under_30 += net_val
        else:
            over_30 += net_val

print(f"\nCalculated Totals:")
print(f" - Total Pending Overdue: ₹ {total_pending:,.2f}")
print(f" - Overdue < 30 days: ₹ {under_30:,.2f}")
print(f" - Overdue > 30 days: ₹ {over_30:,.2f}")
