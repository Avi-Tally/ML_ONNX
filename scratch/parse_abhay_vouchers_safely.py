import re
import xml.etree.ElementTree as ET

with open("scratch/abhay_vouchers.xml", "r", encoding="utf-8") as f:
    content = f.read()

# Strip namespaces like <UDF:xyz> or </UDF:xyz> to avoid unbound prefix errors
content = re.sub(r'<\/?\w+:', '<', content)
# Wait, also replace any attributes like UDF:xyz="abc"
content = re.sub(r'\s\w+:\w+=', ' attr=', content)

root = ET.fromstring(content)
vouchers = root.findall(".//VOUCHER")
print(f"Total Vouchers parsed: {len(vouchers)}")

for v in vouchers:
    vnum = v.findtext("VOUCHERNUMBER")
    vdate = v.findtext("DATE")
    for le in v.findall(".//ALLLEDGERENTRIES.LIST"):
        lname = le.findtext("LEDGERNAME")
        if lname == "Abhay Limited":
            amt = le.findtext("AMOUNT")
            print(f"Voucher: {vnum} | Date: {vdate} | Ledger: {lname} | Amt: {amt}")
            for ba in le.findall(".//BILLALLOCATIONS.LIST"):
                bname = ba.findtext("NAME")
                bamt = ba.findtext("AMOUNT")
                print(f"    Bill Allocation -> Ref: {bname} | Amt: {bamt}")
