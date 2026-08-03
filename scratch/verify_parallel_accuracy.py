import sys
sys.path.insert(0, '.')
from nlp_engine import NLPEngine

engine = NLPEngine()

test_cases = [
    ("sales vouchers for last 30 days", {"voucher_type": "Sales"}),
    ("pending bills for customer Aarkay", {"is_bill_query": True}),
    ("unpaid invoices with pdc receipts", {"pdc_only": True}),
]

print("Verifying accuracy of parallelized ONNX inference...")
all_passed = True
for query, expected in test_cases:
    params = engine.extract_parameters(query)
    for k, v in expected.items():
        if params.get(k) != v:
            print(f"FAILED for query '{query}': expected {k}={v}, got {params.get(k)}")
            all_passed = False
        else:
            print(f"PASSED for query '{query}': {k} = {v}")

if all_passed:
    print("ALL ACCURACY ASSERTONS PASSED SUCCESSFULLY!")
