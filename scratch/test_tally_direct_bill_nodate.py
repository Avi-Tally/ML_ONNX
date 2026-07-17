import requests
import xml.etree.ElementTree as ET

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>AllBills</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="AllBills">
                        <TYPE>Bill</TYPE>
                        <FETCH>Name, ClosingBalance, Parent</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=15)
    root = ET.fromstring(response.text)
    bills = root.findall(".//BILL")
    print(f"Total bills returned: {len(bills)}")
    for b in bills[:5]:
        print(f"  Name: {b.findtext('NAME')} | Parent: {b.findtext('PARENT')} | Bal: {b.findtext('CLOSINGBALANCE')}")
except Exception as e:
    print(f"Error: {e}")
