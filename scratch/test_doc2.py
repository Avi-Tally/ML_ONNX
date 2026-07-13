from nlp_engine import NLPEngine

class MockTally:
    pass

nlp = NLPEngine(MockTally())
res = nlp.extract_parameters('What is the payment status of Bill Number 1027 under Ledger Supreme ?'.lower())
print(res)
