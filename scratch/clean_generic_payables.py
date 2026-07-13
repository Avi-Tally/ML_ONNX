import json

def clean_generic():
    path = "scratch/augmented_training_data.json"
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    updated = 0
    for q in data:
        query = q["query"].lower()
        old_intent = q["intent"]
        
        correct_intent = None
        if "bills i owe" in query or "bills to pay" in query or "payments i have to make" in query or "payments to make" in query or "payments i owe" in query:
            correct_intent = "GET_PAYABLES"
            
        if correct_intent and old_intent != correct_intent:
            q["intent"] = correct_intent
            updated += 1
            print(f"Updated: '{q['query']}' | Old: {old_intent} -> New: {correct_intent}")
            
    if updated > 0:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f"Done. Cleaned {updated} generic payable queries.")
    else:
        print("No queries needed cleaning.")

if __name__ == "__main__":
    clean_generic()
