import json
import os

expected_path = "test_suite_expected.json"
if os.path.exists(expected_path):
    with open(expected_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    matches = []
    for item in data:
        q = item.get("query", "").lower()
        if "list total" in q or "total payable" in q:
            matches.append(item)
            
    print(f"Found {len(matches)} queries in the test suite matching the pattern:")
    for m in matches[:10]:
        print(f"\nQuery: '{m.get('query')}'")
        print(f"Expected Intent: {m.get('intent')}")
        print("Expected Entities:", json.dumps(m.get("expected_entities"), indent=2))
else:
    print("test_suite_expected.json not found.")
