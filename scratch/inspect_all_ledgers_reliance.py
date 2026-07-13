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
        <ID>LedgerList</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="LedgerList">
                        <TYPE>Ledger</TYPE>
                        <FETCH>Name, Parent, OpeningBalance</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

res = client.execute_xml_request(port, payload)
root = ET.fromstring(res)
ledgers = root.findall(".//LEDGER")

print(f"Total ledgers fetched: {len(ledgers)}")
for l in ledgers:
    name = l.findtext("NAME") or l.attrib.get("NAME", "")
    if name and "reliance" in name.lower():
        parent = l.findtext("PARENT") or ""
        op = l.findtext("OPENINGBALANCE") or "0"
        print(f" - Ledger: {name}, Parent: {parent}, OpeningBalance: {op}")
