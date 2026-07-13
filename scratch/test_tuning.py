import spacy
import re
from rapidfuzz import process, fuzz

nlp = spacy.load("en_core_web_sm")

def extract_params(query):
    doc = nlp(query.lower())
    q_lower = query.lower()
    
    params = {
        "date_filter": None,
        "age_filter": None,
        "amount_filter": None,
        "limit": None,
        "sort": None,
        "reference_date": None,
        "is_bill_query": False,
        "document_ref": None,
        "date_target": "bill_date",
        "count_only": False,
        "sum_only": False,
        "status_filter": None
    }
    
    if "till date" in q_lower or "today" in q_lower:
        if "pending" in q_lower or "till" in q_lower or "payable" in q_lower or "receivable" in q_lower or "due" in q_lower:
            params["date_filter"] = {"type": "till_today"}
        else:
            params["date_filter"] = {"type": "today"}

    # Month Year regex fallback because spaCy is sometimes weird
    my_match = re.search(r'\b(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)\s+(\d{4})\b', q_lower)
    if my_match:
        month_str = my_match.group(1)[:3].title()
        month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
        params["date_filter"] = {"type": "month_year", "month": month_map[month_str], "year": int(my_match.group(2))}

    # Amount fallback
    amt_match = re.search(r'(less than|<|under|more than|>|above)\s*(?:rs|inr|₹)?\s*([\d\.]+)\s*(k|l|lakh|cr|m)\b', q_lower)
    if amt_match:
        op_str = amt_match.group(1)
        val = float(amt_match.group(2))
        suf = amt_match.group(3)
        op = "<" if "less" in op_str or "<" in op_str or "under" in op_str else ">"
        if suf == 'k': val *= 1000
        elif suf in ['l', 'lakh']: val *= 100000
        elif suf in ['cr']: val *= 10000000
        params["amount_filter"] = {"operator": op, "value": val}

    for token in doc:
        # Document ref
        if token.text in ["bill", "invoice", "voucher", "reference", "no", "number"]:
            params["is_bill_query"] = True
            for child in token.children:
                if child.pos_ == "NUM" or child.is_digit or re.match(r'^[a-z0-9\-/\\]+$', child.text):
                    if child.text not in ["10", "5", "all", "any", "no", "one"]:
                        params["document_ref"] = child.text
                        break
            if not params["document_ref"] and token.i + 1 < len(doc):
                next_token = doc[token.i + 1]
                if next_token.pos_ == "NUM" or next_token.is_digit or re.match(r'^[a-z0-9\-/\\]+$', next_token.text):
                    if next_token.text not in ["amount", "date", "number", "is", "for", "the", "a", "10", "5", "all"]:
                        params["document_ref"] = next_token.text
                        
    if "bills" in q_lower or "invoices" in q_lower:
        params["is_bill_query"] = True

    for ent in doc.ents:
        text = ent.text.lower()
        if ent.label_ == "DATE":
            if "days" in text:
                match = re.search(r'(\d+)\s*days', text)
                if match:
                    days = int(match.group(1))
                    ctx = q_lower[max(0, ent.start_char - 20):ent.start_char]
                    if "next" in ctx or "next" in text:
                        params["date_filter"] = {"type": "next_days", "days": days}
                    elif "last" in ctx or "last" in text or "past" in text or "past" in ctx:
                        params["date_filter"] = {"type": "last_days", "days": days}
                    else:
                        op = "<" if "less" in ctx or "<" in ctx or "under" in ctx or "less" in text else ">"
                        params["age_filter"] = {"operator": op, "days": days}
            elif "week" in text:
                if "this" in text: params["date_filter"] = {"type": "this_week"}
        
        elif ent.label_ in ["MONEY", "CARDINAL"] and not params["amount_filter"]:
            ctx = q_lower[max(0, ent.start_char - 20):ent.start_char]
            if "less" in ctx or "<" in ctx or "under" in ctx:
                op = "<"
            elif "greater" in ctx or ">" in ctx or "more" in ctx or "above" in ctx:
                op = ">"
            else:
                op = None
            
            if op:
                val_str = text.replace(",", "").replace("rs", "").replace("inr", "").replace("₹", "").strip()
                match = re.search(r'([\d\.]+)\s*(k|l|m|cr|lakh)?', val_str)
                if match:
                    num = float(match.group(1))
                    suf = match.group(2)
                    if suf == 'k': num *= 1000
                    elif suf in ['l', 'lakh']: num *= 100000
                    elif suf in ['cr']: num *= 10000000
                    params["amount_filter"] = {"operator": op, "value": num}
                    
    return params

queries = [
    "Oldest 10 Bills which are pending to receive today only above 1L",
    "Payables till date",
    "Identify the top 5 parties to whom the payment is pending for feb 2025",
    "how many customers bills are due in the next 10 days",
    "amount is less than 1L"
]

for q in queries:
    print(f"{q} => {extract_params(q)}")
