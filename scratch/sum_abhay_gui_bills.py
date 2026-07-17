import xml.etree.ElementTree as ET

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

abhay_bills = [b for b in bills if b.get("party") == "Abhay Limited"]
total_cl = 0.0
for b in abhay_bills:
    try:
        val = float(b.get("cl", "0.0").replace(",", "").strip())
        total_cl += val
    except:
        pass

print(f"Total Abhay Limited bills in GUI export: {len(abhay_bills)}")
print(f"Sum of Abhay Limited bills in GUI export: Rs {total_cl:,.2f}")
