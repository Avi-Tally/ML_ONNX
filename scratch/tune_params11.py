import os
import re

def rewrite():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. count_only for compound queries with "how many" and "list"
    old_count = """        is_compound = ("how many" in q_lower and ("total" in q_lower or "value" in q_lower)) or ("list" in q_lower and ("count" in q_lower or "total" in q_lower))"""
    new_count = """        is_compound = ("how many" in q_lower and ("total" in q_lower or "value" in q_lower or "list" in q_lower)) or ("list" in q_lower and ("count" in q_lower or "total" in q_lower))"""
    content = content.replace(old_count, new_count)

    # 2. age_filter exclusions for "ageing" and "within"
    old_age = """        days_match = re.search(r'(\\d+)\\s*days?', q_lower)
        if days_match:
            days = int(days_match.group(1))
            op = "<" if any(w in q_lower for w in ["less", "under", "<"]) else ">"
            params["age_filter"] = {"operator": op, "days": days}"""
    new_age = """        days_match = re.search(r'(\\d+)\\s*days?', q_lower)
        if days_match and "ageing" not in q_lower and "within" not in q_lower and "next" not in q_lower and "last" not in q_lower:
            days = int(days_match.group(1))
            op = "<" if any(w in q_lower for w in ["less", "under", "<"]) else ">"
            params["age_filter"] = {"operator": op, "days": days}"""
    content = content.replace(old_age, new_age)

    # 3. limit extraction for "latests"
    old_limit = """        match = re.search(r'\\b(top|last|first|oldest|highest)\\s+(\\d+)\\b', q_lower)"""
    new_limit = """        match = re.search(r'\\b(top|last|first|oldest|highest|latest|latests)\\s+(\\d+)\\b', q_lower)"""
    content = content.replace(old_limit, new_limit)

    # 4. sum_only "net" keyword
    old_sum = """            if bool(re.search(r'\\b(total|sum|how much|net amount|amount)\\b', q_lower)) and not params["count_only"]:"""
    new_sum = """            if bool(re.search(r'\\b(total|sum|how much|net amount|net|amount)\\b', q_lower)) and not params["count_only"]:"""
    content = content.replace(old_sum, new_sum)
    
    # 5. Fix "oldest unpaid bill" which was still false because "unpaid" was overriding? No, is_bill_query was False for "Show highest pending... bill amount".
    old_bill2 = """        elif bool(re.search(r'\\b(?:oldest|latest|pending|unpaid|highest|lowest|which|overdue date)\\s+bill\\b', q_lower)):
            params["is_bill_query"] = True"""
    new_bill2 = """        elif bool(re.search(r'\\b(?:oldest|latest|pending|unpaid|highest|lowest|which|overdue date|receivables|payables)\\s+bill\\b', q_lower)) or "bill amount" in q_lower:
            params["is_bill_query"] = True"""
    content = content.replace(old_bill2, new_bill2)

    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    rewrite()
