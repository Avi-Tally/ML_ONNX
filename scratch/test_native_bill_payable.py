import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import requests
import xml.etree.ElementTree as ET
import re

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>TestPayables</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="TestPayables">
                        <TYPE>Bill Payable</TYPE>
                        <FETCH>Name, BillDate, BillCreditPeriod, ClosingBalance, OpeningBalance, Parent, ClearedOn</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

try:
    response = requests.post(f"http://localhost:{port}", data=payload, headers={'Content-Type': 'text/xml'}, timeout=30)
    print("Status:", response.status_code)
    # Sanitize XML
    text = response.text
    text = re.sub(r'&(?!(amp|lt|gt|quot|apos|#);)', '&amp;', text)
    root = ET.fromstring(text)
    bills = root.findall(".//BILL")
    print(f"Total payables bills returned: {len(bills)}")
    
    total_val = 0.0
    for b in bills[:10]:
        name = b.findtext("NAME")
        party = b.findtext("PARENT")
        amt = b.findtext("CLOSINGBALANCE")
        print(f"  - {party} : {name} = {amt}")
        
    for b in bills:
        try:
            total_val += float(b.findtext("CLOSINGBALANCE", "0"))
        except:
            pass
    print(f"Sum of ClosingBalance: ₹ {total_val:,.2f}")
except Exception as e:
    print("Error:", e)
