import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

group_map = client.get_group_hierarchy_map(company_name, port)

# Print hierarchy path for Sundry Debtors and Sundry Creditors
def print_path(group_name):
    path = [group_name]
    curr = group_name
    while curr in group_map and group_map[curr]:
        curr = group_map[curr]
        path.append(curr)
    print(f"Path for '{group_name}': {' -> '.join(path)}")

print_path("Sundry Debtors")
print_path("Sundry Creditors")

# Check parents of other key parties
parties = ["Thermax Ltd", "Effwa Infra & Research Limited", "SINAI ENGINEERING", "Reliance Industries Limited (Guj)", "Reliance Industries Limited", "RELIANCE NEW SOLAR ENERGY LIMITED"]
for p in parties:
    # Let's get parent of these from the XML LedgerList
    import xml.etree.ElementTree as ET
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
                            <FILTER>PartyFilter</FILTER>
                            <FETCH>Name, Parent</FETCH>
                        </COLLECTION>
                        <SYSTEM TYPE="Formula" NAME="PartyFilter">$$IsNameEqual:Name:"{p}"</SYSTEM>
                    </TDLMESSAGE>
                </TDL>
            </DESC>
        </BODY>
    </ENVELOPE>"""
    try:
        res = client.execute_xml_request(port, payload)
        root = ET.fromstring(res)
        l = root.find(".//LEDGER")
        if l is not None:
            print(f"Party: {p}, Parent Group: {l.findtext('PARENT')}")
        else:
            print(f"Party: {p} not found in LedgerList")
    except Exception as e:
        print(f"Error for {p}: {e}")
