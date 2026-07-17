import sys
import os
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient
from datetime import datetime

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
            
    print(f"Total extra bills: {len(extra_bills)}")
    
    # Count by year
    year_counts = {}
    for eb in extra_bills:
        date_str = eb.get("date")
        year = "Unknown"
        if date_str and len(date_str) >= 4:
            year = date_str[:4]
        year_counts[year] = year_counts.get(year, 0) + 1
        
    print("Extra bills by Year:")
    for yr, count in sorted(year_counts.items()):
        print(f"  {yr}: {count} bills")
        
    # Print details of any 2025 extra bills
    eb_2025 = [eb for eb in extra_bills if eb.get("date", "").startswith("2025")]
    print(f"\nTotal 2025 extra bills: {len(eb_2025)}")
    for eb in eb_2025[:10]:
        print(f"  Party: {eb.get('party')} | Ref: {eb.get('name')} | Date: {eb.get('date')} | Bal: {eb.get('amount')}")

if __name__ == "__main__":
    main()
