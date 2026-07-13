import json

def clean_intents():
    path = "scratch/augmented_training_data.json"
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    updated = 0
    for q in data:
        query = q["query"].lower()
        old_intent = q["intent"]
        
        # Determine correct intent based on party / default rules
        correct_intent = None
        if any(p in query for p in ["acme corp", "delta cargo", "global traders"]):
            correct_intent = "GET_PAYABLES"
        elif any(p in query for p in ["sunrise industries", "tech solutions"]):
            correct_intent = "GET_RECEIVABLES"
        elif "payable" in query or "pay" in query or "owe" in query or "creditor" in query or "supplier" in query or "vendor" in query:
            correct_intent = "GET_PAYABLES"
        elif "receivable" in query or "receive" in query or "debtor" in query or "customer" in query:
            correct_intent = "GET_RECEIVABLES"
        else:
            # Default to receivables for generic bills/dues status comparison
            if "unpaid bills marked as cleared" in query or "unpaid dues that were cleared" in query or "cleared vs pending" in query or "cleared dues showing as pending" in query or "settled bills with overdue" in query:
                correct_intent = "GET_RECEIVABLES"
                
        if correct_intent and old_intent != correct_intent:
            q["intent"] = correct_intent
            updated += 1
            print(f"Updated: '{q['query']}' | Old: {old_intent} -> New: {correct_intent}")
            
    if updated > 0:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f"Done. Cleaned {updated} intent labels.")
    else:
        print("No labels needed updating.")

if __name__ == "__main__":
    clean_intents()
