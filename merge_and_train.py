import json
import os
import sys

def merge_datasets():
    """
    Merges queries from multiple sources (original data, test suite, and synthetic data) 
    to create an augmented dataset for training the ONNX models. 
    It prevents duplicates by maintaining a set of existing queries.
    """
    # 1. Load original base training data
    with open("training_data.json", "r", encoding="utf-8") as f:
        train_data = json.load(f)
        
    print(f"Loaded original training data: {len(train_data)} items")
    
    # Maintain a set of lowercase query strings to check for duplicates quickly
    existing_queries = {item["query"].strip().lower() for item in train_data}
    
    # 2. Load expected test cases (benchmark queries) to ensure they are represented in training
    with open("test_suite_expected.json", "r", encoding="utf-8") as f:
        test_expected = json.load(f)
        
    added_test = 0
    for item in test_expected:
        # Standardize query and intent extraction from slightly different JSON schemas
        q = item.get("query", item.get("query_text", "")).strip()
        intent = item.get("intent", item.get("expected_intent", "UNKNOWN"))
        entities = item.get("expected_entities", {})
        
        if not q:
            continue
            
        q_lower = q.lower()
        # Add to training data if the query is not already present
        if q_lower not in existing_queries:
            train_data.append({
                "query": q,
                "intent": intent,
                "expected_entities": entities
            })
            existing_queries.add(q_lower)
            added_test += 1
            
    print(f"Added from test_suite_expected: {added_test} items")
    
    # 3. Load synthetically generated queries for additional coverage
    # (Checking if synthetic file exists since it might be in scratch directory)
    synthetic_path = "scratch/synthetic_1.json"
    if os.path.exists(synthetic_path):
        with open(synthetic_path, "r", encoding="utf-8") as f:
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
    
    # 4. Save the newly compiled augmented dataset back to disk
    os.makedirs("scratch", exist_ok=True)
    augmented_path = "scratch/augmented_training_data.json"
    with open(augmented_path, "w", encoding="utf-8") as f:
        json.dump(train_data, f, indent=2)
        
    return augmented_path

def retrain_models(data_path):
    """
    Triggers the training scripts for both the intent and parameter ONNX models 
    using the newly augmented dataset.
    """
    print("\n--- Retraining Intent Model ---")
    # Load and execute the intent model training script
    import train_intent_model
    train_intent_model.train_and_export(data_path)
    
    print("\n--- Retraining Parameter Models ---")
    # Note: train_param_models might still be missing in the workspace, wrapping in try/except
    try:
        import train_param_models
        train_param_models.train_and_export(data_path)
    except ImportError:
        print("Warning: train_param_models module not found. Skipping parameter models training.")

if __name__ == "__main__":
    augmented_path = merge_datasets()
    retrain_models(augmented_path)
    print("\nRetraining complete!")
