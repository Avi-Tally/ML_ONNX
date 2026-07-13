import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>LedgerDetails</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="LedgerDetails">
                        <TYPE>Ledger</TYPE>
                        <FETCH>Name, Parent</FETCH>
                        <FILTER>IsGrauer</FILTER>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="IsGrauer">
                        $Name contains "Grauer"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

res = client.execute_xml_request(port, payload)
root = ET.fromstring(res)
ledgers = root.findall(".//LEDGER")

for l in ledgers:
    print(f"Ledger: {l.findtext('NAME')}, Parent: {l.findtext('PARENT')}")
