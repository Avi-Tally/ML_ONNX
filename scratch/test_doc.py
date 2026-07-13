from nlp_engine import NLPEngine

class MockTally:
    pass

nlp = NLPEngine(MockTally())
print(nlp.extract_parameters('What is the payment status of Bill Number 1027 under Ledger Supreme ?'.lower(), 'GET_BILL_DETAILS', False, None, False, None, False, False))
