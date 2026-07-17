import requests
import xml.etree.ElementTree as ET

def query_tally_thermax(exclude_pdc):
    company_name = "Modi Chemplast Materials Pvt Ltd"
    port = 9000
    
    pdc_var = f"<SVEXCLUDEPOSTDATED>{'Yes' if exclude_pdc else 'No'}</SVEXCLUDEPOSTDATED>"
    
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
                {pdc_var}
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="CustomBillCollection">
                        <TYPE>Bill</TYPE>
                        <FETCH>Name, BillDate, ClosingBalance, Parent</FETCH>
                        <FILTERS>PendingOnly</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="PendingOnly">
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
        print(f"\n--- Exclude PDC: {exclude_pdc} ---")
        bills = root.findall(".//BILL")
        for b in bills:
            ref = b.findtext("NAME")
            cl = b.findtext("CLOSINGBALANCE")
            print(f"  Ref: {ref} | Bal: {cl}")
    except Exception as e:
        print(f"Error: {e}")

query_tally_thermax(exclude_pdc=False)
query_tally_thermax(exclude_pdc=True)
