import re

with open("scratch/abhay_vouchers.xml", "r", encoding="utf-8") as f:
    lines = f.readlines()

current_voucher = None
current_ledger = None
in_bill_alloc = False
current_bill = None

vouchers_found = []

for line in lines:
    line_str = line.strip()
    
    # Check Voucher start
    v_match = re.search(r'<VOUCHER\b', line_str)
    if v_match:
        current_voucher = {"entries": []}
        continue
        
    if current_voucher is None:
        continue
        
    # Check Voucher end
    if line_str.startswith("</VOUCHER>"):
        # Process voucher
        vnum = current_voucher.get("num")
        vdate = current_voucher.get("date")
        for ent in current_voucher["entries"]:
            if ent.get("ledger") == "Abhay Limited":
                vouchers_found.append((vnum, vdate, ent))
        current_voucher = None
        continue
        
    # Voucher attributes
    num_match = re.search(r'<VOUCHERNUMBER\b[^>]*>(.*?)</VOUCHERNUMBER>', line_str)
    if num_match:
        current_voucher["num"] = num_match.group(1)
        
    date_match = re.search(r'<DATE\b[^>]*>(.*?)</DATE>', line_str)
    if date_match:
        current_voucher["date"] = date_match.group(1)
        
    # Ledger Entries
    le_start = re.search(r'<ALLLEDGERENTRIES\.LIST\b', line_str)
    if le_start:
        current_ledger = {"bills": []}
        continue
        
    if current_ledger is not None:
        if line_str.startswith("</ALLLEDGERENTRIES.LIST>"):
            current_voucher["entries"].append(current_ledger)
            current_ledger = None
            continue
            
        lname_match = re.search(r'<LEDGERNAME\b[^>]*>(.*?)</LEDGERNAME>', line_str)
        if lname_match:
            current_ledger["ledger"] = lname_match.group(1)
            
        amt_match = re.search(r'<AMOUNT\b[^>]*>(.*?)</AMOUNT>', line_str)
        if amt_match:
            current_ledger["amount"] = amt_match.group(1)
            
        # Bill Allocations
        ba_start = re.search(r'<BILLALLOCATIONS\.LIST\b', line_str)
        if ba_start:
            in_bill_alloc = True
            current_bill = {}
            continue
            
        if in_bill_alloc:
            if line_str.startswith("</BILLALLOCATIONS.LIST>"):
                current_ledger["bills"].append(current_bill)
                current_bill = None
                in_bill_alloc = False
                continue
                
            bname_match = re.search(r'<NAME\b[^>]*>(.*?)</NAME>', line_str)
            if bname_match:
                current_bill["name"] = bname_match.group(1)
                
            bamt_match = re.search(r'<AMOUNT\b[^>]*>(.*?)</AMOUNT>', line_str)
            if bamt_match:
                current_bill["amount"] = bamt_match.group(1)

print(f"Total Vouchers with Abhay Limited: {len(vouchers_found)}")
for vnum, vdate, ent in vouchers_found:
    print(f"Voucher: {vnum} | Date: {vdate} | Amt: {ent.get('amount')}")
    for b in ent["bills"]:
        print(f"  Bill Allocation -> Ref: {b.get('name')} | Amt: {b.get('amount')}")
