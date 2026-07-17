import requests
import re

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

target_numbers = ["MODI/25-26/231", "MODI/25-26/440", "MODI/25-26/439", "MODI/25-26/438", "MODI/25-26/426"]

# Query Tally for Sales vouchers with these numbers
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>DebugSales</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="DebugSales">
                        <TYPE>Voucher</TYPE>
                        <FETCH>VoucherNumber, Date, VoucherTypeName, PartyName, Amount</FETCH>
                        <FILTERS>TargetFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetFilter">
                        $VoucherTypeName = "Sales"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=30)
    vouchers = re.findall(r'<VOUCHER\b.*?</VOUCHER>', response.text, re.DOTALL)
    print(f"Total sales vouchers fetched: {len(vouchers)}")
    numbers = []
    for v in vouchers:
        vn_m = re.search(r'<VOUCHERNUMBER\b[^>]*>(.*?)</VOUCHERNUMBER>', v)
        if vn_m:
            numbers.append(vn_m.group(1).strip())
    print("Sales Voucher Numbers:", sorted(numbers))
except Exception as e:
    print(f"Error: {e}")
