import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
import xml.etree.ElementTree as ET

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
# Check if port 9000 works now
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
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

try:
    res = client.execute_xml_request(port, payload)
    root = ET.fromstring(res)
    for l in root.findall(".//LEDGER"):
        name = l.attrib.get("NAME", l.findtext("NAME", "")).strip().lower()
        if "balaji" in name or "v trans" in name or "smit" in name or "wabag" in name or "aquatech" in name:
            print(f"Ledger: '{l.attrib.get('NAME')}' | Parent: '{l.findtext('PARENT')}'")
except Exception as e:
    print("Error:", e)
