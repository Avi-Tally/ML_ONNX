import sys, time
sys.path.insert(0, '.')
from tally_client import TallyClient

client = TallyClient()
print(f"Routing table: {list(client.routing_table.keys())}")

# Test 1: Fetch all trade ledgers
t0 = time.time()
ledgers = client.fetch_ledger_summary('Bella Casa Data for User Activity', 9000)
t1 = time.time()
print(f"\n--- ALL TRADE LEDGERS ---")
print(f"Count: {len(ledgers)}, Time: {t1-t0:.2f}s")

debtors = [l for l in ledgers if l['is_debtor']]
creditors = [l for l in ledgers if l['is_creditor']]
print(f"Debtors: {len(debtors)}, Creditors: {len(creditors)}")

# Top 5 by abs_balance
top5 = sorted(ledgers, key=lambda x: x['abs_balance'], reverse=True)[:5]
print(f"\nTop 5 outstanding:")
for i, l in enumerate(top5):
    direction = "Payable" if l['is_payable'] else "Receivable"
    print(f"  {i+1}. {l['name']}: Rs {l['abs_balance']:,.2f} ({direction}, Group: {l['parent_group']})")

# Test 2: Fetch only Payable ledgers
t0 = time.time()
payable_ledgers = client.fetch_ledger_summary('Bella Casa Data for User Activity', 9000, group_filter="Payable")
t2 = time.time()
print(f"\n--- PAYABLE ONLY ---")
print(f"Count: {len(payable_ledgers)}, Time: {t2-t0:.2f}s")
top3_pay = sorted(payable_ledgers, key=lambda x: x['abs_balance'], reverse=True)[:3]
for i, l in enumerate(top3_pay):
    print(f"  {i+1}. {l['name']}: Rs {l['abs_balance']:,.2f}")

# Test 3: Fetch only Receivable ledgers
t0 = time.time()
recv_ledgers = client.fetch_ledger_summary('Bella Casa Data for User Activity', 9000, group_filter="Receivable")
t3 = time.time()
print(f"\n--- RECEIVABLE ONLY ---")
print(f"Count: {len(recv_ledgers)}, Time: {t3-t0:.2f}s")
top3_rec = sorted(recv_ledgers, key=lambda x: x['abs_balance'], reverse=True)[:3]
for i, l in enumerate(top3_rec):
    print(f"  {i+1}. {l['name']}: Rs {l['abs_balance']:,.2f}")
