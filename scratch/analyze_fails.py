import sys
import json
import codecs
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append('.')
from tally_client import TallyClient
from nlp_engine import NLPEngine

expected_path = 'scratch/augmented_training_data.json'
with open(expected_path, 'r', encoding='utf-8') as f:
    expected_data = json.load(f)

for item in expected_data:
    if 'query' in item and 'query_text' not in item:
        item['query_text'] = item['query']
    if 'intent' in item and 'expected_intent' not in item:
        item['expected_intent'] = item['intent']

class MockTallyClient:
    def __init__(self, data):
        self.routing_table = {'mock_company': {'port': 9000, 'name': 'Mock Company'}}
        self.ledgers = {}
        for q in data:
            lname = q.get('expected_entities', {}).get('ledger_name')
            if lname:
                self.ledgers[lname] = '0.00'
                
    def get_port_for_company(self, query):
        return 9000, 'Mock Company', {}
        
    def fetch_ledgers(self, company, port):
        return self.ledgers

client = MockTallyClient(expected_data)
nlp = NLPEngine(client)

failures = {'intent': 0, 'ledger': 0, 'params': {}, 'other': 0}
mismatched_examples = []

for q in expected_data:
    query = q.get('query_text')
    exp_intent = q.get('expected_intent')
    exp_entities = q.get('expected_entities', {})
    
    try:
        parsed = nlp.parse_query(query)
        act_intent = parsed['intent']
        act_ledger = parsed.get('resolved_ledger')
        act_params = parsed.get('parameters', {})
        
        if act_intent != exp_intent:
            failures['intent'] += 1
            mismatched_examples.append({
                'query': query,
                'type': 'intent',
                'expected': exp_intent,
                'actual': act_intent
            })
            continue
            
        if exp_intent == 'UNKNOWN':
            continue
            
        exp_ledger = exp_entities.get('ledger_name')
        ledger_match = True
        if exp_ledger:
            if not act_ledger or exp_ledger.lower() != act_ledger.lower():
                ledger_match = False
        elif act_ledger and act_ledger != '':
            ledger_match = False
            
        if not ledger_match:
            failures['ledger'] += 1
            mismatched_examples.append({
                'query': query,
                'type': 'ledger',
                'expected': exp_ledger,
                'actual': act_ledger
            })
            continue
            
        param_fail = False
        for k, expected_val in exp_entities.items():
            if k == 'ledger_name':
                continue
            actual_val = act_params.get(k)
            if expected_val != actual_val:
                failures['params'][k] = failures['params'].get(k, 0) + 1
                if not param_fail:
                    mismatched_examples.append({
                        'query': query,
                        'type': f'param:{k}',
                        'expected': expected_val,
                        'actual': actual_val
                    })
                    param_fail = True
    except Exception as e:
        failures['other'] += 1
        mismatched_examples.append({
            'query': query,
            'type': 'error',
            'error': str(e)
        })

print("Failures breakdown:")
print(json.dumps(failures, indent=2))
intent_fails = [m for m in mismatched_examples if m['type'] == 'intent']
print("\nIntent Failures (total {}):".format(len(intent_fails)))
for inf in intent_fails:
    print("Query: '{}' | Exp: {} | Act: {}".format(inf['query'], inf['expected'], inf['actual']))
    
ledger_fails = [m for m in mismatched_examples if m['type'] == 'ledger']
print("\nLedger Failures (total {}):".format(len(ledger_fails)))
for lf in ledger_fails[:20]:
    print("Query: '{}' | Exp: {} | Act: {}".format(lf['query'], lf['expected'], lf['actual']))
    
limit_fails = [m for m in mismatched_examples if m['type'] == 'param:limit']
print("\nLimit Failures (total {}):".format(len(limit_fails)))
for lf in limit_fails:
    print("Query: '{}' | Exp: {} | Act: {}".format(lf['query'], lf['expected'], lf['actual']))
    
amount_fails = [m for m in mismatched_examples if m['type'] == 'param:amount_filter']
print("\nAmount Filter Failures (total {}):".format(len(amount_fails)))
for af in amount_fails:
    print("Query: '{}' | Exp: {} | Act: {}".format(af['query'], af['expected'], af['actual']))
