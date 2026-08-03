import json
import re

# Load sampled masters
with open("scratch/sampled_masters.json", "r", encoding="utf-8") as f:
    sampled_masters = json.load(f)

# Load batch 13
with open("scratch/batches/batch_13.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

substitutions = {
    1201: [("Om Stell Traders", "RAJKAMAL TRADING CO.")],
    1202: [("OM Stell Traders", "MAHAVIR TEX-FAB.")],
    1203: [("Laxmi Traders", "STAR ENTERPRISES"), ("'Raj Company Pvt Ltd'", "'JANAK HANDLOOM PVT LTD (PANIPAT)'")],
    1204: [("Lakshmi Traders", "MITTAL FURNISHING")],
    1205: [],
    1206: [("Young India Stell corporation", "GOVIND EXPORTS")],
    1207: [("Sona Steel enterprises", "HARISH TEXTILE (AHMEDABAD)")],
    1208: [],
    1209: [("Mr Nirman Timbers", "Dinesh Choudhary")]
}

for item in batch:
    qid = item["id"]
    query_str = item["original_query"]
    adapted = query_str
    if qid in substitutions:
        for old_val, new_val in substitutions[qid]:
            adapted = adapted.replace(old_val, new_val)
    item["live_adapted_query"] = adapted
    print(f"ID {qid}:")
    print(f"  Original: {item['original_query']}")
    print(f"  Adapted:  {item['live_adapted_query']}")

# Save back to batch_13.json
with open("scratch/batches/batch_13.json", "w", encoding="utf-8") as f:
    json.dump(batch, f, indent=2)

print("\nSuccessfully updated scratch/batches/batch_13.json")
