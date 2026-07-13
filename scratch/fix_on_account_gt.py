import json

def fix_on_account_gt():
    with open('test_suite_expected.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    count = 0
    for d in data:
        q = d.get('query_text', d.get('query', '')).lower()
        if 'on account' in q or 'on-account' in q:
            if 'expected_entities' in d and d['expected_entities'].get('date_target') == 'due_date':
                d['expected_entities']['date_target'] = 'bill_date'
                count += 1
            
    with open('test_suite_expected.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Fixed {count} on-account queries in test_suite_expected.json to have date_target: 'bill_date'")

if __name__ == "__main__":
    fix_on_account_gt()
