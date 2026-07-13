import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Fetch all bills of RELIANCE NEW SOLAR ENERGY LIMITED
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
                        <FILTER>IsReliance</FILTER>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="IsReliance">
                        $Parent = "RELIANCE NEW SOLAR ENERGY LIMITED"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

res = client.execute_xml_request(port, payload)
root = ET.fromstring(res)
bills = root.findall(".//BILL")

print(f"Total Reliance bills: {len(bills)}")
for b in bills:
    name = b.findtext("NAME")
    c_bal = b.findtext("CLOSINGBALANCE")
    o_bal = b.findtext("OPENINGBALANCE")
    print(f" - Bill: {name}, Closing: {c_bal}, Opening: {o_bal}")
