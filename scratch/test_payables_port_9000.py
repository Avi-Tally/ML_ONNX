import sys
import os
sys.path.append(os.path.abspath('.'))
import asyncio
from tally_client import TallyClient

async def test():
    client = TallyClient()
    company = "Modi Chemplast Materials Pvt Ltd"
    port = 9000
    date = "29-Nov-2025"
    
    print(f"Fetching bills for {company} on {date}...")
    bills = client.fetch_bills(company, port, reference_date=date)
    print(f"Total bills retrieved: {len(bills)}")
    
    # Filter for Thermax and Aquatech System
    for b in bills:
        party = b.get("party", "")
        if "thermax" in party.lower() or "aquatech" in party.lower():
            print(f"Party: {party} | Ref: {b.get('ref')} | Date: {b.get('date')} | Bal: {b.get('amount')} | Cleared: {b.get('cleared_on')}")

if __name__ == "__main__":
    asyncio.run(test())
