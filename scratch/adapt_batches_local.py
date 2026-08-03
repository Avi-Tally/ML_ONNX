import json
import os
import random
import re

# Load sampled masters
with open("scratch/sampled_masters.json", "r", encoding="utf-8") as f:
    masters = json.load(f)

ledgers = masters.get("ledgers", [])
items = masters.get("stock_items", [])
godowns = masters.get("godowns", [])

# Generic terms to replace
generic_parties = [r"\bcustomer\b", r"\bcustomers\b", r"\bvendor\b", r"\bvendors\b", 
                   r"\bsupplier\b", r"\bsuppliers\b", r"\bparty\b", r"\bparties\b",
                   r"\bdebtor\b", r"\bdebtors\b", r"\bcreditor\b", r"\bcreditors\b",
                   r"Acme", r"John Doe", r"XYZ", r"ABC", r"Reliance Industries Ltd", 
                   r"Infosys Ltd", r"Jagat", r"Thermax Ltd", r"Chemical Process Pvt LTD",
                   r"Rashmi Traders", r"AquaTech system", r"Anand Cargo", r"Dew Cargo", 
                   r"DeltaFlow", r"Relaxo", r"CECO", r"Sun Enterprises", r"Dew Impex", r"Agru"]

generic_godowns = [r"\bwarehouse\b", r"\bgodown\b", r"Bhiwandi Godown", r"Main Godown"]

batch_dir = "scratch/batches"
for filename in sorted(os.listdir(batch_dir)):
    if not filename.endswith(".json"):
        continue
        
    filepath = os.path.join(batch_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        batch = json.load(f)
        
    for item_data in batch:
        q = item_data["original_query"]
        adapted = q
        
        # Replace generic parties with random valid ledgers
        if ledgers:
            for pattern in generic_parties:
                if re.search(pattern, adapted, flags=re.IGNORECASE):
                    replacement = random.choice(ledgers)
                    adapted = re.sub(pattern, replacement, adapted, flags=re.IGNORECASE)
                    
        # Replace generic godowns with valid godowns
        if godowns:
            for pattern in generic_godowns:
                if re.search(pattern, adapted, flags=re.IGNORECASE):
                    replacement = random.choice(godowns)
                    adapted = re.sub(pattern, replacement, adapted, flags=re.IGNORECASE)
                    
        item_data["live_adapted_query"] = adapted
        
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(batch, f, indent=2)
        
print("Successfully adapted all 13 batches using local heuristic replacement.")
