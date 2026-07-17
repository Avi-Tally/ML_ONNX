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
                        <FETCH>Name, ClosingBalance, Parent, BillType, IsOnAccount</FETCH>
                        <COMPUTE>BillType: $BillType</COMPUTE>
                        <COMPUTE>IsOnAccount: $IsOnAccount</COMPUTE>
                        <FILTERS>TargetFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetFilter">
                        $Name = "1400115918"
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
        ref = b.findtext("NAME")
        party = b.findtext("PARENT")
        bt = b.findtext("BILLTYPE")
        ioa = b.findtext("ISONACCOUNT")
        print(f"Ref: {ref} | Party: {party} | BillType: {bt} | IsOnAccount: {ioa}")
except Exception as e:
    print(f"Error: {e}")
