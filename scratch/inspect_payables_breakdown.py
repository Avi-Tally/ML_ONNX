import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient
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

from analytics_engine import AnalyticsEngine
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

pos_count = 0
neg_count = 0
pos_sum = 0.0
neg_sum = 0.0

total_count = 0

for elem in bills:
    date_str = elem.findtext("BILLDATE") or ""
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
        
    if is_group_under(parent_group, "Sundry Creditors", group_map):
        total_count += 1
        if val > 0:
            pos_count += 1
            pos_sum += val
        else:
            neg_count += 1
            neg_sum += val

print(f"Total Sundry Creditors pending bills: {total_count}")
print(f"Positive bills count: {pos_count}, Sum: ₹ {pos_sum:,.2f}")
print(f"Negative bills count: {neg_count}, Sum: ₹ {neg_sum:,.2f}")
