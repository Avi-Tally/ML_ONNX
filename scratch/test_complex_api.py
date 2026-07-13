import requests
import json
import sys
import codecs
sys.stdout.reconfigure(encoding='utf-8')

queries = [
    # 1. Complex Ageing Query with real ledger "Jagat"
    "Give me the ageing buckets of 30 60 90 last 180 days for Jagat based on bill date with amount less than 5000000 showing top 20 sorted by due date descending",
    
    # 2. Complex Receivables Query with real ledger "Reliance Industries"
    "List all receivable bills last 180 days for Reliance Industries based on bill date with amount less than 5000000 less than 90 days old showing top 10 sorted by due date descending",
    
    # 3. Complex Group-level Query with sum_only and limit override
    "How many pending payable bills for Sundry Creditors are there and what is their total value sorted by lowest amount?"
]

for idx, q in enumerate(queries, 1):
    print(f"\n==================================================")
    print(f"Executing Complex Query #{idx}:")
    print(f"'{q}'")
    print(f"==================================================")
    try:
        r = requests.post("http://127.0.0.1:8000/query", json={"query": q})
        print(f"Status: {r.status_code}")
        res = r.json()
        print(f"Intent: {res.get('intent')}")
        print(f"Company: {res.get('company')}")
        print(f"Resolved Ledger: {res.get('resolved_ledger')}")
        print("Raw Response Output:")
        print(res.get('raw_response'))
    except Exception as e:
        print(f"Error executing query: {e}")
