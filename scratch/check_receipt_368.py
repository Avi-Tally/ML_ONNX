import requests
import re

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9001

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
                        $VoucherNumber = "368" OR $VoucherNumber = "0368" OR $VoucherNumber = "368/25-26"
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
    print(f"Total matching vouchers: {len(vouchers)}")
    for v in vouchers:
        print("\nVoucher Details:")
        tags = re.findall(r'<([A-Z0-9a-z_.]+)\b[^>]*>(.*?)</\1>', v)
        for tag, val in tags:
            val_s = val.strip()
            if val_s and val_s != "None":
                print(f"  {tag}: {val_s}")
except Exception as e:
    print(f"Error: {e}")
