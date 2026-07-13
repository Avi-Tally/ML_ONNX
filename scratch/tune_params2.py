import os
import re

def rewrite():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update status_filter and count/sum logic
    old_status = """        # Binary flags & simple keyword limits
        is_cleared = bool(re.search(r'\\b(cleared|settled)\\b', q_lower) or re.search(r'(?<!not )(?<!to be )\\bpaid\\b', q_lower))
        is_pending = bool(re.search(r'\\b(pending|outstanding|unpaid|due|overdue)\\b', q_lower) or "not paid" in q_lower or "to be paid" in q_lower)
        
        if is_pending and is_cleared:
            params["status_filter"] = None
        elif is_pending:
            params["status_filter"] = "pending"
        elif is_cleared:
            params["status_filter"] = "cleared"
            
        params["count_only"] = "how many" in q_lower or bool(re.search(r'\\bcount\\b', q_lower))
        params["sum_only"] = "total value" in q_lower or "total amount" in q_lower or "sum" in q_lower"""

    new_status = """        # Binary flags & simple keyword limits
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

    content = content.replace(old_status, new_status)

    # 2. Update date_target logic
    old_target = """        if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending to receive", "pending to pay"]):
            params["date_target"] = "due_date\""""

    new_target = """        if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending", "owe", "payable", "receivable"]):
            params["date_target"] = "due_date"
        if "on account" in q_lower or "on-account" in q_lower:
            params["date_target"] = "bill_date\""""

    content = content.replace(old_target, new_target)

    # 3. Update sort logic
    old_sort = """        if "oldest" in q_lower or "ascending" in q_lower:
            if "bill date" in q_lower or "billdate" in q_lower:
                params["sort"] = {"field": "bill_date", "order": "asc"}
            else:
                params["sort"] = {"field": params["date_target"], "order": "asc"}
        elif "highest" in q_lower or "largest" in q_lower:
            params["sort"] = {"field": "amount", "order": "desc"}
            if not params["limit"]:
                params["limit"] = 10"""

    new_sort = """        if "oldest" in q_lower or "ascending" in q_lower or "asc" in q_lower:
            if "bill" in q_lower and "oldest" in q_lower:
                params["sort"] = {"field": "bill_date", "order": "asc"}
            elif "bill date" in q_lower or "billdate" in q_lower:
                params["sort"] = {"field": "bill_date", "order": "asc"}
            elif "amount" in q_lower:
                params["sort"] = {"field": "amount", "order": "asc"}
            else:
                params["sort"] = {"field": params["date_target"], "order": "asc"}
        elif "highest" in q_lower or "largest" in q_lower or "descending" in q_lower:
            params["sort"] = {"field": "amount", "order": "desc"}
            if not params["limit"]:
                params["limit"] = 10
        elif "maximum overdue days" in q_lower:
            params["sort"] = {"field": "due_date", "order": "asc"}"""

    content = content.replace(old_sort, new_sort)

    # 4. Fix AMOUNT filter to ignore "90 days"
    old_amt = """        amt_match = re.search(r'(less than|<|under|more than|>|above)\\s*(?:rs|inr|₹)?\\s*([\\d\\.]+)\\s*(k|l|lakh|cr|m)?\\b', q_lower)"""
    new_amt = """        amt_match = re.search(r'(less than|<|under|more than|>|above)\\s*(?:rs|inr|₹)?\\s*([\\d\\.]+)\\s*(k|l|lakh|cr|m)?\\b(?!\\s*days)', q_lower)"""
    content = content.replace(old_amt, new_amt)

    old_spacy_amt = """                if op:
                    val_str = text.replace(",", "").replace("rs", "").replace("inr", "").replace("₹", "").strip()"""
    new_spacy_amt = """                if op and "days" not in q_lower[ent.end_char:ent.end_char+10]:
                    val_str = text.replace(",", "").replace("rs", "").replace("inr", "").replace("₹", "").strip()"""
    content = content.replace(old_spacy_amt, new_spacy_amt)

    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    rewrite()
