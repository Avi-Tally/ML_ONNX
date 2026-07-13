import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Fetch the raw XML for some bills of Aquatech System
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
                        <FETCH>Name, BillDate, ClosingBalance, OpeningBalance, Parent</FETCH>
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

print("Aquatech System (Debtor) Bills:")
count = 0
for b in bills:
    party = b.findtext("PARENT")
    if party and "aquatech" in party.lower():
        name = b.findtext("NAME")
        c_bal = b.findtext("CLOSINGBALANCE")
        o_bal = b.findtext("OPENINGBALANCE")
        p_group = b.findtext("PARENTGROUP")
        print(f" - Bill: {name}, Closing: {c_bal}, Opening: {o_bal}, Group: {p_group}")
        count += 1
        if count >= 10:
            break
            
print("\nSample Creditor Bills:")
count = 0
for b in bills:
    p_group = b.findtext("PARENTGROUP")
    if p_group and "creditor" in p_group.lower():
        name = b.findtext("NAME")
        party = b.findtext("PARENT")
        c_bal = b.findtext("CLOSINGBALANCE")
        o_bal = b.findtext("OPENINGBALANCE")
        print(f" - Bill: {name}, Party: {party}, Closing: {c_bal}, Opening: {o_bal}, Group: {p_group}")
        count += 1
        if count >= 10:
            break
