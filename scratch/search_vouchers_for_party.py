import requests
import re

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Query Tally for all vouchers of party "Thermax Ltd"
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>DebugThermaxVouchers</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="DebugThermaxVouchers">
                        <TYPE>Voucher</TYPE>
                        <FETCH>VoucherNumber, Date, VoucherTypeName, IsPostDated, LedgerEntries</FETCH>
                        <FILTERS>TargetFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetFilter">
                        $$IsLedgerWithName:"Thermax Ltd"
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
    print(f"Total vouchers for Thermax Ltd: {len(vouchers)}")
    for i, v in enumerate(vouchers):
        print(f"\n--- Voucher {i+1} ---")
        print(v)
except Exception as e:
    print(f"Error: {e}")
