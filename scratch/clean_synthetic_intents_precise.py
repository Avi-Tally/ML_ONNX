import json

def clean_intents_precise():
    path = "scratch/augmented_training_data.json"
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    updated = 0
    for q in data:
        query = q["query"].lower()
        old_intent = q["intent"]
        
        # Only target status-conflict queries (Synthetic 2)
        has_opposing_status = ("cleared" in query or "settled" in query or "paid" in query) and ("pending" in query or "unpaid" in query or "overdue" in query or "dues" in query or "balance" in query)
        
        if has_opposing_status and old_intent in ["GET_RECEIVABLES", "GET_PAYABLES"]:
            correct_intent = None
            if any(p in query for p in ["acme corp", "delta cargo", "global traders"]):
                correct_intent = "GET_PAYABLES"
            elif any(p in query for p in ["sunrise industries", "tech solutions"]):
                correct_intent = "GET_RECEIVABLES"
            elif "customer" in query or "debtor" in query or "receive" in query:
                correct_intent = "GET_RECEIVABLES"
            elif "supplier" in query or "creditor" in query or "vendor" in query or "pay" in query:
                correct_intent = "GET_PAYABLES"
                
            if correct_intent and old_intent != correct_intent:
                q["intent"] = correct_intent
                updated += 1
                print(f"Updated: '{q['query']}' | Old: {old_intent} -> New: {correct_intent}")
                
    if updated > 0:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f"Done. Cleaned {updated} status-conflict intent labels.")
    else:
        print("No labels needed updating.")

if __name__ == "__main__":
    clean_intents_precise()
