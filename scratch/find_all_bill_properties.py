import requests
import xml.etree.ElementTree as ET

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9001

# We query both 1400115918 and 8100018557 to compare all their fields!
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
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="DebugBills">
                        <TYPE>Bill</TYPE>
                        <FETCH>*</FETCH>
                        <FILTERS>TargetFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetFilter">
                        $Name = "1400115918" OR $Name = "8100018557"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=20)
    import re
    bills = re.findall(r'<BILL\b.*?</BILL>', response.text, re.DOTALL)
    print(f"Total matching bills: {len(bills)}")
    for b in bills:
        name_m = re.search(r'<NAME\b[^>]*>(.*?)</NAME>', b)
        ref = name_m.group(1) if name_m else "N/A"
        print(f"\n--- Bill: {ref} ---")
        # Extract all child tags and their values
        tags = re.findall(r'<(\w+)\b[^>]*>(.*?)</\1>', b)
        for tag, val in tags:
            val_s = val.strip()
            if val_s and val_s != "None":
                print(f"  {tag}: {val_s}")
except Exception as e:
    print(f"Error: {e}")
