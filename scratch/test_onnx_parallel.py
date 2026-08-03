import time
import sys
sys.path.insert(0, '.')
from nlp_engine import NLPEngine

engine = NLPEngine()

queries = [
    "opening amount of KL store",
    "show all overdue invoices of Jagat from April to June 2025",
    "total receivables for Sundry Debtors above 50000",
    "pending bills for Reliance Job cost center",
    "sales vouchers for last 30 days",
    "trial balance for indirect expenses for Modi Chemplast",
    "stock summary of raw materials in Bhiwandi godown",
    "unpaid invoices with pdc receipts",
    "top 10 creditors by balance amount",
    "gstr 2a reconciled bills for customer Aarkay"
] * 5  # 50 total queries

print("Starting ONNX parallel inference benchmark over 50 queries...")
start_time = time.perf_counter()

for q in queries:
    params = engine.extract_parameters(q)

end_time = time.perf_counter()
total_time = end_time - start_time
avg_ms = (total_time / len(queries)) * 1000

print(f"Total time for 50 queries: {total_time:.4f} seconds")
print(f"Average ONNX parameter extraction time per query: {avg_ms:.2f} ms")
