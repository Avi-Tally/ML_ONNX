import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

try:
    group_map = client.get_group_hierarchy_map(company, port)
    print(f"Group map fetched. Count: {len(group_map)}")
    
    # Let's inspect some groups in the group map
    target_groups = ["sundry creditors for expenses", "sundry creditors", "sundry creditors for goods", "gstr-2a creditors"]
    for tg in target_groups:
        parent = group_map.get(tg)
        is_under = client.is_group_under(tg, "sundry creditors", group_map)
        print(f"Group: '{tg}' | Parent in map: '{parent}' | Is under 'sundry creditors': {is_under}")
        
    bills = client.fetch_bills(company, port, "All")
    print(f"\nTotal raw bills: {len(bills)}")
    
    payables_count = 0
    receivables_count = 0
    unknown_count = 0
    
    print("\nSample Bills classification:")
    for b in bills[:20]:
        pg_lower = b.get("parent_group", "").strip().lower()
        party_lower = b.get("party", "").strip().lower()
        
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
        
        # Calculate how it would be classified
        classification = "Unknown"
        if is_creditor and not is_debtor:
            classification = "Payable"
            payables_count += 1
        elif is_debtor and not is_creditor:
            classification = "Receivable"
            receivables_count += 1
        else:
            try:
                amt = float(b.get("amount", 0))
            except:
                amt = 0.0
            classification = "Payable (Fallback)" if amt > 0 else "Receivable (Fallback)"
            if amt > 0:
                payables_count += 1
            else:
                receivables_count += 1
                
        print(f"Party: {b.get('party'):<30} | Group: {b.get('parent_group'):<20} | IsCreditor: {is_creditor:<5} | IsDebtor: {is_debtor:<5} | Class: {classification}")
        
    # Count total classified
    for b in bills[20:]:
        pg_lower = b.get("parent_group", "").strip().lower()
        party_lower = b.get("party", "").strip().lower()
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
        if is_creditor and not is_debtor:
            payables_count += 1
        elif is_debtor and not is_creditor:
            receivables_count += 1
        else:
            try:
                amt = float(b.get("amount", 0))
            except:
                amt = 0.0
            if amt > 0:
                payables_count += 1
            else:
                receivables_count += 1
                
    print(f"\nFinal Totals: Payables={payables_count} | Receivables={receivables_count}")
except Exception as e:
    print("Error:", e)
