import xml.etree.ElementTree as ET

tree = ET.parse("scratch/abhay_vouchers.xml")
root = tree.getroot()

vouchers = root.findall(".//VOUCHER")
print(f"Total Vouchers: {len(vouchers)}")

for v in vouchers[:10]:
    vnum = v.findtext("VOUCHERNUMBER")
    vdate = v.findtext("DATE")
    print(f"Voucher: {vnum} | Date: {vdate}")
    # Print ledger entries and any bill allocations
    for le in v.findall(".//ALLLEDGERENTRIES.LIST"):
        lname = le.findtext("LEDGERNAME")
        amt = le.findtext("AMOUNT")
        print(f"  Ledger: {lname} | Amt: {amt}")
        for ba in le.findall(".//BILLALLOCATIONS.LIST"):
            bname = ba.findtext("NAME")
            bamt = ba.findtext("AMOUNT")
            print(f"    Bill Allocation -> Ref: {bname} | Amt: {bamt}")
