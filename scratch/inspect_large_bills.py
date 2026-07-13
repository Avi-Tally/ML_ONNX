import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# We will execute the XML request directly to get ALL bills
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

target_names = ["MODI/23-24/2681", "1613", "MODI/23-24/2417", "ABG 10% USD 161000"]

print("Inspecting Target Bills from XML:")
for b in bills:
    name = b.findtext("NAME")
    if name and any(tn in name for tn in target_names):
        party = b.findtext("PARENT")
        c_bal = b.findtext("CLOSINGBALANCE")
        o_bal = b.findtext("OPENINGBALANCE")
        p_group = b.findtext("PARENTGROUP")
        print(f" - Bill Name: {name}")
        print(f"   Party: {party}")
        print(f"   Closing: {c_bal}")
        print(f"   Opening: {o_bal}")
        print(f"   ParentGroup: {p_group}")
        print(f"   Raw XML elements:")
        for child in b:
            print(f"     <{child.tag}>: {child.text}")
        print("-" * 50)
