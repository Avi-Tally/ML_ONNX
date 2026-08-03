import json
import os

batch_dir = "scratch/batches"
for filename in sorted(os.listdir(batch_dir)):
    if not filename.endswith(".json"):
        continue
        
    filepath = os.path.join(batch_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        batch = json.load(f)
        
    for item_data in batch:
        # Revert the adapted query back to the original
        item_data["live_adapted_query"] = item_data["original_query"]
        
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(batch, f, indent=2)
        
print("Reverted all adapted queries back to original queries.")
