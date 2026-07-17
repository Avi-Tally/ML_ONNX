import xml.etree.ElementTree as ET

file_path = "raw_xml_dumps/tally_ui_export_new.xml"
with open(file_path, "r", encoding="utf-16") as f:
    content = f.read()

if not content.strip().startswith("<ENVELOPE>"):
    content = f"<ROOT>{content}</ROOT>"

root = ET.fromstring(content)
envelope = root.find("ENVELOPE") or root

bills_with_pdc = []
current_bill = {}
for child in envelope:
    if child.tag == "BILLFIXED":
        if current_bill:
            bills_with_pdc.append(current_bill)
        current_bill = {
            "ref": child.findtext("BILLREF"),
            "party": child.findtext("BILLPARTY"),
            "date": child.findtext("BILLDATE"),
            "cl": child.findtext("BILLCL"),
        }
    elif child.tag == "BILLPDC":
        current_bill["pdc"] = child.text
if current_bill:
    bills_with_pdc.append(current_bill)

pdc_non_empty = [b for b in bills_with_pdc if b.get("pdc") and b.get("pdc").strip()]
print(f"Total bills with non-empty BILLPDC: {len(pdc_non_empty)}")
for b in pdc_non_empty[:10]:
    print(b)
