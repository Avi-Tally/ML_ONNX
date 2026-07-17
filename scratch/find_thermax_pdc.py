import xml.etree.ElementTree as ET

def find_bills(file_path):
    print(f"\n--- Searching {file_path} ---")
    try:
        # Read file as UTF-16
        with open(file_path, "r", encoding="utf-16") as f:
            xml_content = f.read()
        
        # Parse XML
        # Wrap in a root tag if it doesn't have a single root
        if not xml_content.strip().startswith("<ENVELOPE>"):
            xml_content = f"<ROOT>{xml_content}</ROOT>"
            
        root = ET.fromstring(xml_content)
        
        # In tally exports, the structure might have multiple tags.
        # Let's search for BILLPARTY containing Thermax or Aquatech
        bills = []
        # Find all BILLFIXED or elements
        # Since it's a flat list of BILLFIXED, BILLCL, BILLPDC etc. under ENVELOPE
        # We can iterate through the children of ENVELOPE
        envelope = root
        if root.tag != "ENVELOPE":
            envelope = root.find("ENVELOPE")
            
        if envelope is None:
            envelope = root
            
        current_bill = {}
        for child in envelope:
            if child.tag == "BILLFIXED":
                if current_bill:
                    bills.append(current_bill)
                    current_bill = {}
                current_bill["date"] = child.findtext("BILLDATE")
                current_bill["ref"] = child.findtext("BILLREF")
                current_bill["party"] = child.findtext("BILLPARTY")
            elif child.tag == "BILLCL" and "cl" not in current_bill:
                current_bill["cl"] = child.text
            elif child.tag == "BILLPDC":
                current_bill["pdc"] = child.text
            elif child.tag == "BILLFINAL":
                current_bill["final"] = child.text
            elif child.tag == "BILLDUE":
                current_bill["due"] = child.text
        if current_bill:
            bills.append(current_bill)
            
        # Filter for Thermax or Aquatech
        for b in bills:
            party = b.get("party", "")
            if "thermax" in party.lower() or "aquatech" in party.lower():
                print(f"Party: {party} | Ref: {b.get('ref')} | Date: {b.get('date')} | Due: {b.get('due')} | Closing: {b.get('cl')} | PDC: {b.get('pdc')} | Final: {b.get('final')}")
                
    except Exception as e:
        print(f"Error: {e}")

find_bills("raw_xml_dumps/tally_ui_export.xml")
find_bills("raw_xml_dumps/tally_ui_export_new.xml")
