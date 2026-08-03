import time
from mcp_server import _query_tally_internal

queries = [
    ("Tier 1 - Summary", "What are my total receivables?"),
    ("Tier 1 - Summary", "Show comparative summary of receivables vs payables"),
    ("Tier 2 - Sorting", "Who are my top 5 debtors?"),
    ("Tier 3 - Date Filtered Bills", "Show me bills for last month"),
    ("Tier 4 - Party Ledgers", "What is the balance for adinath?")
]

print("Starting benchmark of TDL queries...")
print("-" * 50)
for tier, q in queries:
    start_time = time.time()
    try:
        res = _query_tally_internal(q)
        # Handle the result string, truncate if too long
        res_preview = res[:200].replace('\n', ' ') + '...' if len(res) > 200 else res.replace('\n', ' ')
        success = not str(res).startswith("Error") and "could not resolve" not in str(res).lower()
        status = "SUCCESS" if success else "FAILED"
    except Exception as e:
        status = f"ERROR ({e})"
        res_preview = ""
    elapsed = time.time() - start_time
    print(f"[{tier}] Query: '{q}'")
    print(f"  Time  : {elapsed:.2f}s")
    print(f"  Status: {status}")
    print(f"  Output: {res_preview}")
    print("-" * 50)
