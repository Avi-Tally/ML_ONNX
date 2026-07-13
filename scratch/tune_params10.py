import os
import re

def rewrite():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. status_filter mixed queries
    old_status = """        if is_cleared and any(w in q_lower for w in ["pending", "due", "outstanding", "unpaid", "overdue"]):
            params["status_filter"] = None # mixed query"""
    new_status = """        if is_cleared and bool(re.search(r'\\b(pending|due|dues|outstanding|unpaid|overdue)\\s+(?:and|or|as well as|also)\\s+(?:cleared|settled|paid)\\b', q_lower)) or bool(re.search(r'\\b(?:cleared|settled|paid)\\s+(?:and|or|as well as|also)\\s+(pending|due|dues|outstanding|unpaid|overdue)\\b', q_lower)):
            params["status_filter"] = None # mixed query"""
    content = content.replace(old_status, new_status)

    # 2. date_target for groups and ageing
    old_target = """        if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending", "owe", "payable", "receivable", "paid", "get", "getting", "cash", "received", "receipts"]):
            params["date_target"] = "due_date"
        if "on account" in q_lower or "on-account" in q_lower:
            params["date_target"] = "bill_date"
        if "ledger" in q_lower or "balance" in q_lower or "voucher type" in q_lower:
            if "bill" not in q_lower and "receivable" not in q_lower and "payable" not in q_lower and "on-account" not in q_lower and "on account" not in q_lower:
                params["date_target"] = None"""
    new_target = """        if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending", "owe", "payable", "receivable", "paid", "get", "getting", "cash", "received", "receipts"]):
            params["date_target"] = "due_date"
        if "on account" in q_lower or "on-account" in q_lower:
            params["date_target"] = "bill_date"
        if "ledger" in q_lower or "balance" in q_lower or "voucher type" in q_lower or "group" in q_lower or "ageing" in q_lower:
            if "bill" not in q_lower and "receivable" not in q_lower and "payable" not in q_lower and "on-account" not in q_lower and "on account" not in q_lower:
                params["date_target"] = None
        if "ageing" in q_lower or "group" in q_lower:
            params["date_target"] = None"""
    content = content.replace(old_target, new_target)

    # 3. sum_only strictness
    old_sum = """            if bool(re.search(r'\\b(total|sum|how much|net amount|amount)\\b', q_lower)) and not params["count_only"]:
                # exceptions where they are asking for amount filter or list of amounts
                if "amount is" in q_lower or "amount greater" in q_lower or "amount equal" in q_lower or "balance" in q_lower or "any pending amount" in q_lower or "tax amount" in q_lower:
                    params["sum_only"] = False
                elif "bills" in q_lower or "list" in q_lower:
                    params["sum_only"] = False
                else:
                    params["sum_only"] = True
            else:
                params["sum_only"] = False"""
    new_sum = """            if bool(re.search(r'\\b(total|sum|how much|net amount|amount)\\b', q_lower)) and not params["count_only"]:
                # exceptions where they are asking for amount filter or list of amounts
                if "amount is" in q_lower or "amount greater" in q_lower or "amount equal" in q_lower or "balance" in q_lower or "any pending amount" in q_lower or "tax amount" in q_lower or "total pending amount" in q_lower:
                    params["sum_only"] = False
                elif "bills" in q_lower or "list" in q_lower or "what do i owe" in q_lower:
                    params["sum_only"] = False
                elif params["limit"] == 1:
                    params["sum_only"] = False
                else:
                    params["sum_only"] = True
            else:
                params["sum_only"] = False"""
    content = content.replace(old_sum, new_sum)

    # 4. is_bill_query
    old_bills = """        if params["is_bill_query"] and not params["document_ref"]:
            if bool(re.search(r'\\b(parties|debtors|creditors|payments)\\b', q_lower)) and not bool(re.search(r'\\b(list|show|all).*bills\\b', q_lower)):
                params["is_bill_query"] = False"""
    new_bills = """        if params["is_bill_query"] and not params["document_ref"]:
            if bool(re.search(r'\\b(parties|debtors|creditors|payments)\\b', q_lower)):
                if not bool(re.search(r'\\b(list|show|all).*bills\\b', q_lower)) and not bool(re.search(r'oldest.*bill', q_lower)):
                    params["is_bill_query"] = False"""
    content = content.replace(old_bills, new_bills)

    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    rewrite()
