import requests
import xml.etree.ElementTree as ET

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Let's query Tally for all vouchers on 26-Nov-2025 (20251126)
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>ReceiptVouchers</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="ReceiptVouchers">
                        <TYPE>Voucher</TYPE>
                        <FETCH>VoucherNumber, Date, IsOptional, IsPostDated, PartyLedgerName, Ledgers, LedgerEntries.*, AllLedgerEntries.*</FETCH>
                        <FILTERS>TargetVouchers</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetVouchers">
                        $Date = $$Date:"20251126"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=10)
    print("Response text:")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
