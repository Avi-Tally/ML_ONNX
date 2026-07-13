import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
import xml.etree.ElementTree as ET

company_name = "Bella Casa Data for User Activity"
port = 9001
client = TallyClient()

# Fetch Group Hierarchy
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>GroupParents</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="GroupParents">
                        <TYPE>Group</TYPE>
                        <FETCH>Name, Parent</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

try:
    response_xml = client.execute_xml_request(port, payload)
    root = ET.fromstring(response_xml)
    group_parents = {}
    for g in root.findall(".//GROUP"):
        name = g.attrib.get("NAME", "").strip().lower()
        parent = g.findtext("PARENT", "").strip().lower()
        if name:
            group_parents[name] = parent
            
    def belongs_to_group(group_name, target_group):
        curr = group_name.lower().strip()
        target = target_group.lower().strip()
        visited = set()
        while curr and curr not in visited:
            if curr == target:
                return True
            visited.add(curr)
            curr = group_parents.get(curr, "")
        return False
        
    bills = client.fetch_bills(company_name, port, "All")
    print(f"Total bills: {len(bills)}")
    
    unique_parents = {}
    for b in bills:
        pg = b.get("parent_group", "").strip()
        unique_parents[pg] = unique_parents.get(pg, 0) + 1
        
    print("Unique Parent Groups and their bill counts:")
    for pg, count in sorted(unique_parents.items(), key=lambda x: x[1], reverse=True):
        is_creditor = belongs_to_group(pg, "sundry creditors")
        is_debtor = belongs_to_group(pg, "sundry debtors")
        print(f"  - '{pg}' : {count} bills (belongs to Creditors: {is_creditor}, Debtors: {is_debtor})")
        
except Exception as e:
    print("Error:", e)
