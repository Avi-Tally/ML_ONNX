import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Let's search for collections containing "bill" or "outstanding" in Tally metadata
# We can request Tally to return a list of collections!
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Metadata</TYPE>
        <ID>Collections</ID>
    </HEADER>
    <BODY>
        <DESC>
        </DESC>
    </BODY>
</ENVELOPE>"""

res = client.execute_xml_request(port, payload)
print(f"Response Length: {len(res)}")
# Print first 2000 chars of metadata response
print(res[:2000])
