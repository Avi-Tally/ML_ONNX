import re

def strip_spacy():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Remove "if not self.spacy_nlp: return params" and "doc = self.spacy_nlp..."
    spacy_init_block = r"        if not self\.spacy_nlp:\n            return params\n\n        q_lower = query\.lower\(\)\n        normalized_query = query\.replace\(\"₹\", \"Rs \"\)\n        doc = self\.spacy_nlp\(normalized_query\)"
    content = re.sub(spacy_init_block, "        q_lower = query.lower()\n        normalized_query = query.replace(\"₹\", \"Rs \")", content, flags=re.MULTILINE)
    
    # 2. Replace SPAcy Structural entity extraction completely with Regex for document_ref
    spacy_struct_block = r"        # SPAcy Structural entity extraction\n        # 1\. Document References \(Bills, Vouchers\).*?# 3\. Document Reference fallback\n        document_ref = params\.get\(\"document_ref\", None\)"
    
    new_doc_ref = """        # Regex for Document References
        match = re.search(r'\\b(?:bill|invoice|voucher|reference|no\\.?|number)\\s+(?:no\\.?\\s*)?([a-z0-9\\-/\\\\]+)\\b', q_lower)
        if match:
            doc_id = match.group(1)
            if doc_id not in ["10", "5", "all", "any", "no", "one"] and bool(re.search(r'\\d', doc_id)):
                params["is_bill_query"] = True
                params["document_ref"] = doc_id

        if not use_ml_is_bill:
            if "bills" in q_lower or "invoices" in q_lower or "bill amount" in q_lower or "receivable bill" in q_lower or "payable bill" in q_lower or "collections due" in q_lower:
                params["is_bill_query"] = True
            elif bool(re.search(r'\\b(?:oldest|latest|pending|unpaid|highest|lowest|which|overdue date|receivables|payables)\\s+bill\\b', q_lower)) or "bill amount" in q_lower:
                params["is_bill_query"] = True
                
            if params["is_bill_query"] and not params["document_ref"]:
                if bool(re.search(r'\\b(parties|debtors|creditors|payments)\\b', q_lower)):
                    if not bool(re.search(r'\\b(list|show|all).*bills\\b', q_lower)) and not bool(re.search(r'oldest.*bill', q_lower)) and "bill amount" not in q_lower:
                        params["is_bill_query"] = False

        # 3. Document Reference fallback
        document_ref = params.get("document_ref", None)"""
    
    content = re.sub(spacy_struct_block, new_doc_ref, content, flags=re.DOTALL)
    
    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Done stripping spaCy from parameters")

if __name__ == '__main__':
    strip_spacy()
