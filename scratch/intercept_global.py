import re

def refactor():
    with open('mcp_server.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # If GET_RECEIVABLES / GET_PAYABLES has NO resolved ledger, intercept and use fetch_ledger_summary
    target_block = '''        # 8. ANALYTICAL INTENTS (Ageing, Receivables, Payables)
        elif intent in ["GET_RECEIVABLES", "GET_PAYABLES", "GET_AGEING"]:
            try:
                resolved_ledger = parsed.get("resolved_ledger")'''
                
    replacement_block = '''        # 8. ANALYTICAL INTENTS (Ageing, Receivables, Payables)
        elif intent in ["GET_RECEIVABLES", "GET_PAYABLES", "GET_AGEING"]:
            try:
                resolved_ledger = parsed.get("resolved_ledger")
                
                # INTERCEPT: If it's a global query (no ledger specified), do NOT download all bills!
                if not resolved_ledger and intent in ["GET_RECEIVABLES", "GET_PAYABLES"]:
                    group_name = "Sundry Debtors" if intent == "GET_RECEIVABLES" else "Sundry Creditors"
                    ledgers = tally_client.fetch_ledger_summary(company_name, port, group_name=group_name, from_date=f_date, to_date=t_date)
                    
                    total_parties = len(ledgers)
                    # For debtors, amounts are normally negative (Dr). We want absolute value.
                    total_val = sum(abs(l['amount']) for l in ledgers)
                    
                    md = [f"### {intent.replace('GET_', '').title()} Summary - {company_name}"]
                    md.append(f"**Total Parties:** {total_parties}  |  **Total Value:** ₹ {total_val:,.2f}")
                    return "\\n".join(md)
'''
    content = content.replace(target_block, replacement_block)

    with open('mcp_server.py', 'w', encoding='utf-8') as f:
        f.write(content)
        
refactor()
print("Intercept added successfully.")
