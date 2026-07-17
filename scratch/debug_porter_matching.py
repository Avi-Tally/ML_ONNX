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
    
    # Let's inspect Porter bills
    api_porter = [b for b in api_bills if "porter" in str(b.get("party")).lower()]
    gui_porter = [b for b in gui_bills if "porter" in str(b.get("party")).lower()]
    
    print(f"API Porter Count: {len(api_porter)}")
    print(f"GUI Porter Count: {len(gui_porter)}")
    
    if api_porter:
        print("\nFirst API Porter Bill:")
        print(f"  Name repr: {repr(api_porter[0].get('name'))}")
        print(f"  Party repr: {repr(api_porter[0].get('party'))}")
        
    if gui_porter:
        print("\nFirst GUI Porter Bill:")
        print(f"  Ref repr: {repr(gui_porter[0].get('ref'))}")
        print(f"  Party repr: {repr(gui_porter[0].get('party'))}")

if __name__ == "__main__":
    main()
