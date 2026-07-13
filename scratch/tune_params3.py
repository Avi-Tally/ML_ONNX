import os
import re

def rewrite():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update status_filter and count/sum logic
    old_status = """        # Binary flags & simple keyword limits
        is_cleared = bool(re.search(r'\\b(cleared|settled)\\b', q_lower) or re.search(r'(?<!not )(?<!to be )\\bpaid\\b', q_lower))
        # Default pending is usually implied by payables/receivables intents. 
        # Only set status_filter to pending if explicitly asked for "pending bills" vs just "payables"
        if is_cleared:
            params["status_filter"] = "cleared"
        elif "pending" in q_lower and "bill" in q_lower:
            params["status_filter"] = "pending"
        elif "unpaid" in q_lower:
            params["status_filter"] = "pending"
            
        # Count and Sum
        if "how many days" in q_lower:
            params["count_only"] = False
        else:
            params["count_only"] = ("how many" in q_lower or bool(re.search(r'\\bcount\\b', q_lower))) and "total" not in q_lower

        params["sum_only"] = bool(re.search(r'\\b(total|sum|how much)\\b', q_lower)) and not params["count_only"]"""

    new_status = """        # Binary flags & simple keyword limits
        is_cleared = bool(re.search(r'\\b(cleared|settled)\\b', q_lower) or re.search(r'(?<!not )(?<!to be )\\bpaid\\b', q_lower))
        if is_cleared and "pending" in q_lower:
            params["status_filter"] = None # mixed query
        elif is_cleared:
            params["status_filter"] = "cleared"
        elif any(w in q_lower for w in ["pending", "overdue", "unpaid", "outstanding", "owe", "due"]):
            params["status_filter"] = "pending"
            
        # Count and Sum
        if "how many days" in q_lower:
            params["count_only"] = False
        else:
            params["count_only"] = ("how many" in q_lower or bool(re.search(r'\\bcount\\b', q_lower))) and "total" not in q_lower and "value" not in q_lower and "amount" not in q_lower

        is_compound = ("how many" in q_lower and ("total" in q_lower or "value" in q_lower)) or ("list" in q_lower)
        if is_compound:
            params["count_only"] = False
            params["sum_only"] = False
        else:
            params["sum_only"] = bool(re.search(r'\\b(total|sum|how much|net amount|amount)\\b', q_lower)) and not params["count_only"] and "amount is" not in q_lower and "amount less" not in q_lower and "amount greater" not in q_lower"""

    content = content.replace(old_status, new_status)

    # 3. Update limit
    old_sort = """        elif "highest" in q_lower or "largest" in q_lower or "descending" in q_lower:
            params["sort"] = {"field": "amount", "order": "desc"}
            if not params["limit"]:
                params["limit"] = 10"""

    new_sort = """        elif "highest" in q_lower or "largest" in q_lower or "descending" in q_lower or "lowest" in q_lower:
            params["sort"] = {"field": "amount", "order": "asc" if "lowest" in q_lower else "desc"}
            if not params["limit"]:
                params["limit"] = 1 if "top" not in q_lower else 10"""
    content = content.replace(old_sort, new_sort)

    # 4. date target for ledger balance
    old_target = """        if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending", "owe", "payable", "receivable"]):
            params["date_target"] = "due_date"
        if "on account" in q_lower or "on-account" in q_lower:
            params["date_target"] = "bill_date\""""

    new_target = """        if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending", "owe", "payable", "receivable"]):
            params["date_target"] = "due_date"
        if "on account" in q_lower or "on-account" in q_lower:
            params["date_target"] = "bill_date"
        if "ledger" in q_lower and "balance" in q_lower:
            params["date_target"] = None
        if "outstanding balance" in q_lower and "ledger" in q_lower:
            params["date_target"] = None"""
            
    content = content.replace(old_target, new_target)
    
    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    rewrite()
