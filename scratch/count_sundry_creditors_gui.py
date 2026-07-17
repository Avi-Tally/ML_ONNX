import sys
import os
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

def load_gui_bills():
    file_path = "raw_xml_dumps/tally_ui_export_new.xml"
    with open(file_path, "r", encoding="utf-16") as f:
        content = f.read()
    if not content.strip().startswith("<ENVELOPE>"):
        content = f"<ROOT>{content}</ROOT>"
    root = ET.fromstring(content)
    envelope = root.find("ENVELOPE") or root
    bills = []
    current_bill = {}
    for child in envelope:
        if child.tag == "BILLFIXED":
            if current_bill:
                bills.append(current_bill)
            current_bill = {
                "ref": child.findtext("BILLREF"),
                "party": child.findtext("BILLPARTY"),
                "date": child.findtext("BILLDATE"),
            }
        elif child.tag == "BILLCL" and "cl" not in current_bill:
            current_bill["cl"] = child.text
    if current_bill:
        bills.append(current_bill)
    return bills

def main():
    client = TallyClient()
    company = "Modi Chemplast Materials Pvt Ltd"
    port = 9000
    
    # Fetch group map from Port 9000
    group_map = client.get_group_hierarchy_map(company, port)
    
    # Fetch all ledgers to get their parent groups
    # Wait, we can fetch all ledgers and build a map of ledger -> parent group
    print("Fetching all ledgers...")
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
                    <SVCURRENTCOMPANY>{company}</SVCURRENTCOMPANY>
                </STATICVARIABLES>
                <TDL>
                    <TDLMESSAGE>
                        <COLLECTION NAME="LedgerList">
                            <TYPE>Ledger</TYPE>
                            <FETCH>Name, Parent</FETCH>
                        </COLLECTION>
                    </TDLMESSAGE>
                </TDL>
            </DESC>
        </BODY>
    </ENVELOPE>"""
    
    import requests
    import re
    res = requests.post(f"http://localhost:{port}", data=payload, headers={'Content-Type': 'text/xml'}, timeout=20)
    ledgers = re.findall(r'<LEDGER\b.*?</LEDGER>', res.text, re.DOTALL)
    ledger_groups = {}
    for l in ledgers:
        name_m = re.search(r'<NAME\b[^>]*>(.*?)</NAME>', l)
        parent_m = re.search(r'<PARENT\b[^>]*>(.*?)</PARENT>', l)
        if name_m:
            name = name_m.group(1).strip()
            parent = parent_m.group(1).strip() if parent_m else ""
            ledger_groups[name.lower()] = parent.lower()
            
    gui_bills = load_gui_bills()
    print(f"Total GUI bills: {len(gui_bills)}")
    
    # Filter GUI bills to only include those in Sundry Creditors lineage
    filtered_gui = []
    excluded_parties = set()
    for gb in gui_bills:
        party = gb.get("party")
        pg_lower = ledger_groups.get(party.lower(), "")
        is_creditor = (
            client.is_group_under(pg_lower, "sundry creditors", group_map) or
            client.is_group_under(pg_lower, "trade payables", group_map) or
            any(w in pg_lower for w in ["creditor", "payable", "supplier", "vendor"]) or
            any(w in party.lower() for w in ["creditor", "supplier", "vendor"])
        )
        if is_creditor:
            filtered_gui.append(gb)
        else:
            excluded_parties.add((party, pg_lower))
            
    print(f"Filtered GUI bills (Sundry Creditors lineage): {len(filtered_gui)}")
    print(f"Excluded parties count: {len(excluded_parties)}")
    print("Excluded parties:")
    for p, g in sorted(excluded_parties)[:10]:
        print(f"  - {p} (Group: {g})")

if __name__ == "__main__":
    main()
