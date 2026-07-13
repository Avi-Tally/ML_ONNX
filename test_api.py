import requests
import json
import time

# Give the server a second to start up
time.sleep(2)

print("--- Testing /health ---")
r = requests.get("http://127.0.0.1:8000/health")
print(f"Status: {r.status_code}")
print(json.dumps(r.json(), indent=2))

print("\n--- Testing /companies ---")
r = requests.get("http://127.0.0.1:8000/companies")
print(f"Status: {r.status_code}")
print(json.dumps(r.json(), indent=2))

print("\n--- Testing /query (LIST_COMPANIES) ---")
r = requests.post("http://127.0.0.1:8000/query", json={"query": "what companies are loaded?"})
print(f"Status: {r.status_code}")
print(json.dumps(r.json(), indent=2))

print("\n--- Testing /query (GET_LEDGER_BALANCE for Modi Chemplast) ---")
r = requests.post("http://127.0.0.1:8000/query", json={"query": "what is the balance of Anand Cargo?"})
print(f"Status: {r.status_code}")
print(json.dumps(r.json(), indent=2))

print("\n--- Testing /query (FAQ Query) ---")
r = requests.post("http://127.0.0.1:8000/query", json={"query": "What is an overdue bill?"})
print(f"Status: {r.status_code}")
print(json.dumps(r.json(), indent=2))
