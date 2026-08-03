"""Isolated test: only test fetch_ledger_summary + fetch_bills per-party."""
import sys, time
sys.path.insert(0, '.')
print("Importing tally_client...", flush=True)
from tally_client import TallyClient

print("Creating client...", flush=True)
client = TallyClient()
print(f"Routing: {list(client.routing_table.keys())}", flush=True)

company = 'Bella Casa Data for User Activity'
port = 9000

# Step 1: Ledger summary
print("\n--- STEP 1: Ledger Summary ---", flush=True)
t0 = time.time()
summaries = client.fetch_ledger_summary(company, port, group_filter="Payable")
print(f"Got {len(summaries)} payable ledgers in {time.time()-t0:.2f}s", flush=True)

# Step 2: Fetch bills for top 3 parties only
top3 = sorted(summaries, key=lambda x: x['abs_balance'], reverse=True)[:3]
print(f"\n--- STEP 2: Bills for Top 3 ---", flush=True)
for ledger in top3:
    t1 = time.time()
    bills = client.fetch_bills(company, port, "Payable", ledger_filter=ledger['name'])
    party_bills = [b for b in bills if b['party'].lower() == ledger['name'].lower()]
    print(f"  {ledger['name']}: {len(party_bills)} bills in {time.time()-t1:.2f}s", flush=True)

print("\nDONE", flush=True)
