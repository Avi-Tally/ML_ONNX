import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Let's fetch a list of ledgers with their opening balances and parent groups
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>LedgerList</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="LedgerList">
                        <TYPE>Ledger</TYPE>
                        <FETCH>Name, Parent, OpeningBalance</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

res = client.execute_xml_request(port, payload)
root = ET.fromstring(res)
ledgers = root.findall(".//LEDGER")

print("Sample Sundry Creditors Ledgers:")
c_count = 0
for l in ledgers:
    name = l.findtext("NAME") or l.attrib.get("NAME", "")
    parent = l.findtext("PARENT") or ""
    op = l.findtext("OPENINGBALANCE") or "0"
    if "creditor" in parent.lower():
        print(f" - Ledger: {name}, Parent: {parent}, OpeningBalance: {op}")
        c_count += 1
        if c_count >= 10:
            break
            
print("\nSample Sundry Debtors Ledgers:")
d_count = 0
for l in ledgers:
    name = l.findtext("NAME") or l.attrib.get("NAME", "")
    parent = l.findtext("PARENT") or ""
    op = l.findtext("OPENINGBALANCE") or "0"
    if "debtor" in parent.lower():
        print(f" - Ledger: {name}, Parent: {parent}, OpeningBalance: {op}")
        d_count += 1
        if d_count >= 10:
            break
