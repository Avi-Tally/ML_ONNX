import requests
import xml.etree.ElementTree as ET

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Query Tally for all vouchers whose number is 368
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>VoucherNumber368</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="VoucherNumber368">
                        <TYPE>Voucher</TYPE>
                        <FETCH>VoucherNumber, Date, IsOptional, IsPostDated, PartyLedgerName, Ledgers, VoucherTypeName</FETCH>
                        <FILTERS>TargetVouchers</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetVouchers">
                        $VoucherNumber = "368"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=10)
    print("Raw Response:")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
