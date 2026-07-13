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
    print("Root Tag:", root.tag)
    # Find all GROUP elements using different casing/paths
    groups = root.findall(".//GROUP")
    print("GROUP count:", len(groups))
    if len(groups) == 0:
        # Print children of root and DATA
        print("Root children:", [c.tag for c in root])
        data_elem = root.find("BODY/DATA")
        if data_elem is not None:
            print("DATA children:", [c.tag for c in data_elem[:10]])
            
    group_parents = {}
    for g in groups:
        name = g.attrib.get("NAME", "").strip().lower()
        parent = g.findtext("PARENT", "").strip().lower()
        if name:
            group_parents[name] = parent
            
    print(f"Total groups fetched: {len(group_parents)}")
    
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
        
    print("Is 'sundry creditors' a grouping of 'sundry creditors'?", belongs_to_group("sundry creditors", "sundry creditors"))
    
    bills = client.fetch_bills(company_name, port, "All")
    print(f"Total bills fetched: {len(bills)}")
    
    payables_count = 0
    receivables_count = 0
    other_count = 0
    for b in bills:
        pg = b.get("parent_group", "")
        if belongs_to_group(pg, "sundry creditors"):
            payables_count += 1
        elif belongs_to_group(pg, "sundry debtors"):
            receivables_count += 1
        else:
            other_count += 1
            
    print(f"Payables: {payables_count}, Receivables: {receivables_count}, Others: {other_count}")
except Exception as e:
    print("Error:", e)
