import os
import re

def rewrite():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. limit regex
    old_limit = """        limit_match = re.search(r"(?:top|first|oldest|highest|lowest)\\s+(\\d+)|\\b(\\d+)\\s+(?:top|first|oldest|highest|lowest)\\b", q_lower)"""
    new_limit = """        limit_match = re.search(r"(?:top|last|latest|latests|first|oldest|highest|lowest)\\s+(\\d+)|\\b(\\d+)\\s+(?:top|last|latest|latests|first|oldest|highest|lowest)\\b", q_lower)"""
    content = content.replace(old_limit, new_limit)

    # 2. limit default logic
    old_default = """                if "first" in q_lower or "list" in q_lower or "bucket" in q_lower:
                    params["limit"] = None
                else:
                    params["limit"] = 1 if "top" not in q_lower else 10"""
    new_default = """                if "first" in q_lower or "list" in q_lower or "bucket" in q_lower or "show" in q_lower or "all" in q_lower:
                    params["limit"] = None
                else:
                    params["limit"] = 1 if "top" not in q_lower else 10"""
    content = content.replace(old_default, new_default)

    # 3. is_bill_query
    old_bill = """        if params["is_bill_query"] and not params["document_ref"]:
            if bool(re.search(r'\\b(parties|debtors|creditors|payments)\\b', q_lower)):
                if not bool(re.search(r'\\b(list|show|all).*bills\\b', q_lower)) and not bool(re.search(r'oldest.*bill', q_lower)):
                    params["is_bill_query"] = False"""
    new_bill = """        if params["is_bill_query"] and not params["document_ref"]:
            if bool(re.search(r'\\b(parties|debtors|creditors|payments)\\b', q_lower)):
                if not bool(re.search(r'\\b(list|show|all).*bills\\b', q_lower)) and not bool(re.search(r'oldest.*bill', q_lower)) and "bill amount" not in q_lower:
                    params["is_bill_query"] = False"""
    content = content.replace(old_bill, new_bill)

    # 4. date_target for debtors/creditors
    old_target = """        if "ledger" in q_lower or "balance" in q_lower or "voucher type" in q_lower or "group" in q_lower or "ageing" in q_lower:
            if "bill" not in q_lower and "receivable" not in q_lower and "payable" not in q_lower and "on-account" not in q_lower and "on account" not in q_lower:
                params["date_target"] = None
        if "ageing" in q_lower or "group" in q_lower:
            params["date_target"] = None"""
    new_target = """        if "ledger" in q_lower or "balance" in q_lower or "voucher type" in q_lower or "group" in q_lower or "ageing" in q_lower:
            if "bill" not in q_lower and "receivable" not in q_lower and "payable" not in q_lower and "on-account" not in q_lower and "on account" not in q_lower:
                params["date_target"] = None
        if "ageing" in q_lower or "group" in q_lower or "debtor" in q_lower or "creditor" in q_lower:
            params["date_target"] = None"""
    content = content.replace(old_target, new_target)

    # 5. sum_only
    old_sum = """                if "amount is" in q_lower or "amount greater" in q_lower or "amount equal" in q_lower or "balance" in q_lower or "any pending amount" in q_lower or "tax amount" in q_lower or "total pending amount" in q_lower:
                    params["sum_only"] = False
                elif "bills" in q_lower or "list" in q_lower or "what do i owe" in q_lower:
                    params["sum_only"] = False"""
    new_sum = """                if "amount is" in q_lower or "amount greater" in q_lower or "amount equal" in q_lower or "balance" in q_lower or "any pending amount" in q_lower or "tax amount" in q_lower or "total pending amount" in q_lower or "how much is overdue" in q_lower or "how much does" in q_lower:
                    params["sum_only"] = False
                elif "bills" in q_lower or "list" in q_lower or "what do i owe" in q_lower:
                    params["sum_only"] = False"""
    content = content.replace(old_sum, new_sum)

    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    rewrite()
