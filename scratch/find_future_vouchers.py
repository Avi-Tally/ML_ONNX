import xml.etree.ElementTree as ET
from datetime import datetime

file_path = "raw_xml_dumps/tally_ui_export_new.xml"
with open(file_path, "r", encoding="utf-16") as f:
    content = f.read()

if not content.strip().startswith("<ENVELOPE>"):
    content = f"<ROOT>{content}</ROOT>"

root = ET.fromstring(content)
envelope = root.find("ENVELOPE") or root

# Let's inspect the structure of the XML to see if there are other nodes like VOUCHER or if it's just bills.
print("Root child tags:")
child_tags = set(c.tag for c in envelope)
print(child_tags)

# If this is a bills outstandings report, it might only contain BILL nodes.
# Let's see if we can find any bill that has a PDC tag or date > 29-Nov-2025.
bills_with_future_date = []
for child in envelope:
    if child.tag == "BILLFIXED":
        ref = child.findtext("BILLREF")
        bdate_str = child.findtext("BILLDATE")
        party = child.findtext("BILLPARTY")
        try:
            bdate = datetime.strptime(bdate_str, "%d-%b-%y")
            if bdate > datetime(2025, 11, 29):
                bills_with_future_date.append((party, ref, bdate_str))
        except:
            pass

print(f"Total bills with date > 29-Nov-2025 in GUI XML: {len(bills_with_future_date)}")
for b in bills_with_future_date[:10]:
    print(b)
