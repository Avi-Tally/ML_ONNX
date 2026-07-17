import re

daybook_path = "raw_xml_dumps/daybook_raw.xml"
print(f"Text searching {daybook_path}...")

with open(daybook_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Let's find all <VOUCHER> ... </VOUCHER> blocks
voucher_blocks = re.findall(r"<VOUCHER\b.*?</VOUCHER>", content, re.DOTALL)
print(f"Total voucher blocks found: {len(voucher_blocks)}")

count = 0
for v in voucher_blocks:
    # Check date
    date_match = re.search(r"<DATE[^>]*>(20251126)</DATE>", v)
    if date_match:
        count += 1
        vnum = re.search(r"<VOUCHERNUMBER[^>]*>(.*?)</VOUCHERNUMBER>", v)
        vtype = re.search(r"<VOUCHERTYPENAME[^>]*>(.*?)</VOUCHERTYPENAME>", v)
        is_pdc = re.search(r"<ISPOSTDATED[^>]*>(.*?)</ISPOSTDATED>", v)
        is_opt = re.search(r"<ISOPTIONAL[^>]*>(.*?)</ISOPTIONAL>", v)
        
        vnum_str = vnum.group(1) if vnum else "None"
        vtype_str = vtype.group(1) if vtype else "None"
        is_pdc_str = is_pdc.group(1) if is_pdc else "None"
        is_opt_str = is_opt.group(1) if is_opt else "None"
        
        print(f"Date: 20251126 | Type: {vtype_str} | Num: {vnum_str} | Post-Dated: {is_pdc_str} | Optional: {is_opt_str}")
        
        # Let's print all ledger entries and their amounts and bill allocations!
        ledger_entries = re.findall(r"<ALLLEDGERENTRIES.LIST\b.*?</ALLLEDGERENTRIES.LIST>", v, re.DOTALL)
        for le in ledger_entries:
            lname = re.search(r"<LEDGERNAME[^>]*>(.*?)</LEDGERNAME>", le)
            amt = re.search(r"<AMOUNT[^>]*>(.*?)</AMOUNT>", le)
            lname_str = lname.group(1) if lname else "None"
            amt_str = amt.group(1) if amt else "None"
            print(f"    Ledger: {lname_str} | Amt: {amt_str}")
            
            # Print bill allocations
            bill_allocs = re.findall(r"<BILLALLOCATIONS.LIST\b.*?</BILLALLOCATIONS.LIST>", le, re.DOTALL)
            for ba in bill_allocs:
                baname = re.search(r"<NAME[^>]*>(.*?)</NAME>", ba)
                baamt = re.search(r"<AMOUNT[^>]*>(.*?)</AMOUNT>", ba)
                baname_str = baname.group(1) if baname else "None"
                baamt_str = baamt.group(1) if baamt else "None"
                print(f"        Bill: {baname_str} | Alloc Amt: {baamt_str}")
                
print(f"Found {count} vouchers on 26-Nov-2025.")
