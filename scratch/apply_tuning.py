import os

def rewrite():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = "    def extract_parameters(self, query: str) -> dict:"
    end_str = "    def parse_query(self, query: str):"
    
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    new_ext = """    def extract_parameters(self, query: str) -> dict:
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
        normalized_query = query.replace("₹", "Rs ")
        doc = self.spacy_nlp(normalized_query)
        
        # Binary flags & simple keyword limits
        is_cleared = bool(re.search(r'\\b(cleared|settled)\\b', q_lower) or re.search(r'(?<!not )(?<!to be )\\bpaid\\b', q_lower))
        is_pending = bool(re.search(r'\\b(pending|outstanding|unpaid|due|overdue)\\b', q_lower) or "not paid" in q_lower or "to be paid" in q_lower)
        
        if is_pending and is_cleared:
            params["status_filter"] = None
        elif is_pending:
            params["status_filter"] = "pending"
        elif is_cleared:
            params["status_filter"] = "cleared"
            
        params["count_only"] = "how many" in q_lower or bool(re.search(r'\\bcount\\b', q_lower))
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

        # Custom date/amount extractors for stability
        if "till date" in q_lower or "today" in q_lower:
            if "pending" in q_lower or "till" in q_lower or "payable" in q_lower or "receivable" in q_lower or "due" in q_lower:
                params["date_filter"] = {"type": "till_today"}
            else:
                params["date_filter"] = {"type": "today"}

        my_match = re.search(r'\\b(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)\\s+(\\d{4})\\b', q_lower)
        if my_match:
            month_str = my_match.group(1)[:3].title()
            month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
            params["date_filter"] = {"type": "month_year", "month": month_map[month_str], "year": int(my_match.group(2))}

        amt_match = re.search(r'(less than|<|under|more than|>|above)\\s*(?:rs|inr|₹)?\\s*([\\d\\.]+)\\s*(k|l|lakh|cr|m)?\\b', q_lower)
        if amt_match:
            op_str = amt_match.group(1)
            val = float(amt_match.group(2))
            suf = amt_match.group(3)
            op = "<" if "less" in op_str or "<" in op_str or "under" in op_str else ">"
            if suf == 'k': val *= 1000
            elif suf in ['l', 'lakh']: val *= 100000
            elif suf in ['cr']: val *= 10000000
            params["amount_filter"] = {"operator": op, "value": val}

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

        if "bills" in q_lower or "invoices" in q_lower:
            params["is_bill_query"] = True

        # 2. Dates, Ages, Amounts (Fallback if regex missed)
        for ent in doc.ents:
            text = ent.text.lower()
            if ent.label_ == "DATE":
                if "days" in text:
                    match = re.search(r'(\\d+)\\s*days', text)
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
    content = content[:start_idx] + new_ext + content[end_idx:]
    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    rewrite()
