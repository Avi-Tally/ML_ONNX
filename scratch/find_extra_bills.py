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
    
    print("Fetching API bills...")
    api_bills = client.fetch_bills(
        company, 
        port, 
        report_type="Payable", 
        status_filter="pending", 
        reference_date=date,
        exclude_pdc=True
    )
    
    gui_bills = load_gui_bills()
    
    print(f"API count: {len(api_bills)}")
    print(f"GUI count: {len(gui_bills)}")
    
    # Create maps for comparison
    # Match by party name and bill reference (case-insensitive)
    gui_set = set()
    for gb in gui_bills:
        ref = str(gb.get("ref")).strip().lower()
        party = str(gb.get("party")).strip().lower()
        gui_set.add((party, ref))
        
    extra_bills = []
    for ab in api_bills:
        ref = str(ab.get("name")).strip().lower()
        party = str(ab.get("party")).strip().lower()
        if (party, ref) not in gui_set:
            extra_bills.append(ab)
            
    print(f"\nTotal extra bills in API: {len(extra_bills)}")
    
    # Let's group extra bills by party and print summary
    party_counts = {}
    for eb in extra_bills:
        party = eb.get("party")
        party_counts[party] = party_counts.get(party, 0) + 1
        
    print("\nExtra bills by Party:")
    for party, count in sorted(party_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {party}: {count} bills")
        
    print("\nFirst 10 extra bills details:")
    for eb in extra_bills[:10]:
        print(f"  Party: {eb.get('party')} | Ref: {eb.get('name')} | Date: {eb.get('date')} | Bal: {eb.get('amount')}")

if __name__ == "__main__":
    main()
