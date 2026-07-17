import requests
import xml.etree.ElementTree as ET

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Let's query bills of Aquatech System using CHILD OF
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
                        <CHILD OF>"Aquatech System"</CHILD OF>
                        <FETCH>Name, BillDate, ClosingBalance, Parent</FETCH>
                        <COMPUTE>valPostDated: $PostDated</COMPUTE>
                        <COMPUTE>valPDCAmount: $PDCAmount</COMPUTE>
                        <COMPUTE>valPDCBalance: $PDCBalance</COMPUTE>
                        <COMPUTE>valBillPDC: $BillPDC</COMPUTE>
                    </COLLECTION>
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
    print(f"Total bills returned: {len(bills)}")
    for b in bills:
        ref = b.findtext("NAME")
        cl = b.findtext("CLOSINGBALANCE")
        # Print candidate computed fields
        pdc = b.findtext("VALPOSTDATED")
        pdc_amt = b.findtext("VALPDCAMOUNT")
        pdc_bal = b.findtext("VALPDCBALANCE")
        bill_pdc = b.findtext("VALBILLPDC")
        print(f"Ref: {ref} | Bal: {cl} | PostDated: {pdc} | PDCAmount: {pdc_amt} | PDCBalance: {pdc_bal} | BillPDC: {bill_pdc}")
except Exception as e:
    print(f"Error: {e}")
