from nlp_engine import NLPEngine

class MockTally:
    pass

nlp = NLPEngine(MockTally())
q = "What's the total overdue receivable amount?"
res = nlp.extract_parameters(q.lower())
print(res)
