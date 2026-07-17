import requests
import re

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Query all vouchers dated between 29-Nov-2025 and 31-Dec-2025
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
                        <FETCH>VoucherNumber, Date, VoucherTypeName, IsPostDated, PartyName, Amount</FETCH>
                        <FILTERS>TargetFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetFilter">
                        $Date &gt;= $$Date:"20251129" AND $Date &lt;= $$Date:"20251231"
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
    print(f"Total vouchers in date range: {len(vouchers)}")
    for v in vouchers:
        vn_m = re.search(r'<VOUCHERNUMBER\b[^>]*>(.*?)</VOUCHERNUMBER>', v)
        dt_m = re.search(r'<DATE\b[^>]*>(.*?)</DATE>', v)
        vt_m = re.search(r'<VOUCHERTYPENAME\b[^>]*>(.*?)</VOUCHERTYPENAME>', v)
        ipd_m = re.search(r'<ISPOSTDATED\b[^>]*>(.*?)</ISPOSTDATED>', v)
        p_m = re.search(r'<PARTYNAME\b[^>]*>(.*?)</PARTYNAME>', v)
        a_m = re.search(r'<AMOUNT\b[^>]*>(.*?)</AMOUNT>', v)
        
        vn = vn_m.group(1) if vn_m else "N/A"
        dt = dt_m.group(1) if dt_m else "N/A"
        vt = vt_m.group(1) if vt_m else "N/A"
        ipd = ipd_m.group(1) if ipd_m else "N/A"
        party = p_m.group(1) if p_m else "N/A"
        amt = a_m.group(1) if a_m else "N/A"
        print(f"Type: {vt} | Number: {vn} | Date: {dt} | IsPostDated: {ipd} | Party: {party} | Amt: {amt}")
except Exception as e:
    print(f"Error: {e}")
