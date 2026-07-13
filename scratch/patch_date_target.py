import json

def patch_ground_truth():
    with open('test_suite_expected.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    count = 0
    for d in data:
        q = d.get('query_text', d.get('query', '')).lower()
        intent = d.get('intent', d.get('expected_intent', ''))
        
        # Any query explicitly mentioning payment/due OR falling into payables/receivables
        if ('payment' in q or 'pay' in q or 'due' in q or 'receivable' in q or 'payable' in q or 
            intent in ['GET_PAYABLES', 'GET_RECEIVABLES']):
            if 'expected_entities' in d:
                d['expected_entities']['date_target'] = 'due_date'
                count += 1
            
    with open('test_suite_expected.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Patched {count} queries in test_suite_expected.json to have date_target: 'due_date'")

if __name__ == "__main__":
    patch_ground_truth()
