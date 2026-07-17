import requests
import re

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9001

payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>DebugBills</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
                <SVCURRENTDATE>20251129</SVCURRENTDATE>
                <SVEXCLUDEPOSTDATED>Yes</SVEXCLUDEPOSTDATED>
                <SVEXCLUDEOPTIONAL>Yes</SVEXCLUDEOPTIONAL>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="DebugBills">
                        <TYPE>Bill</TYPE>
                        <FETCH>Name, ClosingBalance, Parent, BillDate</FETCH>
                        <FILTERS>TargetFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetFilter">
                        $Name = "MODI/25-26/231" OR $Name = "MODI/25-26/440" OR $Name = "MODI/25-26/439" OR $Name = "MODI/25-26/438" OR $Name = "MODI/25-26/426"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=20)
    bills = re.findall(r'<BILL\b.*?</BILL>', response.text, re.DOTALL)
    print(f"Total matching bills for Thermax & Aquatech in DB WITH PDC VARS: {len(bills)}")
    for b in bills:
        name_m = re.search(r'<NAME\b[^>]*>(.*?)</NAME>', b)
        parent_m = re.search(r'<PARENT\b[^>]*>(.*?)</PARENT>', b)
        cl_m = re.search(r'<CLOSINGBALANCE\b[^>]*>(.*?)</CLOSINGBALANCE>', b)
        ref = name_m.group(1) if name_m else "N/A"
        party = parent_m.group(1) if parent_m else "N/A"
        cl = cl_m.group(1) if cl_m else "0.0"
        
        # Check if it is one of the 5 post-dated bills
        if any(tr in ref for tr in ["231", "440", "439", "438", "426"]):
            print(f"FOUND TARGET -> Party: {party} | Ref: {ref} | Bal: {cl}")
except Exception as e:
    print(f"Error: {e}")
