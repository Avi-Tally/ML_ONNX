import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient

client = TallyClient()
company = "Modi Chemplast Materials Pvt Ltd"
port = 9000

bills = client.fetch_bills(company, port, "All", reference_date="29-Nov-2025")
group_map = client.get_group_hierarchy_map(company, port)

targets = ["ASAHI YUKIZAI CORPORATION", "Zhejiang Heyue Flowtech Co.,Ltd."]

print("Tracing target bills:")
for b in bills:
    if b.get("party") in targets:
        pg_lower = b.get("parent_group", "").strip().lower()
        party_lower = b.get("party", "").strip().lower()
        
        try:
            amt_float = float(b.get("amount", "0").strip() or 0)
        except:
            amt_float = 0.0
            
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
        
        is_payable = False
        is_receivable = False
        
        if amt_float > 0:
            is_payable = True
        elif amt_float < 0:
            is_receivable = True
            
        if is_creditor:
            is_payable = True
        if is_debtor:
            is_receivable = True
            
        print(f"Party: {b.get('party')} | Bill: {b.get('name')} | Group: {b.get('parent_group')} | Amt: {amt_float} | IsCreditor: {is_creditor} | IsDebtor: {is_debtor} | IsPayable: {is_payable} | IsReceivable: {is_receivable}")
