import re
import json
import os
import sys

def rewrite():
    with open('nlp_engine.py.bak', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Imports
    if 'import spacy' not in content:
        content = content.replace('import numpy as np', 'import numpy as np\nimport spacy')
        
    # 2. Init
    init_old = """        try:
            model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model')"""
            
    init_new = """        try:
            import spacy
            self.spacy_nlp = spacy.load("en_core_web_sm")
        except Exception as e:
            print(f"Warning: Failed to load spaCy model ({e}).")
            self.spacy_nlp = None
            
        try:
            model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model')"""
            
    content = content.replace(init_old, init_new)

    # 3. resolve_ledger
    # We will replace resolve_ledger completely
    resolve_ledger_old_start = "    def resolve_ledger(self, query, ledgers):"
    resolve_ledger_old_end = "    def get_embedding(self, text):"
    
    start_idx = content.find(resolve_ledger_old_start)
    end_idx = content.find(resolve_ledger_old_end)
    
    resolve_ledger_new = """    def resolve_ledger(self, query, ledgers):
        if not ledgers or not self.spacy_nlp:
            return None, 0.0, []
            
        ledger_names = list(ledgers.keys())
        query_lower = query.lower()
        
        # 1. Exact match
        for name in ledger_names:
            name_lower = name.lower()
            if name_lower in self.common_words or len(name_lower) < 2:
                continue
            pattern = r'\\b' + re.escape(name_lower) + r'\\b'
            try:
                if re.search(pattern, query_lower):
                    return name, 100.0, []
            except re.error:
                if name_lower in query_lower:
                    return name, 100.0, []
                    
        # 2. Extract noun chunks using spaCy
        doc = self.spacy_nlp(query)
        exclude_nouns = {"balance", "amount", "ledger", "account", "outstanding", "dues", "bills", "invoices", "receivables", "payables", "payment", "receipts", "parties", "party", "customers", "customer", "suppliers", "supplier", "vendors", "vendor", "creditors", "creditor", "debtors", "debtor", "all", "which", "show", "give", "list", "total"}
        
        candidate_chunks = []
        for chunk in doc.noun_chunks:
            if chunk.root.text.lower() not in exclude_nouns:
                candidate_chunks.append(chunk.text)
                
        for ent in doc.ents:
            if ent.label_ in ["ORG", "PERSON"]:
                candidate_chunks.append(ent.text)
                
        clean_query = " ".join(set(candidate_chunks)).lower()
        
        if not clean_query:
            return None, 0.0, []
            
        ledger_names_lower = [name.lower() for name in ledger_names]
        matches = process.extract(clean_query, ledger_names_lower, scorer=fuzz.WRatio, limit=2)
        
        if not matches:
            return None, 0.0, []
            
        match1 = matches[0]
        name1_lower, score1, idx1 = match1
        
        if score1 < 85.0:
            return None, score1, []
            
        if len(matches) > 1:
            match2 = matches[1]
            if abs(score1 - match2[1]) <= 5.0 and idx1 != match2[2]:
                return None, score1, [ledger_names[idx1], ledger_names[match2[2]]]
                
        return ledger_names[idx1], score1, []

"""
    content = content[:start_idx] + resolve_ledger_new + content[end_idx:]

    # 4. extract_parameters
    ext_start = "    def extract_parameters(self, query: str) -> dict:"
    ext_end = "    def parse_query(self, query: str):"
    
    start_idx = content.find(ext_start)
    end_idx = content.find(ext_end)
    
    ext_new = """    def extract_parameters(self, query: str) -> dict:
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
        
        if not self.spacy_nlp:
            return params
            
        q_lower = query.lower()
        doc = self.spacy_nlp(query)
        
        # Binary flags & simple keyword limits
        is_cleared = bool(re.search(r'\\b(cleared|settled)\\b', q_lower) or re.search(r'(?<!not )(?<!to be )\\bpaid\\b', q_lower))
        is_pending = bool(re.search(r'\\b(pending|outstanding|unpaid|due|overdue)\\b', q_lower) or "not paid" in q_lower or "to be paid" in q_lower)
        
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
            
        limit_match = re.search(r"(?:top|first|oldest|highest|lowest)\\s+(\\d+)|\\b(\\d+)\\s+(?:top|first|oldest|highest|lowest)\\b", q_lower)
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

        # SPAcy Structural entity extraction
        # 1. Document References (Bills, Vouchers)
        for token in doc:
            if token.text.lower() in ["bill", "invoice", "voucher", "reference", "no", "number"]:
                # Check children
                for child in token.children:
                    if child.pos_ == "NUM" or child.is_digit or re.match(r'^[a-z0-9\\-/\\\\]+$', child.text.lower()):
                        if child.text.lower() not in ["10", "5", "all", "any", "no", "one"]:
                            params["is_bill_query"] = True
                            params["document_ref"] = child.text
                            break
                # Check adjacent
                if not params["is_bill_query"] and token.i + 1 < len(doc):
                    next_token = doc[token.i + 1]
                    if next_token.pos_ == "NUM" or next_token.is_digit or re.match(r'^[a-z0-9\\-/\\\\]+$', next_token.text.lower()):
                        if next_token.text.lower() not in ["amount", "date", "number", "is", "for", "the", "a", "10", "5", "all"]:
                            params["is_bill_query"] = True
                            params["document_ref"] = next_token.text

        # 2. Dates, Ages, Amounts
        for ent in doc.ents:
            text = ent.text.lower()
            if ent.label_ == "DATE":
                if "days" in text:
                    match = re.search(r'(\\d+)\\s*days', text)
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
                ctx = q_lower[max(0, ent.start_char - 20):ent.start_char]
                if "less" in ctx or "<" in ctx or "under" in ctx:
                    op = "<"
                elif "greater" in ctx or ">" in ctx or "more" in ctx or "above" in ctx:
                    op = ">"
                else:
                    op = None
                
                if op:
                    val_str = text.replace(",", "").replace("rs", "").replace("inr", "").replace("₹", "").strip()
                    match = re.search(r'([\\d\\.]+)\\s*(k|l|m|cr|lakh)?', val_str)
                    if match:
                        num = float(match.group(1))
                        suf = match.group(2)
                        if suf == 'k': num *= 1000
                        elif suf in ['l', 'lakh']: num *= 100000
                        elif suf in ['cr']: num *= 10000000
                        params["amount_filter"] = {"operator": op, "value": num}
                        
        # 3. Explicit Reference Dates (Still easier with regex since it's rigid)
        ref_match = re.search(r"(?:on|as of|as on|till)\\s+(\\d{1,2})[-/\\s]+(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)[a-z]*[-/\\s]+(\\d{4})", q_lower)
        numeric_ref_match = re.search(r"(?:on|as of|as on|till)\\s+(\\d{1,2})[-/\\s]+(\\d{1,2})[-/\\s]+(\\d{4})", q_lower)
        if ref_match:
            try:
                day = int(ref_match.group(1))
                month_str = ref_match.group(2)[:3].title()
                year = int(ref_match.group(3))
                params["reference_date"] = f"{day:02d}-{month_str}-{year}"
            except: pass
        elif numeric_ref_match:
            try:
                day = int(numeric_ref_match.group(1))
                month_idx = int(numeric_ref_match.group(2))
                year = int(numeric_ref_match.group(3))
                month_map = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 
                             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
                if month_idx in month_map:
                    params["reference_date"] = f"{day:02d}-{month_map[month_idx]}-{year}"
            except: pass

        return params

"""
    content = content[:start_idx] + ext_new + content[end_idx:]

    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)

rewrite()
