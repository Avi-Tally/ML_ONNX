import requests
import xml.etree.ElementTree as ET

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Let's query Tally for ALL bills of Thermax Ltd
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>AllThermaxBills</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="AllThermaxBills">
                        <TYPE>Bill</TYPE>
                        <FETCH>Name, BillDate, ClosingBalance, Parent, ClearedOn</FETCH>
                        <FILTERS>TargetFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetFilter">
                        $Parent = "Thermax Ltd"
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
    bills = root.findall(".//BILL")
    print(f"Total Thermax bills found (all): {len(bills)}")
    for b in bills:
        ref = b.findtext("NAME")
        date = b.findtext("BILLDATE")
        cl = b.findtext("CLOSINGBALANCE")
        cleared = b.findtext("CLEAREDON")
        if "231" in ref or cl == "0.00" or cl == "0" or cleared:
            print(f"  Ref: {ref} | Date: {date} | Bal: {cl} | ClearedOn: {cleared}")
except Exception as e:
    print(f"Error: {e}")
