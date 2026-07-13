import sys
sys.path.append('.')
from nlp_engine import NLPEngine
class MockTallyClient:
    def __init__(self, data):
        self.routing_table = {'mock_company': {'port': 9000, 'name': 'Mock Company'}}
        self.ledgers = {}
    def fetch_ledgers(self, company, port):
        return self.ledgers
    def get_port_for_company(self, company_key):
        return 9000, 'Mock Company', None

tally = MockTallyClient({})
# Populate ledgers
tally.ledgers = {
    "Local Suppliers": "0.00",
    "Key Vendors": "0.00",
    "Hardware Suppliers": "0.00",
    "Group Expenses": "0.00",
    "Retailers": "0.00",
    "Wholesalers": "0.00",
    "Sundry Creditors": "0.00",
    "South Region Debtors": "0.00",
    "Sundry Debtors": "0.00",
    "John Doe": "0.00"
}
tally.routing_table = {
    "modi chemplast materials pvt ltd": {"port": 9000, "name": "Modi Chemplast Materials Pvt Ltd"}
}

nlp = NLPEngine(tally_client=tally)
q = "Show company-wise outstanding for ModiChem company and also identify whether the balance is receivable, payable, or net."

# Run parse_query parts
query_clean = q.strip()
query_lower = query_clean.lower()
query_without_company = query_clean
parameters = nlp.extract_parameters(query_without_company)
detected_intent = nlp.predict_intent(query_without_company)
res_ledger, score, amb = nlp.resolve_ledger(query_without_company, tally.ledgers)

print("Initial Intent:", detected_intent)
print("Resolved Ledger:", res_ledger)
print("Score:", score)
print("Amb:", amb)

# Tracing exact match manually
query_lower = query_without_company.lower()
for name in tally.ledgers.keys():
    name_lower = name.lower()
    pattern = r'\b' + name_lower + r'\b'
    import re
    print(f"Checking {name_lower} against pattern {pattern}: match={bool(re.search(pattern, query_lower))}")
res = nlp.parse_query(q)
print("Final Intent:", res["intent"])
print("Final Resolved Ledger:", res["resolved_ledger"])
