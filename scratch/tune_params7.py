import os
import re

def rewrite():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Revert is_bill_query overly broad fallback
    old_bills = """        if "bills" in q_lower or "invoices" in q_lower or "bill amount" in q_lower or "receivable bill" in q_lower or "payable bill" in q_lower:
            params["is_bill_query"] = True
            
        if params["is_bill_query"] and not params["document_ref"]:
            if any(w in q_lower for w in ["parties", "debtors", "creditors", "payments", "collections"]):
                if not any(w in q_lower for w in ["customers bills", "vendors bills", "suppliers bills", "party bills"]):
                    params["is_bill_query"] = False"""
    new_bills = """        if "bills" in q_lower or "invoices" in q_lower or "bill amount" in q_lower or "receivable bill" in q_lower or "payable bill" in q_lower or "collections due" in q_lower:
            params["is_bill_query"] = True"""
    content = content.replace(old_bills, new_bills)

    # 2. Fix limit for oldest and latest
    old_sort = """        if "oldest" in q_lower or "ascending" in q_lower or "asc" in q_lower:
            if "bill" in q_lower and "oldest" in q_lower:
                params["sort"] = {"field": "bill_date", "order": "asc"}
            elif "bill date" in q_lower or "billdate" in q_lower:
                params["sort"] = {"field": "bill_date", "order": "asc"}
            elif "amount" in q_lower:
                params["sort"] = {"field": "amount", "order": "asc"}
            else:
                params["sort"] = {"field": params["date_target"], "order": "asc"}"""
    new_sort = """        if "oldest" in q_lower or "ascending" in q_lower or "asc" in q_lower or "latest" in q_lower:
            if "bill" in q_lower and "oldest" in q_lower:
                params["sort"] = {"field": "bill_date", "order": "asc"}
                if not params["limit"]: params["limit"] = 1
            elif "latest" in q_lower:
                params["sort"] = {"field": "bill_date", "order": "desc"}
            elif "bill date" in q_lower or "billdate" in q_lower:
                params["sort"] = {"field": "bill_date", "order": "asc"}
            elif "amount" in q_lower:
                params["sort"] = {"field": "amount", "order": "asc"}
            else:
                params["sort"] = {"field": params["date_target"], "order": "asc"}"""
    content = content.replace(old_sort, new_sort)

    # 3. Simplify sum_only to remove bad exception
    old_sum = """                # exceptions where they are asking for amount filter or list of amounts
                if "amount is" in q_lower or "amount less" in q_lower or "amount greater" in q_lower or "opening amount" in q_lower or "amount equal" in q_lower or "balance" in q_lower:
                    params["sum_only"] = False"""
    new_sum = """                # exceptions where they are asking for amount filter or list of amounts
                if "amount is" in q_lower or "amount greater" in q_lower or "opening amount" in q_lower or "amount equal" in q_lower or "balance" in q_lower:
                    params["sum_only"] = False"""
    content = content.replace(old_sum, new_sum)

    # 4. Fix date target for ledger "on-account" conflict
    old_target = """        if "ledger" in q_lower or "balance" in q_lower or "voucher type" in q_lower:
            if "bill" not in q_lower and "receivable" not in q_lower and "payable" not in q_lower:
                params["date_target"] = None"""
    new_target = """        if "ledger" in q_lower or "balance" in q_lower or "voucher type" in q_lower:
            if "bill" not in q_lower and "receivable" not in q_lower and "payable" not in q_lower and "on-account" not in q_lower and "on account" not in q_lower:
                params["date_target"] = None"""
    content = content.replace(old_target, new_target)
    
    # 5. Add between dates
    old_between = """        my_match = re.search(r'\\b(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)\\s+(\\d{4})\\b', q_lower)"""
    new_between = """        bw_match = re.search(r'between\\s+(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)\\s+(\\d{4})\\s+and\\s+(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)\\s+(\\d{4})', q_lower)
        if bw_match:
            month_map = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
            sm = month_map[bw_match.group(1)[:3]]
            sy = int(bw_match.group(2))
            em = month_map[bw_match.group(3)[:3]]
            ey = int(bw_match.group(4))
            import calendar
            end_day = calendar.monthrange(ey, em)[1]
            params["date_filter"] = {"type": "explicit_range", "start_day": 1, "start_month": sm, "start_year": sy, "end_day": end_day, "end_month": em, "end_year": ey}
            
        my_match = re.search(r'\\b(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)\\s+(\\d{4})\\b', q_lower)"""
    content = content.replace(old_between, new_between)

    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    rewrite()
