import re

def refactor():
    with open('mcp_server.py', 'r', encoding='utf-8') as f:
        content = f.read()

    target_block = '''                # INTERCEPT: If it's a global query (no ledger specified), do NOT download all bills!
                if not resolved_ledger and intent in ["GET_RECEIVABLES", "GET_PAYABLES"]:
                    group_name = "Sundry Debtors" if intent == "GET_RECEIVABLES" else "Sundry Creditors"'''
                
    replacement_block = '''                # INTERCEPT: If it's a global query (no ledger specified), do NOT download all bills!
                if not resolved_ledger and intent == "GET_AGEING":
                    return "Global ageing reports across all parties are too large to process in real-time. Please specify a party name (e.g., 'Show ageing for adinath')."

                if not resolved_ledger and intent in ["GET_RECEIVABLES", "GET_PAYABLES"]:
                    group_name = "Sundry Debtors" if intent == "GET_RECEIVABLES" else "Sundry Creditors"'''
                    
    content = content.replace(target_block, replacement_block)

    with open('mcp_server.py', 'w', encoding='utf-8') as f:
        f.write(content)
        
refactor()
print("Ageing block added successfully.")
