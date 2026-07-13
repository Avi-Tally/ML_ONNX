import re
from rapidfuzz import process, fuzz

def extract_ledger_sliding_window(query, known_ledgers):
    # Common words to ignore when forming windows
    common = {"what", "is", "the", "balance", "of", "show", "me", "how", "much", "does", "owe", 
              "amount", "for", "party", "invoices", "pending", "from", "ledger", "account", "due", "receivables"}
              
    # Clean query
    q = re.sub(r'[^a-zA-Z0-9\s]', '', query.lower())
    words = q.split()
    
    # Generate all n-grams (1 to 4 words)
    windows = []
    for n in range(1, 5):
        for i in range(len(words) - n + 1):
            window = " ".join(words[i:i+n])
            # If all words in window are common, skip
            if all(w in common for w in words[i:i+n]):
                continue
            # If window is too short
            if len(window) < 3:
                continue
            windows.append(window)
            
    best_match = None
    best_score = 0
    
    for window in windows:
        matches = process.extract(window, known_ledgers, scorer=fuzz.WRatio, limit=1)
        if matches:
            score = matches[0][1]
            if score > best_score:
                best_score = score
                best_match = matches[0][0]
                
    return best_match, best_score

known = [
    "sundry debtors", "sundry creditors", "aquatech system", "thermax ltd", 
    "jagat", "chemical process pvt ltd", "abhishek", "supreme", "varad engineers",
    "modichem company", "reliance industries ltd", "infosys ltd", "expenses",
    "credit card expenses"
]

queries = [
    "Show highest pending and cleared receivables bill amount for sundry debtors also give their GST status?",
    "highest receivable amount for creditors with overdue days less than a month",
    "Display the last 7 days due outstanding of debtors",
    "For Aquatech system, how many overdue bills are available till date",
    "Show me the overdue bills of the party AquaTech system",
    "Show me all invoices pending from Thermax Ltd",
    "Amount of Bill no 308 for Abhishek and give the tax amount",
    "List all the pending receivable bills number for Chemical Process Pvt LTD",
    "What is the payment status of Bill Number 1027 under Ledger Supreme ?",
    "Give adjustment summary for Reliance Industries Ltd and Infosys Ltd"
]

for q in queries:
    match, score = extract_ledger_sliding_window(q, known)
    print(f"Q: {q[:40]}... -> {match} (Score: {score})")
