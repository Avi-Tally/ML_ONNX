import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Let's test IsDr, IsCr, IsDebit, IsCredit on the Bill collection!
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
                        <COMPUTE>IsDr: $IsDr</COMPUTE>
                        <COMPUTE>IsCr: $IsCr</COMPUTE>
                        <COMPUTE>IsDebit: $IsDebit</COMPUTE>
                        <COMPUTE>IsCredit: $IsCredit</COMPUTE>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

res = client.execute_xml_request(port, payload)
root = ET.fromstring(res)
bills = root.findall(".//BILL")

print("Sample Bills:")
for b in bills[:10]:
    name = b.findtext("NAME")
    party = b.findtext("PARENT")
    is_dr = b.findtext("ISDR")
    is_cr = b.findtext("ISCR")
    is_deb = b.findtext("ISDEBIT")
    is_cred = b.findtext("ISCREDIT")
    amt = b.findtext("CLOSINGBALANCE")
    print(f" - Bill: {name}, Party: {party}, Amt: {amt}, IsDr: {is_dr}, IsCr: {is_cr}, IsDebit: {is_deb}, IsCredit: {is_cred}")
