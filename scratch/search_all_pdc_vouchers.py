import requests
import re

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Query Tally for any post-dated voucher
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>DebugPDCVouchers</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="DebugPDCVouchers">
                        <TYPE>Voucher</TYPE>
                        <FETCH>VoucherNumber, Date, VoucherTypeName, IsPostDated, PartyName, Amount</FETCH>
                        <FILTERS>TargetFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetFilter">
                        $IsPostDated
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
    print(f"Total post-dated vouchers in active Tally DB: {len(vouchers)}")
    for v in vouchers[:10]:
        vn_m = re.search(r'<VOUCHERNUMBER\b[^>]*>(.*?)</VOUCHERNUMBER>', v)
        dt_m = re.search(r'<DATE\b[^>]*>(.*?)</DATE>', v)
        vt_m = re.search(r'<VOUCHERTYPENAME\b[^>]*>(.*?)</VOUCHERTYPENAME>', v)
        p_m = re.search(r'<PARTYNAME\b[^>]*>(.*?)</PARTYNAME>', v)
        a_m = re.search(r'<AMOUNT\b[^>]*>(.*?)</AMOUNT>', v)
        
        vn = vn_m.group(1) if vn_m else "N/A"
        dt = dt_m.group(1) if dt_m else "N/A"
        vt = vt_m.group(1) if vt_m else "N/A"
        party = p_m.group(1) if p_m else "N/A"
        amt = a_m.group(1) if a_m else "N/A"
        print(f"  - Type: {vt} | Number: {vn} | Date: {dt} | Party: {party} | Amt: {amt}")
except Exception as e:
    print(f"Error: {e}")
