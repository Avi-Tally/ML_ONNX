import requests
import xml.etree.ElementTree as ET

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

def run_query(exclude_pdc):
    pdc_val = "Yes" if exclude_pdc else "No"
    
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
                <SVEXCLUDEPOSTDATED>{pdc_val}</SVEXCLUDEPOSTDATED>
                <SVEXCLUDEOPTIONAL>{pdc_val}</SVEXCLUDEOPTIONAL>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="CustomBillCollection">
                        <TYPE>Bill</TYPE>
                        <FETCH>Name, BillDate, ClosingBalance, Parent</FETCH>
                        <FILTERS>PendingOnly</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="PendingOnly">
                        ($Parent = "Thermax Ltd" OR $Parent = "Aquatech System") AND $ClosingBalance != 0
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

    url = f"http://localhost:{port}"
    try:
        # Since Port 9000 might be hung, let's try calling it.
        # If it times out, we will catch it.
        response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=15)
        root = ET.fromstring(response.text)
        print(f"\n--- SVEXCLUDEPOSTDATED: {pdc_val} ---")
        bills = root.findall(".//BILL")
        print(f"Total bills returned: {len(bills)}")
        for b in bills:
            ref = b.findtext("NAME")
            cl = b.findtext("CLOSINGBALANCE")
            date = b.findtext("BILLDATE")
            # If target bill
            if "231" in ref or "440" in ref or "439" in ref or "438" in ref or "426" in ref:
                print(f"  TARGET FOUND: Ref: {ref} | Date: {date} | Bal: {cl}")
    except Exception as e:
        print(f"Error for exclude_pdc={exclude_pdc}: {e}")

run_query(exclude_pdc=False)
run_query(exclude_pdc=True)
