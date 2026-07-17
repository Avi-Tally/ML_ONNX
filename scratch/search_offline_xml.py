import xml.etree.ElementTree as ET

def search_xml(file_path):
    print(f"\n=== Searching {file_path} ===")
    with open(file_path, "r", encoding="utf-16") as f:
        xml_content = f.read()
    
    if not xml_content.strip().startswith("<ENVELOPE>"):
        xml_content = f"<ROOT>{xml_content}</ROOT>"
        
    root = ET.fromstring(xml_content)
    
    # We want to find any BILLFIXED block
    # Let's search by iterate
    envelope = root.find("ENVELOPE") or root
    
    current_bill = {}
    all_bills = []
    for child in envelope:
        if child.tag == "BILLFIXED":
            if current_bill:
                all_bills.append(current_bill)
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
        all_bills.append(current_bill)
        
    print(f"Total bills found in XML: {len(all_bills)}")
    
    # Let's count how many match Thermax or Aquatech
    count = 0
    for b in all_bills:
        party = b.get("party", "") or ""
        if "thermax" in party.lower() or "aquatech" in party.lower():
            count += 1
            ref = b.get("ref")
            cl = b.get("cl")
            pdc = b.get("pdc")
            final = b.get("final")
            # If ref is MODI/25-26/231 or 440 or 439 or 438 or 426
            if any(k in str(ref) for k in ["231", "440", "439", "438", "426"]):
                print(f"  MATCH TARGET: Party: {party} | Ref: {ref} | Bal: {cl} | PDC: {pdc} | Final: {final}")
            else:
                # print a summary
                pass
    print(f"Total Thermax/Aquatech bills: {count}")

search_xml("raw_xml_dumps/tally_ui_export.xml")
search_xml("raw_xml_dumps/tally_ui_export_new.xml")
