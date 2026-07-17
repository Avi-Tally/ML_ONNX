import requests
import xml.etree.ElementTree as ET

def test_pdc(exclude_pdc, exclude_opt):
    company_name = "Modi Chemplast Materials Pvt Ltd"
    port = 9000
    
    pdc_val = "Yes" if exclude_pdc else "No"
    opt_val = "Yes" if exclude_opt else "No"
    
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
                <SVEXCLUDEOPTIONAL>{opt_val}</SVEXCLUDEOPTIONAL>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="CustomBillCollection">
                        <TYPE>Bill</TYPE>
                        <FETCH>Name, BillDate, ClosingBalance, Parent</FETCH>
                        <FILTERS>PendingOnly</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="PendingOnly">
                        $Parent = "Thermax Ltd" OR $Parent = "Aquatech System"
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
        print(f"\n--- Exclude PDC: {pdc_val} | Exclude Opt: {opt_val} ---")
        bills = root.findall(".//BILL")
        # Let's count how many bills are returned and print the ones that have date 20250613 or are MODI/25-26/231
        target_bills = []
        for b in bills:
            ref = b.findtext("NAME")
            parent = b.findtext("PARENT")
            date = b.findtext("BILLDATE")
            cl = b.findtext("CLOSINGBALANCE")
            if "231" in ref or "440" in ref or "439" in ref or "438" in ref or "426" in ref:
                target_bills.append(f"  Party: {parent} | Ref: {ref} | Date: {date} | Bal: {cl}")
        print(f"Total matching target bills: {len(target_bills)}")
        for tb in target_bills:
            print(tb)
    except Exception as e:
        print(f"Error: {e}")

test_pdc(exclude_pdc=False, exclude_opt=False)
test_pdc(exclude_pdc=True, exclude_opt=False)
test_pdc(exclude_pdc=False, exclude_opt=True)
test_pdc(exclude_pdc=True, exclude_opt=True)
