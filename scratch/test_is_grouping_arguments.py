import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Let's test both argument orders for IsGroupingOf
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
                        <FETCH>Name, BillDate, ClosingBalance, Parent</FETCH>
                        <COMPUTE>ParentGroup: $Parent:Ledger:$Parent</COMPUTE>
                        <COMPUTE>Order1: $$IsGroupingOf:"Sundry Creditors":($Parent:Ledger:$Parent)</COMPUTE>
                        <COMPUTE>Order2: $$IsGroupingOf:($Parent:Ledger:$Parent):"Sundry Creditors"</COMPUTE>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

res = client.execute_xml_request(port, payload)
root = ET.fromstring(res)
bills = root.findall(".//BILL")

print("Creditor Bills:")
c_count = 0
for b in bills:
    p_group = b.findtext("PARENTGROUP")
    if p_group and "creditor" in p_group.lower():
        name = b.findtext("NAME")
        party = b.findtext("PARENT")
        o1 = b.findtext("ORDER1")
        o2 = b.findtext("ORDER2")
        print(f" - Bill: {name}, Party: {party}, Group: {p_group}, Order1 (Creditors, Group): {o1}, Order2 (Group, Creditors): {o2}")
        c_count += 1
        if c_count >= 5:
            break
            
print("\nDebtor Bills:")
d_count = 0
for b in bills:
    p_group = b.findtext("PARENTGROUP")
    if p_group and "debtor" in p_group.lower():
        name = b.findtext("NAME")
        party = b.findtext("PARENT")
        o1 = b.findtext("ORDER1")
        o2 = b.findtext("ORDER2")
        print(f" - Bill: {name}, Party: {party}, Group: {p_group}, Order1 (Creditors, Group): {o1}, Order2 (Group, Creditors): {o2}")
        d_count += 1
        if d_count >= 5:
            break
