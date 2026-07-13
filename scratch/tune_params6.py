import os
import re

def rewrite():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. document_ref requires a digit
    old_doc1 = """                    if child.pos_ == "NUM" or child.is_digit or re.match(r'^[a-z0-9\\-/\\\\]+$', child.text.lower()):
                        if child.text.lower() not in ["10", "5", "all", "any", "no", "one"]:
                            params["is_bill_query"] = True
                            params["document_ref"] = child.text
                            break"""
    new_doc1 = """                    if child.pos_ == "NUM" or child.is_digit or re.match(r'^[a-z0-9\\-/\\\\]+$', child.text.lower()):
                        if child.text.lower() not in ["10", "5", "all", "any", "no", "one"] and bool(re.search(r'\\d', child.text)):
                            params["is_bill_query"] = True
                            params["document_ref"] = child.text
                            break"""
    content = content.replace(old_doc1, new_doc1)

    old_doc2 = """                    if next_token.pos_ == "NUM" or next_token.is_digit or re.match(r'^[a-z0-9\\-/\\\\]+$', next_token.text.lower()):
                        if next_token.text.lower() not in ["amount", "date", "number", "is", "for", "the", "a", "10", "5", "all", "bill", "invoice", "reference"]:
                            params["is_bill_query"] = True
                            params["document_ref"] = next_token.text"""
    new_doc2 = """                    if next_token.pos_ == "NUM" or next_token.is_digit or re.match(r'^[a-z0-9\\-/\\\\]+$', next_token.text.lower()):
                        if next_token.text.lower() not in ["amount", "date", "number", "is", "for", "the", "a", "10", "5", "all", "bill", "invoice", "reference"] and bool(re.search(r'\\d', next_token.text)):
                            params["is_bill_query"] = True
                            params["document_ref"] = next_token.text"""
    content = content.replace(old_doc2, new_doc2)

    # 2. is_bill_query fallback logic
    old_bills = """        if "bills" in q_lower or "invoices" in q_lower or "bill amount" in q_lower or "receivable bill" in q_lower or "payable bill" in q_lower:
            params["is_bill_query"] = True"""
    new_bills = """        if "bills" in q_lower or "invoices" in q_lower or "bill amount" in q_lower or "receivable bill" in q_lower or "payable bill" in q_lower:
            params["is_bill_query"] = True
            
        if params["is_bill_query"] and not params["document_ref"]:
            if any(w in q_lower for w in ["parties", "debtors", "creditors", "payments", "collections"]):
                if not any(w in q_lower for w in ["customers bills", "vendors bills", "suppliers bills", "party bills"]):
                    params["is_bill_query"] = False"""
    content = content.replace(old_bills, new_bills)

    # 3. Explicit date ranges for FY and "next month" / "next hy"
    old_date = """        my_match = re.search(r'\\b(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)\\s+(\\d{4})\\b', q_lower)
        if my_match:"""
    new_date = """        fy_match = re.search(r'\\bfy\\s*(?:20)?(\\d{2})-(?:20)?(\\d{2})\\b', q_lower)
        if fy_match:
            sy = int("20" + fy_match.group(1))
            ey = int("20" + fy_match.group(2))
            params["date_filter"] = {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": sy, "end_day": 31, "end_month": 3, "end_year": ey}
        elif "next month" in q_lower:
            params["date_filter"] = {"type": "next_days", "days": 30}
        elif "next hy" in q_lower or "next half year" in q_lower:
            params["date_filter"] = {"type": "next_days", "days": 180}
            
        my_match = re.search(r'\\b(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)\\s+(\\d{4})\\b', q_lower)
        if my_match and not params["date_filter"]:"""
    content = content.replace(old_date, new_date)
    
    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    rewrite()
