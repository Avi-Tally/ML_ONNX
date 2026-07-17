import sys
import os
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

def mock_parse_offline_xml(file_path):
    print(f"\n=== Offline Verification of {file_path} ===")
    
    # Read XML
    with open(file_path, "r", encoding="utf-16") as f:
        xml_content = f.read()
        
    if not xml_content.strip().startswith("<ENVELOPE>"):
        xml_content = f"<ROOT>{xml_content}</ROOT>"
        
    root = ET.fromstring(xml_content)
    
    # TallyClient instance to use helper methods
    client = TallyClient()
    
    # In tally_client.py, we parse <BILL> elements.
    # In the UI export, the bills are stored under BILLFIXED, BILLCL, BILLPDC etc.
    # Let's map the UI export structure into <BILL> elements to test the parser!
    envelope = root.find("ENVELOPE") or root
    
    current_bill = {}
    bills_xml_elements = []
    
    # Reconstruct <BILL> elements
    for child in envelope:
        if child.tag == "BILLFIXED":
            if current_bill:
                bills_xml_elements.append(current_bill)
            current_bill = {
                "ref": child.findtext("BILLREF"),
                "date": child.findtext("BILLDATE"),
                "party": child.findtext("BILLPARTY"),
            }
        elif child.tag == "BILLCL" and "cl" not in current_bill:
            current_bill["cl"] = child.text
        elif child.tag == "BILLPDC":
            current_bill["pdc"] = child.text
        elif child.tag == "BILLFINAL":
            current_bill["final"] = child.text
        elif child.tag == "BILLDUE":
            current_bill["due"] = child.text
    if current_bill:
        bills_xml_elements.append(current_bill)
        
    print(f"Total bills reconstructed from XML: {len(bills_xml_elements)}")
    
    # Let's check which ones should be filtered
    # For a real Tally client, we do the check on ISBILLWISEON.
    # In the XML file, does it have ISBILLWISEON?
    # No, the XML export from Tally GUI outstanding report does not contain ISBILLWISEON tag.
    # But wait! We can verify that our tally_client.py parsing code (with ISBILLWISEON check)
    # works correctly when ISBILLWISEON is present or absent!
    # Let's verify if Abhay Limited's bill Ref: 1400115918 is in the list
    abhay_bill = None
    for b in bills_xml_elements:
        if str(b.get("ref")).strip() == "1400115918":
            abhay_bill = b
            break
            
    if abhay_bill:
        print(f"Abhay Limited target bill 1400115918 is present in GUI export XML: Ref={abhay_bill['ref']} | Bal={abhay_bill['cl']}")
    else:
        print("Abhay Limited target bill 1400115918 is NOT present in GUI export XML!")

mock_parse_offline_xml("raw_xml_dumps/tally_ui_export.xml")
mock_parse_offline_xml("raw_xml_dumps/tally_ui_export_new.xml")
