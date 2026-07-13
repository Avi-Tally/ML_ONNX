import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Let's fetch all groups in Tally and print their names and parent groups
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>GroupList</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="GroupList">
                        <TYPE>Group</TYPE>
                        <FETCH>Name, Parent</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

res = client.execute_xml_request(port, payload)
root = ET.fromstring(res)
groups = root.findall(".//GROUP")

group_parents = {}
for g in groups:
    name = g.findtext("NAME") or g.attrib.get("NAME", "")
    parent = g.findtext("PARENT") or ""
    if name:
        group_parents[name.strip().lower()] = parent.strip().lower()

# Print hierarchy path function
def get_hierarchy_path(group_name):
    path = []
    curr = group_name.strip().lower()
    while curr:
        path.append(curr)
        curr = group_parents.get(curr)
    return " -> ".join(path)

print("Group Hierarchy Paths:")
for name in sorted(group_parents.keys()):
    print(f" - {name}: {get_hierarchy_path(name)}")
