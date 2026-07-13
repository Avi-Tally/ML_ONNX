import json
import os

with open('scratch/synthetic_1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

md = "# 125 Complex Synthetic Queries\n\n"
for i, item in enumerate(data):
    md += f"**{i+1}. {item['query']}**\n"
    md += f"- Intent: `{item.get('intent', item.get('expected_intent'))}`\n"
    md += f"- Expected Params: `{json.dumps(item['expected_entities'])}`\n\n"

# Write to artifact dir
artifact_path = r"C:\Users\avija\.gemini\antigravity\brain\b17f1b4c-0c87-45b9-b9be-fe3b17f6d0d3\synthetic_queries_125.md"
with open(artifact_path, 'w', encoding='utf-8') as f:
    f.write(md)

print("Markdown created successfully.")
