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
        <ID>AllLedgers</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="AllLedgers">
                        <TYPE>Ledger</TYPE>
                        <FETCH>Name, Parent, IsBillWiseOn</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=20)
    ledgers = re.findall(r'<LEDGER\b.*?</LEDGER>', response.text, re.DOTALL)
    print(f"Total ledgers matched: {len(ledgers)}")
    
    with open("scratch/all_ledgers.txt", "w", encoding="utf-8") as f:
        for l in ledgers:
            name_m = re.search(r'<NAME\b[^>]*>(.*?)</NAME>', l)
            parent_m = re.search(r'<PARENT\b[^>]*>(.*?)</PARENT>', l)
            bw_m = re.search(r'<ISBILLWISEON\b[^>]*>(.*?)</ISBILLWISEON>', l)
            
            name = name_m.group(1) if name_m else "N/A"
            parent = parent_m.group(1) if parent_m else "N/A"
            bw = bw_m.group(1) if bw_m else "N/A"
            f.write(f"Ledger: {name} | Parent: {parent} | IsBillWiseOn: {bw}\n")
    print("Wrote all ledgers to scratch/all_ledgers.txt")
except Exception as e:
    print(f"Error: {e}")
