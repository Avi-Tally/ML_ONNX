import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

try:
    print(f"Fetching all raw bills for '{company}' from Port {port}...")
    bills = client.fetch_bills(company, port, "All")
    print(f"Total raw bills fetched: {len(bills)}")
    
    # Sort bills by date descending to see recent ones
    bills_sorted = sorted(bills, key=lambda x: x.get("date", ""), reverse=True)
    
    print("\nSample of 30 most recent bills fetched from Tally:")
    print(f"{'Date':<10} | {'Due Date':<10} | {'Party':<35} | {'Bill Name':<20} | {'Amount':<15} | {'Parent Group':<20}")
    print("-" * 120)
    for b in bills_sorted[:40]:
        print(f"{b.get('date',''):<10} | {b.get('due_date',''):<10} | {b.get('party',''):<35} | {b.get('name',''):<20} | {b.get('amount',''):<15} | {b.get('parent_group',''):<20}")
except Exception as e:
    print("Error:", e)
