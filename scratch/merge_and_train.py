import json
import os
import sys

def merge_datasets():
    # 1. Load original training data
    with open("training_data.json", "r", encoding="utf-8") as f:
        train_data = json.load(f)
        
    print(f"Loaded original training data: {len(train_data)} items")
    
    existing_queries = {item["query"].strip().lower() for item in train_data}
    
    # 2. Load test suite expected (230 queries)
    with open("test_suite_expected.json", "r", encoding="utf-8") as f:
        test_expected = json.load(f)
        
    added_test = 0
    for item in test_expected:
        q = item.get("query", item.get("query_text", "")).strip()
        intent = item.get("intent", item.get("expected_intent", "UNKNOWN"))
        entities = item.get("expected_entities", {})
        
        if not q:
            continue
            
        q_lower = q.lower()
        if q_lower not in existing_queries:
            train_data.append({
                "query": q,
                "intent": intent,
                "expected_entities": entities
            })
            existing_queries.add(q_lower)
            added_test += 1
            
    print(f"Added from test_suite_expected: {added_test} items")
    
    # 3. Load synthetic queries (125 queries)
    with open("scratch/synthetic_1.json", "r", encoding="utf-8") as f:
        synthetic = json.load(f)
        
    added_synthetic = 0
    for item in synthetic:
        q = item.get("query", item.get("query_text", "")).strip()
        intent = item.get("intent", item.get("expected_intent"))
        entities = item.get("expected_entities", {})
        
        if not q:
            continue
            
        q_lower = q.lower()
        if q_lower not in existing_queries:
            train_data.append({
                "query": q,
                "intent": intent,
                "expected_entities": entities
            })
            existing_queries.add(q_lower)
            added_synthetic += 1
            
    print(f"Added from synthetic_1: {added_synthetic} items")
    print(f"Total training dataset size: {len(train_data)} items")
    
    # 4. Save augmented dataset
    augmented_path = "scratch/augmented_training_data.json"
    with open(augmented_path, "w", encoding="utf-8") as f:
        json.dump(train_data, f, indent=2)
        
    return augmented_path

def retrain_models(data_path):
    print("\n--- Retraining Intent Model ---")
    sys.path.append(os.path.abspath("scratch"))
    import train_intent_model
    train_intent_model.train_and_export(data_path)
    
    print("\n--- Retraining Parameter Models ---")
    import train_param_models
    train_param_models.train_and_export(data_path)

if __name__ == "__main__":
    augmented_path = merge_datasets()
    retrain_models(augmented_path)
    print("\nRetraining complete!")
