import json

with open('scratch/batches/batch_08.json', 'r', encoding='utf-8') as f:
    batch = json.load(f)

for q in batch:
    print(f"{q['id']}: {q['original_query']}")
