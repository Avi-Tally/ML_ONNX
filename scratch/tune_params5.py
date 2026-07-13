import os
import re

def rewrite():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update date_target logic to include "paid" and "get" / "getting"
    old_target = """        if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending", "owe", "payable", "receivable"]):
            params["date_target"] = "due_date\""""
    new_target = """        if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending", "owe", "payable", "receivable", "paid", "get", "getting", "cash"]):
            params["date_target"] = "due_date\""""
    content = content.replace(old_target, new_target)

    # 2. Update amount filter regex to include commas and "greater than", "equal to"
    old_amt = """        amt_match = re.search(r'(less than|<|under|more than|>|above)\\s*(?:rs|inr|₹)?\\s*([\\d\\.]+)\\s*(k|l|lakh|cr|m)?\\b(?!\\s*days)', q_lower)"""
    new_amt = """        amt_match = re.search(r'(less than|<|under|more than|>|above|greater than|equal to)\\s*(?:rs|inr|₹)?\\s*([\\d\\.,]+)\\s*(k|l|lakh|cr|m)?\\b(?!\\s*days)', q_lower)"""
    content = content.replace(old_amt, new_amt)

    old_amt_logic = """            op = "<" if "less" in op_str or "<" in op_str or "under" in op_str else ">"
            if suf == 'k': val *= 1000"""
    new_amt_logic = """            if "less" in op_str or "<" in op_str or "under" in op_str: op = "<"
            elif "equal" in op_str: op = "="
            else: op = ">"
            if op == "=":
                # The labeler uses a weird hack for equal: < val + 1
                op = "<"
                val += 1.0
            
            if suf == 'k': val *= 1000"""
    content = content.replace(old_amt_logic, new_amt_logic)

    # Fix val float conversion for commas
    content = content.replace("val = float(amt_match.group(2))", "val = float(amt_match.group(2).replace(',', ''))")

    # 3. Fix date_filter "till_today" missing keywords
    old_till = """            if "pending" in q_lower or "till" in q_lower or "payable" in q_lower or "receivable" in q_lower or "due" in q_lower:"""
    new_till = """            if "pending" in q_lower or "till" in q_lower or "payable" in q_lower or "receivable" in q_lower or "due" in q_lower or "getting" in q_lower or "outstanding" in q_lower or "owe" in q_lower:"""
    content = content.replace(old_till, new_till)

    # 4. Limit fix for "first" or "highest" without numbers
    old_limit = """        elif "highest" in q_lower or "largest" in q_lower or "descending" in q_lower or "lowest" in q_lower:
            params["sort"] = {"field": "amount", "order": "asc" if "lowest" in q_lower else "desc"}
            if not params["limit"]:
                params["limit"] = 1 if "top" not in q_lower else 10"""
    new_limit = """        elif "highest" in q_lower or "largest" in q_lower or "descending" in q_lower or "lowest" in q_lower:
            params["sort"] = {"field": "amount", "order": "asc" if "lowest" in q_lower else "desc"}
            if not params["limit"]:
                # If they explicitly ask for list/first and no number, don't limit to 1
                if "first" in q_lower or "list" in q_lower or "bucket" in q_lower:
                    params["limit"] = None
                else:
                    params["limit"] = 1 if "top" not in q_lower else 10"""
    content = content.replace(old_limit, new_limit)

    # 5. is_bill_query fix for singular "bill" when not tied to a number
    old_bills = """        if "bills" in q_lower or "invoices" in q_lower:
            params["is_bill_query"] = True"""
    new_bills = """        if "bills" in q_lower or "invoices" in q_lower or "bill amount" in q_lower or "receivable bill" in q_lower or "payable bill" in q_lower:
            params["is_bill_query"] = True"""
    content = content.replace(old_bills, new_bills)

    # 6. document_ref fix for "613" being extracted as "bill"
    old_doc = """                    if next_token.pos_ == "NUM" or next_token.is_digit or re.match(r'^[a-z0-9\\-/\\\\]+$', next_token.text.lower()):
                        if next_token.text.lower() not in ["amount", "date", "number", "is", "for", "the", "a", "10", "5", "all"]:
                            params["is_bill_query"] = True
                            params["document_ref"] = next_token.text"""
    new_doc = """                    if next_token.pos_ == "NUM" or next_token.is_digit or re.match(r'^[a-z0-9\\-/\\\\]+$', next_token.text.lower()):
                        if next_token.text.lower() not in ["amount", "date", "number", "is", "for", "the", "a", "10", "5", "all", "bill", "invoice", "reference"]:
                            params["is_bill_query"] = True
                            params["document_ref"] = next_token.text"""
    content = content.replace(old_doc, new_doc)
    
    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    rewrite()
