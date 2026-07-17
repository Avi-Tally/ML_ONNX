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
            }
        elif child.tag == "BILLCL" and "cl" not in current_bill:
            current_bill["cl"] = child.text
    if current_bill:
        bills.append(current_bill)
    return bills

def main():
    client = TallyClient()
    company = "Modi Chemplast Materials Pvt Ltd"
    port = 9001
    date = "29-Nov-2025"
    
    api_bills = client.fetch_bills(
        company, 
        port, 
        report_type="Payable", 
        status_filter="pending", 
        reference_date=date,
        exclude_pdc=True
    )
    
    gui_bills = load_gui_bills()
    
    # Create maps for comparison
    api_set = set()
    for ab in api_bills:
        ref = str(ab.get("name")).strip().lower()
        party = str(ab.get("party")).strip().lower()
        api_set.add((party, ref))
        
    missing_bills = []
    for gb in gui_bills:
        ref = str(gb.get("ref")).strip().lower()
        party = str(gb.get("party")).strip().lower()
        if (party, ref) not in api_set:
            missing_bills.append(gb)
            
    print(f"Total missing bills in API (but present in GUI): {len(missing_bills)}")
    
    # Group missing bills by party
    party_counts = {}
    for mb in missing_bills:
        party = mb.get("party")
        party_counts[party] = party_counts.get(party, 0) + 1
        
    print("\nMissing bills by Party:")
    for party, count in sorted(party_counts.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(f"  {party}: {count} bills")
        
    print("\nFirst 10 missing bills details:")
    for mb in missing_bills[:10]:
        print(f"  Party: {mb.get('party')} | Ref: {mb.get('ref')} | Bal: {mb.get('cl')}")

if __name__ == "__main__":
    main()
