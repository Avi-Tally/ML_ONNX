import requests
import xml.etree.ElementTree as ET
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
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="DebugBills">
                        <TYPE>Bill</TYPE>
                        <FETCH>Name, ClosingBalance, Parent, BillDate, BillCreditPeriod, IsAdvance, IsAgstRef</FETCH>
                        <COMPUTE>IsAdvance: $IsAdvance</COMPUTE>
                        <COMPUTE>IsAgstRef: $IsAgstRef</COMPUTE>
                        <FILTERS>TargetFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetFilter">
                        $Name = "PONO:E-10035 - 59933"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=10)
    bills = re.findall(r'<BILL\b.*?</BILL>', response.text, re.DOTALL)
    for b in bills:
        print("Aquatech Extra Bill XML:")
        tags = re.findall(r'<(\w+)\b[^>]*>(.*?)</\1>', b)
        for tag, val in tags:
            print(f"  {tag}: {val.strip()}")
except Exception as e:
    print(f"Error: {e}")
