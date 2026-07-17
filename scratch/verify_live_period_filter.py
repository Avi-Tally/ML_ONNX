import sys
import os
sys.path.append(os.path.abspath('.'))

import asyncio
from datetime import datetime
from tally_client import TallyClient

async def verify():
    client = TallyClient()
    company = "Modi Chemplast Materials Pvt Ltd"
    port = 9001
    date = "29-Nov-2025"
    
    print(f"Fetching outstanding payables for '{company}' on {date}...")
    
    bills = client.fetch_bills(
        company, 
        port, 
        report_type="Payable", 
        status_filter="pending", 
        reference_date=date,
        exclude_pdc=True
    )
    
    print(f"Total pending payables fetched: {len(bills)}")
    
    ref_date = datetime.strptime(date, "%d-%b-%Y")
    period_start = datetime(2024, 4, 1)
    
    filtered_bills = []
    for b in bills:
        # Filter by BillDate >= 1-Apr-2025
        bdate_str = b.get("date")
        if not bdate_str:
            continue
        try:
            bdate = datetime.strptime(bdate_str, "%Y%m%d")
        except:
            continue
            
        if bdate < period_start:
            continue
            
        # Get due date
        due_date_str = b.get("due_date")
        if not due_date_str:
            continue
        try:
            due_date = datetime.strptime(due_date_str, "%Y%m%d")
        except:
            continue
            
        # Age is ref_date - due_date
        age = (ref_date - due_date).days
        if age > 40:
            filtered_bills.append(b)
            
    print(f"\nFiltered bills (BillDate >= 1-Apr-2025 AND Age > 40 days on 29-Nov-2025): {len(filtered_bills)}")
    
    total_val = 0.0
    for b in filtered_bills:
        total_val += b.get("normalized_payables_amount", 0.0)
        
    print(f"Grand Total Outstanding of filtered bills: Rs {total_val:,.2f}")
    
    # Check for Abhay Limited bill Ref: 1400115918
    abhay_bill = [b for b in filtered_bills if "1400115918" in str(b.get("name"))]
    if abhay_bill:
        print(f"WARNING: Abhay Limited bill 1400115918 is PRESENT: Ref={abhay_bill[0]['name']} | Bal={abhay_bill[0]['amount']}")
    else:
        print("SUCCESS: Abhay Limited bill 1400115918 is ABSENT.")

if __name__ == "__main__":
    asyncio.run(verify())
