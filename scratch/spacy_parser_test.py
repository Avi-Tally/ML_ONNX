import spacy
import re
from rapidfuzz import process, fuzz

nlp = spacy.load("en_core_web_sm")

def extract_params(query):
    doc = nlp(query.lower())
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
    
    # 1. Structural Document Ref Extraction
    for token in doc:
        if token.text in ["bill", "invoice", "voucher", "reference", "no", "number"]:
            # Check children
            for child in token.children:
                if child.pos_ == "NUM" or child.is_digit or re.match(r'^[a-z0-9\-/\\]+$', child.text):
                    if child.text not in ["10", "5", "all", "any", "no", "one"]:
                        params["is_bill_query"] = True
                        params["document_ref"] = child.text
                        break
            # Check adjacent
            if not params["is_bill_query"] and token.i + 1 < len(doc):
                next_token = doc[token.i + 1]
                if next_token.pos_ == "NUM" or next_token.is_digit or re.match(r'^[a-z0-9\-/\\]+$', next_token.text):
                    if next_token.text not in ["amount", "date", "number", "is", "for", "the", "a", "10", "5", "all"]:
                        params["is_bill_query"] = True
                        params["document_ref"] = next_token.text
                        
    # 2. Status & Aggregations (Keep simple regex/keyword for these since they are binary flags)
    q_lower = query.lower()
    is_cleared = bool(re.search(r'\b(cleared|settled)\b', q_lower) or re.search(r'(?<!not )(?<!to be )\bpaid\b', q_lower))
    is_pending = bool(re.search(r'\b(pending|outstanding|unpaid|due|overdue)\b', q_lower) or "not paid" in q_lower or "to be paid" in q_lower)
    
    if is_pending and is_cleared:
        params["status_filter"] = None
    elif is_pending:
        params["status_filter"] = "pending"
    elif is_cleared:
        params["status_filter"] = "cleared"
        
    params["count_only"] = "how many" in q_lower or "count" in q_lower
    params["sum_only"] = "total value" in q_lower or "total amount" in q_lower or "sum" in q_lower
    
    if any(w in q_lower for w in ["due", "payment", "overdue", "late", "outstanding", "pending to receive", "pending to pay"]):
        params["date_target"] = "due_date"
        
    limit_match = re.search(r"(?:top|first|oldest|highest|lowest)\s+(\d+)|\b(\d+)\s+(?:top|first|oldest|highest|lowest)\b", q_lower)
    if limit_match:
        params["limit"] = int(limit_match.group(1) or limit_match.group(2))
        
    if "oldest" in q_lower or "ascending" in q_lower:
        if "bill date" in q_lower or "billdate" in q_lower:
            params["sort"] = {"field": "bill_date", "order": "asc"}
        else:
            params["sort"] = {"field": params["date_target"], "order": "asc"}
    elif "highest" in q_lower or "largest" in q_lower:
        params["sort"] = {"field": "amount", "order": "desc"}
        if not params["limit"]:
            params["limit"] = 10

    # Date and Age from Entities
    for ent in doc.ents:
        if ent.label_ == "DATE":
            text = ent.text
            if "days" in text:
                match = re.search(r'(\d+)\s*days', text)
                if match:
                    days = int(match.group(1))
                    ctx = q_lower[max(0, ent.start_char - 20):ent.start_char]
                    if "next" in ctx:
                        params["date_filter"] = {"type": "next_days", "days": days}
                    elif "last" in ctx:
                        params["date_filter"] = {"type": "last_days", "days": days}
                    else:
                        op = "<" if "less" in ctx or "<" in ctx or "under" in ctx else ">"
                        params["age_filter"] = {"operator": op, "days": days}
            elif "week" in text:
                if "this" in text: params["date_filter"] = {"type": "this_week"}
            elif "today" in text:
                params["date_filter"] = {"type": "till_today" if "till" in q_lower else "today"}

        elif ent.label_ in ["MONEY", "CARDINAL"]:
            # Check context for < or >
            ctx = q_lower[max(0, ent.start_char - 20):ent.start_char]
            op = "<" if "less" in ctx or "<" in ctx or "under" in ctx else ">"
            # parse numeric val
            val_str = ent.text.replace(",", "").replace("rs", "").replace("inr", "").strip()
            match = re.search(r'([\d\.]+)\s*(k|l|m|cr|lakh)?', val_str)
            if match:
                num = float(match.group(1))
                suf = match.group(2)
                if suf == 'k': num *= 1000
                elif suf in ['l', 'lakh']: num *= 100000
                elif suf in ['cr']: num *= 10000000
                params["amount_filter"] = {"operator": op, "value": num}
                
    return params

def extract_ledger(query, ledger_names):
    doc = nlp(query)
    exclude_nouns = {"balance", "amount", "ledger", "account", "outstanding", "dues", "bills", "invoices", "receivables", "payables", "payment", "receipts", "parties", "party", "customers", "customer", "suppliers", "supplier", "vendors", "vendor", "creditors", "creditor", "debtors", "debtor"}
    
    candidate_chunks = []
    for chunk in doc.noun_chunks:
        # Ignore chunks if their root is a generic financial word
        if chunk.root.text.lower() not in exclude_nouns:
            candidate_chunks.append(chunk.text)
            
    # Add ORG and PERSON entities directly
    for ent in doc.ents:
        if ent.label_ in ["ORG", "PERSON"]:
            candidate_chunks.append(ent.text)
            
    clean_query = " ".join(candidate_chunks)
    
    if not clean_query:
        return None
        
    matches = process.extract(clean_query, [n.lower() for n in ledger_names], scorer=fuzz.WRatio, limit=1)
    if matches and matches[0][1] >= 90:
        return ledger_names[matches[0][2]]
    return None

queries = [
    "What is the total pending amount for Chemical Process Pipping Pvt Ltd for bill number MODI/25-26/956",
    "List the parties to whom I need to make the payment this week",
    "Customer dues and settled bills with over due amount less than 55000",
    "Total cleared bills for Reliance Industries Ltd.",
]

mock_ledgers = ["Chemical Process Pipping Pvt Ltd", "Reliance Industries Ltd.", "Customer"]

for q in queries:
    print(f"\nQuery: {q}")
    params = extract_params(q)
    ledger = extract_ledger(q, mock_ledgers)
    print("Params:", params)
    print("Ledger:", ledger)

