import re

def apply():
    with open('nlp_engine.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove import spacy
    content = content.replace("import spacy\n", "")
    
    # 2. Remove spacy load in __init__
    init_spacy_regex = r"        try:\n            import spacy\n            self\.spacy_nlp = spacy\.load\(\"en_core_web_sm\"\)\n        except Exception as e:\n            print\(f\"Warning: Failed to load spaCy model \(\{e\}\)\.\"\)\n            self\.spacy_nlp = None\n"
    content = re.sub(init_spacy_regex, "", content)
    
    # 3. Replace resolve_ledger
    resolve_ledger_regex = r"    def resolve_ledger\(self, query, ledgers\):.*?return ledger_names\[idx1\], score1, \[\]\n"
    new_resolve_ledger = """    def resolve_ledger(self, query, ledgers):
        if not ledgers:
            return None, 0.0, []
            
        ledger_names = list(ledgers.keys())
        query_lower = query.lower()
        
        # 1. Exact match fast-path
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
                    
        # 2. Sliding window n-gram match
        common = {"what", "is", "the", "balance", "of", "show", "me", "how", "much", "does", "owe", 
                  "amount", "for", "party", "invoices", "pending", "from", "ledger", "account", "due", "receivables"}
                  
        q_clean = re.sub(r'[^a-zA-Z0-9\\s]', '', query_lower)
        words = q_clean.split()
        
        windows = []
        for n in range(1, 5):
            for i in range(len(words) - n + 1):
                window = " ".join(words[i:i+n])
                if all(w in common for w in words[i:i+n]):
                    continue
                if len(window) < 3:
                    continue
                windows.append(window)
                
        if not windows:
            return None, 0.0, []
            
        ledger_names_lower = [name.lower() for name in ledger_names]
        
        best_match = None
        best_score = 0
        best_idx = -1
        
        for window in windows:
            matches = process.extract(window, ledger_names_lower, scorer=fuzz.WRatio, limit=2)
            if matches:
                score = matches[0][1]
                idx = matches[0][2]
                if score > best_score:
                    best_score = score
                    best_match = matches[0][0]
                    best_idx = idx
                    
        if best_score < 85.0:
            return None, best_score, []
            
        return ledger_names[best_idx], best_score, []
"""
    content = re.sub(resolve_ledger_regex, new_resolve_ledger, content, flags=re.DOTALL)
    
    with open('nlp_engine.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Applied Phase 7 changes to nlp_engine.py")

if __name__ == '__main__':
    apply()
