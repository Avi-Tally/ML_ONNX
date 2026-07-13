import requests
import json
import time

time.sleep(2)

queries = [
    "Pending bills on 1-dec-2025 with age less than 80",
    "Pending bills on 1-dec-2025 with age less than 80 days",
    "Pending bills on 1-dec-2025 with age less than 80 days for ledger Veolia water tech",
    "List receivable ageing for sundry creditors where total pending amount is less than 50000"
]

for q in queries:
    print(f"\nQuery: {q}")
    r = requests.post("http://127.0.0.1:8000/query", json={"query": q})
    print(f"Status: {r.status_code}")
    print(f"Company: {r.json().get('company')}")
    print(f"Resolved Ledger: {r.json().get('resolved_ledger')}")
