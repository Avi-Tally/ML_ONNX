import xml.etree.ElementTree as ET
from datetime import datetime

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
    bills.append(current_bill)

print(f"Total bills in GUI export: {len(bills)}")

ref_date = datetime(2025, 11, 29)

# Filter for age > 40 days
filtered_bills = []
total_val = 0.0

for b in bills:
    date_str = b.get("date")
    if not date_str:
        continue
    try:
        # Date format is usually YYYYMMDD
        bdate = datetime.strptime(date_str, "%Y%m%d")
    except:
        try:
            # Try alternate format
            bdate = datetime.strptime(date_str, "%d-%b-%y")
        except:
            continue
            
    # Wait, is age calculated from bill date or due date?
    # Tally outstanding age is calculated from the DUE date!
    # Let's check if the due date is in the XML, or if we calculate from bill date + credit period.
    # In GUI export, we have BILLDUE which might contain the due date or age.
    # Let's check how the due date is stored.
    # Let's assume age is ref_date - bdate (from bill date) first, or due date if available.
    due_str = b.get("due")
    # In tally_ui_export_new.xml, BILLDUE represents the due date.
    # Let's see what is inside BILLDUE.
    due_date = bdate
    if due_str:
        try:
            due_date = datetime.strptime(due_str, "%Y%m%d")
        except:
            pass
            
    age = (ref_date - due_date).days
    if age > 40:
        filtered_bills.append(b)
        # Parse closing balance
        cl_str = b.get("cl", "0.0")
        try:
            val = float(cl_str.replace(",", "").strip())
            total_val += val
        except:
            pass

print(f"Filtered GUI bills (Age > 40 days on 29-Nov-2025): {len(filtered_bills)}")
print(f"Grand Total Outstanding of filtered GUI bills: Rs {total_val:,.2f}")

# Count GUI bills by year
gui_year_counts = {}
for b in bills:
    date_str = b.get("date")
    year = "Unknown"
    if date_str:
        try:
            bdate = datetime.strptime(date_str, "%Y%m%d")
            year = str(bdate.year)
        except:
            try:
                bdate = datetime.strptime(date_str, "%d-%b-%y")
                year = str(bdate.year)
            except:
                pass
    gui_year_counts[year] = gui_year_counts.get(year, 0) + 1

print("\nGUI Bills by Year:")
for yr, count in sorted(gui_year_counts.items()):
    print(f"  {yr}: {count} bills")

# Search for Abhay Limited
abhay = [b for b in bills if "abhay" in str(b.get("party")).lower()]
print(f"\nAbhay Limited bills in GUI export: {len(abhay)}")
for ab in abhay[:5]:
    print(ab)
