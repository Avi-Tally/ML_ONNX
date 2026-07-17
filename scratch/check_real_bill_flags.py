import requests
import xml.etree.ElementTree as ET

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9001

payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>DebugBills</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="DebugBills">
                        <TYPE>Bill</TYPE>
                        <FETCH>Name, Parent, IsAdvance, IsNewRef, IsAgstRef, BillType</FETCH>
                        <COMPUTE>IsAdvance: $IsAdvance</COMPUTE>
                        <COMPUTE>IsNewRef: $IsNewRef</COMPUTE>
                        <COMPUTE>IsAgstRef: $IsAgstRef</COMPUTE>
                        <FILTERS>TargetFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetFilter">
                        $Name = "8100018557"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=20)
    root = ET.fromstring(response.text)
    bills = root.findall(".//BILL")
    print(f"Total matching bills: {len(bills)}")
    for b in bills:
        print("Raw XML details for real bill 8100018557:")
        for child in b:
            print(f"  {child.tag}: {child.text}")
except Exception as e:
    print(f"Error: {e}")
