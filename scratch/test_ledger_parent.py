import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Let's test different methods of getting parent group name from Ledger via Bill
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
                        <COMPUTE>ParentGroup1: $Parent:Ledger:$Parent</COMPUTE>
                        <COMPUTE>ParentGroup2: $Parent:Ledger:Parent</COMPUTE>
                        <COMPUTE>ParentGroup3: $ParentGroup:Ledger:$Parent</COMPUTE>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

res = client.execute_xml_request(port, payload)
root = ET.fromstring(res)
bills = root.findall(".//BILL")

print("Sample Bills with parent groups:")
for b in bills[:10]:
    name = b.findtext("NAME")
    party = b.findtext("PARENT")
    p1 = b.findtext("PARENTGROUP1")
    p2 = b.findtext("PARENTGROUP2")
    p3 = b.findtext("PARENTGROUP3")
    print(f" - Bill: {name}, Party: {party}, P1: {p1}, P2: {p2}, P3: {p3}")
