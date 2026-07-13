import os
import re

def rewrite():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. status_filter
    old_status = """        if is_cleared and "pending" in q_lower:
            params["status_filter"] = None # mixed query
        elif is_cleared:
            params["status_filter"] = "cleared"
        elif any(w in q_lower for w in ["pending", "overdue", "unpaid"]):"""
    new_status = """        if is_cleared and any(w in q_lower for w in ["pending", "due", "outstanding", "unpaid", "overdue"]):
            params["status_filter"] = None # mixed query
        elif is_cleared:
            params["status_filter"] = "cleared"
        elif any(w in q_lower for w in ["pending", "overdue", "unpaid", "not paid"]):"""
    content = content.replace(old_status, new_status)
    
    old_status2 = """                params["status_filter"] = "pending\""""
    new_status2 = """                params["status_filter"] = "pending"
                
        # If explicitly asking for a single bill's details, status doesn't matter
        if params.get("document_ref") and "overdue" not in q_lower:
            params["status_filter"] = None"""
    content = content.replace(old_status2, new_status2)

    # 2. sum_only
    old_sum = """                if "amount is" in q_lower or "amount greater" in q_lower or "opening amount" in q_lower or "amount equal" in q_lower or "balance" in q_lower:"""
    new_sum = """                if "amount is" in q_lower or "amount greater" in q_lower or "amount equal" in q_lower or "balance" in q_lower or "any pending amount" in q_lower or "tax amount" in q_lower:"""
    content = content.replace(old_sum, new_sum)

    # 3. is_bill_query exceptions for parties/payments
    old_bills = """        elif bool(re.search(r'\\b(?:oldest|latest|pending|unpaid|highest|lowest|which|overdue date)\\s+bill\\b', q_lower)):
            params["is_bill_query"] = True"""
    new_bills = """        elif bool(re.search(r'\\b(?:oldest|latest|pending|unpaid|highest|lowest|which|overdue date)\\s+bill\\b', q_lower)):
            params["is_bill_query"] = True
            
        if params["is_bill_query"] and not params["document_ref"]:
            if bool(re.search(r'\\b(parties|debtors|creditors|payments)\\b', q_lower)) and not bool(re.search(r'\\b(list|show|all).*bills\\b', q_lower)):
                params["is_bill_query"] = False"""
    content = content.replace(old_bills, new_bills)

    # 4. date_filter explicit timeframes
    old_date = """        elif "this quarter" in q_lower:
            params["date_filter"] = {"type": "last_days", "days": 90}"""
    new_date = """        elif "this quarter" in q_lower:
            params["date_filter"] = {"type": "last_days", "days": 90}
        elif "past 6 months" in q_lower:
            params["date_filter"] = {"type": "last_days", "days": 180}
        elif "within 7 days" in q_lower:
            params["date_filter"] = {"type": "next_days", "days": 7}"""
    content = content.replace(old_date, new_date)

    # 5. date_target 
    old_target = """        if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending", "owe", "payable", "receivable", "paid", "get", "getting", "cash"]):
            params["date_target"] = "due_date"
        if "on account" in q_lower or "on-account" in q_lower:"""
    new_target = """        if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending", "owe", "payable", "receivable", "paid", "get", "getting", "cash", "received", "receipts"]):
            params["date_target"] = "due_date"
        if "on account" in q_lower or "on-account" in q_lower:"""
    content = content.replace(old_target, new_target)
    
    old_target2 = """        if "which ledger is associated" in q_lower or "which voucher type" in q_lower:
            params["date_target"] = None"""
    new_target2 = """        if "which ledger is associated" in q_lower or "which voucher type" in q_lower or params.get("document_ref"):
            params["date_target"] = None"""
    content = content.replace(old_target2, new_target2)

    # 6. sort fix
    old_sort = """        elif "highest" in q_lower or "largest" in q_lower or "descending" in q_lower or "lowest" in q_lower or "most overdue" in q_lower:
            params["sort"] = {"field": "amount", "order": "asc" if "lowest" in q_lower else "desc"}"""
    new_sort = """        elif "highest" in q_lower or "largest" in q_lower or "descending" in q_lower or "lowest" in q_lower or "most overdue" in q_lower:
            if "most overdue" in q_lower or "least overdue" in q_lower:
                params["sort"] = {"field": "due_date", "order": "desc" if "least" in q_lower else "asc"}
            else:
                params["sort"] = {"field": "amount", "order": "asc" if "lowest" in q_lower else "desc"}
            
            # Ageing reports rarely have a standard sort parameter in our spec
            if "ageing" in q_lower:
                params["sort"] = None"""
    content = content.replace(old_sort, new_sort)

    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    rewrite()
