import requests
import xml.etree.ElementTree as ET

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9001

payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>DebugLedger</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="DebugLedger">
                        <TYPE>Ledger</TYPE>
                        <FETCH>Name, IsBillWiseOn</FETCH>
                        <FILTERS>TargetFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetFilter">
                        $Name = "Abhay Limited"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=10)
    root = ET.fromstring(response.text)
    ledgers = root.findall(".//LEDGER")
    print(f"Total matching ledgers: {len(ledgers)}")
    for l in ledgers:
        name = l.findtext("NAME")
        bw = l.findtext("ISBILLWISEON")
        print(f"Ledger Name: {name} | IsBillWiseOn: {bw}")
except Exception as e:
    print(f"Error: {e}")
