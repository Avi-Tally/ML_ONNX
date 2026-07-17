import requests
import re

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# We query all vouchers that contain the bill reference "MODI/25-26/231"
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>DebugVouchers</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="DebugVouchers">
                        <TYPE>Voucher</TYPE>
                        <FETCH>VoucherNumber, Date, VoucherTypeName, IsPostDated, LedgerEntries</FETCH>
                        <FILTERS>TargetFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetFilter">
                        $$IsLedgerWithBillName:"MODI/25-26/231"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=20)
    vouchers = re.findall(r'<VOUCHER\b.*?</VOUCHER>', response.text, re.DOTALL)
    print(f"Total matching vouchers for bill: {len(vouchers)}")
    for v in vouchers:
        print("Raw Voucher XML:")
        print(v)
except Exception as e:
    print(f"Error: {e}")
