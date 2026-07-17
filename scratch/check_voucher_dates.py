import requests
import re

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Query Tally for all Sales vouchers and print their numbers and dates
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>DebugSalesDates</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="DebugSalesDates">
                        <TYPE>Voucher</TYPE>
                        <FETCH>VoucherNumber, Date, VoucherTypeName, PartyName</FETCH>
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
    print(f"Total sales vouchers: {len(vouchers)}")
    results = []
    for v in vouchers:
        vn_m = re.search(r'<VOUCHERNUMBER\b[^>]*>(.*?)</VOUCHERNUMBER>', v)
        dt_m = re.search(r'<DATE\b[^>]*>(.*?)</DATE>', v)
        p_m = re.search(r'<PARTYNAME\b[^>]*>(.*?)</PARTYNAME>', v)
        vn = vn_m.group(1).strip() if vn_m else "N/A"
        dt = dt_m.group(1).strip() if dt_m else "N/A"
        party = p_m.group(1).strip() if p_m else "N/A"
        results.append((dt, vn, party))
    results.sort()
    for r in results:
        print(f"Date: {r[0]} | Number: {r[1]} | Party: {r[2]}")
except Exception as e:
    print(f"Error: {e}")
