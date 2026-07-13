import sys
sys.path.append('.')
import json
from nlp_engine import NLPEngine

class MockClient:
    def __init__(self):
        self.routing_table = {"mock_company": {"port": 9000, "name": "Mock Company"}}
    def get_port_for_company(self, query):
        return 9000, "Mock Company", {}
    def fetch_ledgers(self, company, port):
        return {"Mock Ledger": "0.00"}

nlp = NLPEngine(MockClient())
q1 = 'What is the balance outstanding for bill 613 as of today?'
q2 = 'Display the Opening Amount, pending and final balance of payables as on 02-03-2025'

print(f'Q1: {q1}')
print(json.dumps(nlp.parse_query(q1), indent=2))

print(f'\nQ2: {q2}')
print(json.dumps(nlp.parse_query(q2), indent=2))
