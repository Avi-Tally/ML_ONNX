import json

def align_conceptual():
    path = "scratch/augmented_training_data.json"
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    conceptual_keywords = [
        "receivable ageing getting worse",
        "overdue receivables increasing this financial year",
        "payable trends indicate delayed vendor",
        "collection efficiency improving",
        "outstanding receivables unusually high",
        "too many old pending bills in sundry debtors",
        "becoming more dependent on a few customers",
        "overdue bills concentrated within a specific",
        "net outstanding position improving"
    ]
    
    updated = 0
    for q in data:
        query = q["query"].lower()
        if any(kw in query for kw in conceptual_keywords):
            if q["intent"] != "UNKNOWN":
                print(f"Aligning conceptual query: '{q['query']}' | Old intent: {q['intent']} -> New: UNKNOWN")
                q["intent"] = "UNKNOWN"
                updated += 1
                
    if updated > 0:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f"Successfully aligned {updated} conceptual query intents to UNKNOWN.")
    else:
        print("No conceptual queries needed alignment.")

if __name__ == "__main__":
    align_conceptual()
