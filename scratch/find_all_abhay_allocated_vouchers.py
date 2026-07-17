import re

with open("scratch/abhay_vouchers.xml", "r", encoding="utf-8") as f:
    content = f.read()

# Find all blocks of <VOUCHER> ... </VOUCHER>
vouchers = re.findall(r'<VOUCHER\b.*?</VOUCHER>', content, re.DOTALL)

print(f"Total Vouchers in file: {len(vouchers)}")

matching_vouchers = []
for v in vouchers:
    if "1400115918" in v:
        matching_vouchers.append(v)

print(f"Found {len(matching_vouchers)} vouchers containing '1400115918':")
for i, v in enumerate(matching_vouchers):
    # Extract voucher type, number, date
    vtype = re.search(r'<VOUCHERTYPENAME>(.*?)</VOUCHERTYPENAME>', v)
    vnum = re.search(r'<VOUCHERNUMBER>(.*?)</VOUCHERNUMBER>', v)
    vdate = re.search(r'<DATE>(.*?)</DATE>', v)
    vt = vtype.group(1) if vtype else "N/A"
    vn = vnum.group(1) if vnum else "N/A"
    vd = vdate.group(1) if vdate else "N/A"
    print(f"\nVoucher {i+1}: Type={vt} | Num={vn} | Date={vd}")
    
    # Print ledger entries that mention 1400115918 or are related
    entries = re.findall(r'<ALLLEDGERENTRIES\.LIST\b.*?</ALLLEDGERENTRIES\.LIST>', v, re.DOTALL)
    for ent in entries:
        if "1400115918" in ent:
            lname = re.search(r'<LEDGERNAME>(.*?)</LEDGERNAME>', ent)
            amt = re.search(r'<AMOUNT>(.*?)</AMOUNT>', ent)
            ln = lname.group(1) if lname else "N/A"
            am = amt.group(1) if amt else "N/A"
            print(f"  Ledger Entry: {ln} | Amt: {am}")
            
            # Print bill allocations
            bas = re.findall(r'<BILLALLOCATIONS\.LIST\b.*?</BILLALLOCATIONS\.LIST>', ent, re.DOTALL)
            for ba in bas:
                if "1400115918" in ba:
                    baname = re.search(r'<NAME>(.*?)</NAME>', ba)
                    baamt = re.search(r'<AMOUNT>(.*?)</AMOUNT>', ba)
                    batype = re.search(r'<BILLTYPE>(.*?)</BILLTYPE>', ba)
                    ban = baname.group(1) if baname else "N/A"
                    baa = baamt.group(1) if baamt else "N/A"
                    bat = batype.group(1) if batype else "N/A"
                    print(f"    Bill Allocation -> Ref: {ban} | Amt: {baa} | Type: {bat}")
