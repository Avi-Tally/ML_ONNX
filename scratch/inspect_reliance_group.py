import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Fetch the ledger details for RELIANCE NEW SOLAR ENERGY LIMITED
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
                        <FETCH>Name, Parent, OpeningBalance</FETCH>
                        <FILTER>IsReliance</FILTER>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="IsReliance">
                        $Name = "RELIANCE NEW SOLAR ENERGY LIMITED"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

res = client.execute_xml_request(port, payload)
root = ET.fromstring(res)
ledger = root.find(".//LEDGER")

if ledger is not None:
    print("RELIANCE NEW SOLAR ENERGY LIMITED details:")
    print(" - Name:", ledger.findtext("NAME"))
    print(" - Parent Group:", ledger.findtext("PARENT"))
    print(" - Opening Balance:", ledger.findtext("OPENINGBALANCE"))
else:
    print("Ledger not found!")
