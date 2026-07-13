from nlp_engine import NLPEngine

class MockTallyClient:
    def __init__(self, ledgers):
        self.routing_table = {"mock_company": {"port": 9000, "name": "Mock Company"}}
        self.ledgers = ledgers
    def get_port_for_company(self, query):
        return 9000, "Mock Company", {}
    def fetch_ledgers(self, company, port):
        return self.ledgers

ledgers = {"sundry debtors": "0.00", "Aquatech system": "0.00", "AquaTech system": "0.00"}
engine = NLPEngine(MockTallyClient(ledgers))

query1 = "Show highest pending and cleared receivables bill amount for sundry debtors also give their GST status?"
res1 = engine.parse_query(query1)
print(f"Query 1: {res1.get('resolved_ledger')}")

query2 = "what is the outstanding of Aquatech system"
res2 = engine.parse_query(query2)
print(f"Query 2: {res2.get('resolved_ledger')}")
