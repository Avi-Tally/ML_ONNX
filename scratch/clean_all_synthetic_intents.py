import json

def clean_all_intents():
    path = "scratch/augmented_training_data.json"
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    updated = 0
    
    creditor_groups = [
        "acme corp", "delta cargo", "global traders", "reliance industries", "tcs", 
        "wipro", "thermax ltd", "jagat", "v trans (india) ltd.", "sundry creditors", 
        "creditors", "hardware suppliers", "group expenses", "key vendors", "local suppliers"
    ]
    
    debtor_groups = [
        "john doe", "sunrise industries", "tech solutions", "chemical process pvt ltd", 
        "aquatech system", "sukan engineering", "dew cargo", "sundry debtors", 
        "debtors", "retailers", "wholesalers"
    ]
    
    for q in data:
        query = q["query"].lower()
        old_intent = q["intent"]
        
        # We only want to clean synthetic/generated queries, not the real-world ones from test_suite_expected!
        # Wait, the real-world queries in test_suite_expected.json are also in augmented_training_data.json.
        # But we want the ground truth of the dataset to be logically correct and consistent.
        
        # Let's check if the query contains top debtors/creditors specifiers:
        is_top_debtors_query = "debtor" in query or "debtors" in query or "customer" in query or "customers" in query
        is_top_creditors_query = "creditor" in query or "creditors" in query or "supplier" in query or "suppliers" in query or "vendor" in query or "vendors" in query
        
        # Check if the query is a report on the group's own bills (not nested top debtors/creditors)
        is_group_report = not ("debtors from" in query or "creditors from" in query or "debtor from" in query or "creditor from" in query or "customers from" in query or "suppliers from" in query or "vendors from" in query)
        
        correct_intent = None
        if is_group_report:
            # Match group to its logical intent
            if any(g in query for g in creditor_groups):
                if old_intent == "GET_RECEIVABLES":
                    correct_intent = "GET_PAYABLES"
                elif old_intent == "GET_TOP_DEBTORS":
                    correct_intent = "GET_TOP_CREDITORS"
            elif any(g in query for g in debtor_groups):
                if old_intent == "GET_PAYABLES":
                    correct_intent = "GET_RECEIVABLES"
                elif old_intent == "GET_TOP_CREDITORS":
                    correct_intent = "GET_TOP_DEBTORS"
            else:
                # Default to receivables for generic bills/dues status comparison
                if any(w in query for w in ["unpaid bills", "unpaid dues", "cleared vs pending", "cleared dues", "settled bills", "pending vs paid", "pending balances", "settled accounts", "unpaid bill"]):
                    if not any(g in query for g in creditor_groups + debtor_groups):
                        correct_intent = "GET_RECEIVABLES"
        # Apply special corrections for nested top queries:
        # e.g., "debtors from Key Vendors" -> GET_TOP_DEBTORS
        if "debtors from" in query or "debtor from" in query:
            if old_intent != "GET_TOP_DEBTORS":
                correct_intent = "GET_TOP_DEBTORS"
        elif "creditors from" in query or "creditor from" in query or "suppliers from" in query or "vendors from" in query:
            if old_intent != "GET_TOP_CREDITORS":
                correct_intent = "GET_TOP_CREDITORS"
                
        if correct_intent and old_intent != correct_intent:
            q["intent"] = correct_intent
            updated += 1
            print(f"Updated: '{q['query']}' | Old: {old_intent} -> New: {correct_intent}")
            
    if updated > 0:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f"Done. Cleaned {updated} total intent labels.")
    else:
        print("No labels needed updating.")

if __name__ == "__main__":
    clean_all_intents()
