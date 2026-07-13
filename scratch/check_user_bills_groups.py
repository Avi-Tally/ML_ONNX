import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Fetch ALL raw bills to ensure we see them regardless of classification
bills = client.fetch_bills(company, port, "All", reference_date="26-Nov-2025")

target_refs = ["792", "GSTCN/25-26/46", "EIRL/PO/P-100/224/25-26", "883", "SE/PO/25-26/011"]

print(f"Total bills in Tally: {len(bills)}")
print("\nInspecting the 5 bills:")
for ref in target_refs:
    found = False
    for b in bills:
        # Check if ref matches name/bill name
        if b.get("name", "").strip().lower() == ref.strip().lower() or ref.strip().lower() in b.get("name", "").strip().lower():
            found = True
            print(f"Party: {b.get('party')} | Bill Name: {b.get('name')} | Date: {b.get('date')} | Due: {b.get('due_date')} | Amt: {b.get('amount')} | Parent Group: {b.get('parent_group')}")
            
            # Check classification
            pg_lower = b.get("parent_group", "").strip().lower()
            party_lower = b.get("party", "").strip().lower()
            group_map = client.get_group_hierarchy_map(company, port)
            is_creditor = (
                client.is_group_under(pg_lower, "sundry creditors", group_map) or
                client.is_group_under(pg_lower, "trade payables", group_map) or
                any(w in pg_lower for w in ["creditor", "payable", "supplier", "vendor"]) or
                any(w in party_lower for w in ["creditor", "supplier", "vendor"])
            )
            is_debtor = (
                client.is_group_under(pg_lower, "sundry debtors", group_map) or
                client.is_group_under(pg_lower, "trade receivables", group_map) or
                any(w in pg_lower for w in ["debtor", "receivable", "customer", "client", "sales"]) or
                any(w in party_lower for w in ["debtor", "customer", "client"])
            )
            print(f"  -> IsCreditor={is_creditor} | IsDebtor={is_debtor}")
    if not found:
        print(f"Ref '{ref}' NOT found in Tally bills!")
