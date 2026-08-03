import json

with open('scratch/batches/batch_12.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('scratch/sampled_masters.json', 'r', encoding='utf-8') as f:
    masters = json.load(f)

print("Sampled Ledgers:", masters['ledgers'][:10])
print("Sampled Stock Items:", masters['stock_items'][:10])
print("Sampled Godowns:", masters['godowns'][:10])
print("--- Queries ---")
for item in data:
    print(f"{item['id']}: {item['original_query']}")
