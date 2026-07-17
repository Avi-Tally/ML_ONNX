import requests
import xml.etree.ElementTree as ET

def query_tally_with_pdc_var(exclude_pdc):
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
                        <COMPUTE>ParentGroup: $Parent:Ledger:$Parent</COMPUTE>
                        <FILTERS>PendingOnly</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="PendingOnly">
                        ($Parent = "Aquatech System" OR $Parent = "Thermax Ltd") AND 
                        ($Name = "MODI/25-26/231" OR $Name = "MODI/25-26/440" OR $Name = "MODI/25-26/439" OR $Name = "MODI/25-26/438" OR $Name = "MODI/25-26/426")
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
        print(f"Total bills returned: {len(bills)}")
        for b in bills:
            ref = b.findtext("NAME")
            parent = b.findtext("PARENT")
            cl = b.findtext("CLOSINGBALANCE")
            print(f"  Party: {parent} | Ref: {ref} | Bal: {cl}")
    except Exception as e:
        print(f"Error: {e}")

print("Testing Tally response with different SVEXCLUDEPOSTDATED settings for the 5 target bills:")
query_tally_with_pdc_var(exclude_pdc=False)
query_tally_with_pdc_var(exclude_pdc=True)
