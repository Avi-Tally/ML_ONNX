import json
import os
import pandas as pd

# 1. Read 727 queries from test_suite_expected.json
with open('test_suite_expected.json', 'r', encoding='utf-8') as f:
    suite_727 = json.load(f)

queries_727 = [item['query'] for item in suite_727 if 'query' in item]
print(f"Loaded {len(queries_727)} queries from test_suite_expected.json")

# 2. Read 482 queries from Excel
df = pd.read_excel(r'Real_world_queries\482 suite.xlsx')
queries_482 = df['Queries'].dropna().tolist()
print(f"Loaded {len(queries_482)} queries from 482 suite.xlsx")

# 3. Combine them
all_queries_text = queries_727 + queries_482
print(f"Total combined queries: {len(all_queries_text)}")

# 4. Format them into expected schema for run_live_batch_test.py
formatted_queries = []
for i, q_text in enumerate(all_queries_text, 1):
    # Ensure it is a string and handle any potential newlines/spaces
    clean_text = str(q_text).strip().replace('\n', ' ')
    formatted_queries.append({
        "id": i,
        "original_query": clean_text,
        "live_adapted_query": clean_text
    })

# 5. Save in batches of 100
os.makedirs("scratch/batches", exist_ok=True)
batch_size = 100
batch_num = 1

for i in range(0, len(formatted_queries), batch_size):
    batch = formatted_queries[i:i + batch_size]
    batch_file = f"scratch/batches/batch_{batch_num:02d}.json"
    with open(batch_file, "w", encoding="utf-8") as f:
        json.dump(batch, f, indent=2)
    print(f"Saved {len(batch)} queries to {batch_file}")
    batch_num += 1

print("\nAll batches generated successfully. Ready for live testing when instructed.")
