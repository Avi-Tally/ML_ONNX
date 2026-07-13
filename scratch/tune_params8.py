import os
import re

def rewrite():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. is_bill_query for singular bill
    old_bills = """        if "bills" in q_lower or "invoices" in q_lower or "bill amount" in q_lower or "receivable bill" in q_lower or "payable bill" in q_lower or "collections due" in q_lower:
            params["is_bill_query"] = True"""
    new_bills = """        if "bills" in q_lower or "invoices" in q_lower or "bill amount" in q_lower or "receivable bill" in q_lower or "payable bill" in q_lower or "collections due" in q_lower:
            params["is_bill_query"] = True
        elif bool(re.search(r'\\b(?:oldest|latest|pending|unpaid|highest|lowest|which|overdue date)\\s+bill\\b', q_lower)):
            params["is_bill_query"] = True"""
    content = content.replace(old_bills, new_bills)

    # 2. limit=None enforcement for "first" or "list"
    old_sort = """            if "bill" in q_lower and "oldest" in q_lower:
                params["sort"] = {"field": "bill_date", "order": "asc"}
                if not params["limit"]: params["limit"] = 1"""
    new_sort = """            if "bill" in q_lower and "oldest" in q_lower:
                params["sort"] = {"field": "bill_date", "order": "asc"}
                if not params["limit"] and "first" not in q_lower and "list" not in q_lower: 
                    params["limit"] = 1"""
    content = content.replace(old_sort, new_sort)
    
    old_most = """        elif "highest" in q_lower or "largest" in q_lower or "descending" in q_lower or "lowest" in q_lower:"""
    new_most = """        elif "highest" in q_lower or "largest" in q_lower or "descending" in q_lower or "lowest" in q_lower or "most overdue" in q_lower:"""
    content = content.replace(old_most, new_most)

    # 3. "this quarter" handling
    old_date = """        elif "next hy" in q_lower or "next half year" in q_lower:
            params["date_filter"] = {"type": "next_days", "days": 180}"""
    new_date = """        elif "next hy" in q_lower or "next half year" in q_lower:
            params["date_filter"] = {"type": "next_days", "days": 180}
        elif "this quarter" in q_lower:
            params["date_filter"] = {"type": "last_days", "days": 90}"""
    content = content.replace(old_date, new_date)
    
    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    rewrite()
