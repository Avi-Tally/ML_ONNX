import requests
import re

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Fetch all vouchers from the database (up to 1000) and check for "Thermax" or "Aquatech"
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>AllVouchers</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="AllVouchers">
                        <TYPE>Voucher</TYPE>
                        <FETCH>VoucherNumber, Date, VoucherTypeName, IsPostDated, PartyName, Amount, LedgerEntries</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=60)
    vouchers = re.findall(r'<VOUCHER\b.*?</VOUCHER>', response.text, re.DOTALL)
    print(f"Total vouchers fetched: {len(vouchers)}")
    
    targets = ["thermax", "aquatech"]
    found_count = 0
    for v in vouchers:
        v_lower = v.lower()
        if any(t in v_lower for t in targets):
            found_count += 1
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
            print(f"MATCH: Type: {vt} | Number: {vn} | Date: {dt} | IsPostDated: {ipd} | Party: {party} | Amt: {amt}")
    print(f"Total matching vouchers found: {found_count}")
except Exception as e:
    print(f"Error: {e}")
