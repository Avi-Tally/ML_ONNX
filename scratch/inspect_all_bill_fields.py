import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# We will fetch raw XML for bills of RELIANCE NEW SOLAR ENERGY LIMITED
# and V TRANS (INDIA) LTD. and print the exact XML string of the bills!
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>CustomBillCollection</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="CustomBillCollection">
                        <TYPE>Bill</TYPE>
                        <FETCH>*</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

res = client.execute_xml_request(port, payload)

# Let's find the XML substring for the target bills
import re
target_bills = ["MODI/23-24/2681", "11459588"]
for tb in target_bills:
    pattern = rf"<BILL>.*?<NAME>{re.escape(tb)}</NAME>.*?</BILL>"
    match = re.search(pattern, res, re.DOTALL)
    if match:
        print(f"\nExact XML for bill {tb}:")
        print(match.group(0))
    else:
        print(f"\nCould not find XML for bill {tb}")
