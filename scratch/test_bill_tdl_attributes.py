import requests
import xml.etree.ElementTree as ET

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Let's query a few bills of Aquatech System
# And fetch candidate methods/computes on the Bill object
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
                <SVCURRENTDATE>20251129</SVCURRENTDATE>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="CustomBillCollection">
                        <TYPE>Bill</TYPE>
                        <!-- We fetch standard fields plus candidates -->
                        <FETCH>Name, BillDate, ClosingBalance, Parent</FETCH>
                        <COMPUTE>valPostDated: $PostDated</COMPUTE>
                        <COMPUTE>valPDCAmount: $PDCAmount</COMPUTE>
                        <COMPUTE>valPDCBalance: $PDCBalance</COMPUTE>
                        <COMPUTE>valBillPDC: $BillPDC</COMPUTE>
                        <FILTERS>TargetFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetFilter">
                        $Parent = "Aquatech System"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=120)
    root = ET.fromstring(response.text)
    bills = root.findall(".//BILL")
    print(f"Total target bills returned: {len(bills)}")
    for b in bills[:5]:
        ref = b.findtext("NAME")
        cl = b.findtext("CLOSINGBALANCE")
        print(f"\nBill Ref: {ref} | ClosingBalance: {cl}")
        for child in b:
            if child.tag not in ["NAME", "CLOSINGBALANCE", "PARENT", "BILLDATE"]:
                print(f"  {child.tag}: {child.text}")
except Exception as e:
    print(f"Error: {e}")
