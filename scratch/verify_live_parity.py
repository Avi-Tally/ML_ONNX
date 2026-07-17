import sys
import os
sys.path.append(os.path.abspath('.'))

import asyncio
from tally_client import TallyClient

async def verify():
    client = TallyClient()
    company = "Modi Chemplast Materials Pvt Ltd"
    port = 9001
    date = "29-Nov-2025"
    
    print(f"Fetching outstanding payables for '{company}' on {date}...")
    
    # We query payables on 29-Nov-2025
    # The default setting of exclude_pdc=True should be applied
    bills = client.fetch_bills(
        company, 
        port, 
        report_type="Payable", 
        status_filter="pending", 
        reference_date=date,
        exclude_pdc=True
    )
    
    print(f"\nTotal bills returned by API: {len(bills)}")
    
    # Calculate total outstanding payables amount
    total_val = 0.0
    for b in bills:
        # For payables, the amount field in tally_client represents the pre-normalized balance
        # positive values are normal payables, negative are advances
        # Wait, let's verify if we need to sum normalized_payables_amount or amount
        # Let's check both
        total_val += b.get("normalized_payables_amount", 0.0)
        
    print(f"Grand Total Outstanding (normalized_payables_amount): Rs {total_val:,.2f}")
    
    # Let's check for the Abhay Limited bill Ref: 1400115918
    abhay_bill = [b for b in bills if "1400115918" in str(b.get("name"))]
    if abhay_bill:
        print(f"WARNING: Abhay Limited bill 1400115918 IS PRESENT: Ref={abhay_bill[0]['name']} | Bal={abhay_bill[0]['amount']}")
    else:
        print("SUCCESS: Abhay Limited bill 1400115918 is ABSENT (filtered out due to bill-by-bill disabled).")
        
    # Let's check for the 5 target bills of Thermax and Aquatech System
    target_refs = ["MODI/25-26/231", "MODI/25-26/440", "MODI/25-26/439", "MODI/25-26/438", "MODI/25-26/426"]
    found_targets = []
    for b in bills:
        ref = b.get("name")
        if ref in target_refs:
            found_targets.append(f"  Ref: {ref} | Party: {b.get('party')} | Bal: {b.get('amount')}")
            
    print(f"\nTarget post-dated bills found ({len(found_targets)}/5):")
    for ft in found_targets:
        print(ft)
        
    if len(found_targets) == 5:
        print("SUCCESS: All 5 post-dated bills are correctly present as outstanding.")
    else:
        print("WARNING: Some post-dated bills are missing!")

if __name__ == "__main__":
    asyncio.run(verify())
