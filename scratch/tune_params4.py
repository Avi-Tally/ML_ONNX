import os
import re

def rewrite():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update status_filter
    old_status = """        if is_cleared and "pending" in q_lower:
            params["status_filter"] = None # mixed query
        elif is_cleared:
            params["status_filter"] = "cleared"
        elif any(w in q_lower for w in ["pending", "overdue", "unpaid", "outstanding", "owe", "due"]):
            params["status_filter"] = "pending\""""

    new_status = """        if is_cleared and "pending" in q_lower:
            params["status_filter"] = None # mixed query
        elif is_cleared:
            params["status_filter"] = "cleared"
        elif any(w in q_lower for w in ["pending", "overdue", "unpaid"]):
            if "settled" in q_lower or "cleared" in q_lower:
                params["status_filter"] = None
            else:
                params["status_filter"] = "pending\""""
    content = content.replace(old_status, new_status)

    # 2. Update sum_only / count_only
    old_sum = """        is_compound = ("how many" in q_lower and ("total" in q_lower or "value" in q_lower)) or ("list" in q_lower)
        if is_compound:
            params["count_only"] = False
            params["sum_only"] = False
        else:
            params["sum_only"] = bool(re.search(r'\\b(total|sum|how much|net amount|amount)\\b', q_lower)) and not params["count_only"] and "amount is" not in q_lower and "amount less" not in q_lower and "amount greater" not in q_lower"""

    new_sum = """        is_compound = ("how many" in q_lower and ("total" in q_lower or "value" in q_lower)) or ("list" in q_lower and ("count" in q_lower or "total" in q_lower))
        
        # If they ask for count AND sum, tally handles it as False/False (List with totals)
        if ("how many" in q_lower and ("total" in q_lower or "value" in q_lower)):
            params["count_only"] = False
            params["sum_only"] = False
        else:
            # sum_only is true if they strictly ask for total/sum and NO bills/list/details
            if bool(re.search(r'\\b(total|sum|how much|net amount|amount)\\b', q_lower)) and not params["count_only"]:
                # exceptions where they are asking for amount filter or list of amounts
                if "amount is" in q_lower or "amount less" in q_lower or "amount greater" in q_lower or "opening amount" in q_lower or "amount equal" in q_lower or "balance" in q_lower:
                    params["sum_only"] = False
                elif "bills" in q_lower or "list" in q_lower:
                    params["sum_only"] = False
                else:
                    params["sum_only"] = True
            else:
                params["sum_only"] = False"""
    content = content.replace(old_sum, new_sum)

    # 3. Update date_target logic
    old_target = """        if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending", "owe", "payable", "receivable"]):
            params["date_target"] = "due_date"
        if "on account" in q_lower or "on-account" in q_lower:
            params["date_target"] = "bill_date"
        if "ledger" in q_lower and "balance" in q_lower:
            params["date_target"] = None
        if "outstanding balance" in q_lower and "ledger" in q_lower:
            params["date_target"] = None"""
            
    new_target = """        if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending", "owe", "payable", "receivable"]):
            params["date_target"] = "due_date"
        if "on account" in q_lower or "on-account" in q_lower:
            params["date_target"] = "bill_date"
        # For ledger balances or voucher queries, date_target is irrelevant/None
        if "ledger" in q_lower or "balance" in q_lower or "voucher type" in q_lower:
            if "bill" not in q_lower and "receivable" not in q_lower and "payable" not in q_lower:
                params["date_target"] = None
        # Explicit bill details
        if "which ledger is associated" in q_lower or "which voucher type" in q_lower:
            params["date_target"] = None"""
    content = content.replace(old_target, new_target)
    
    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    rewrite()
