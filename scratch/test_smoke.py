"""Quick smoke test: run 3 representative queries through the full pipeline."""
import sys, os, time
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')

from mcp_server import _query_tally_internal

queries = [
    # 1. GET_PAYABLES (global, should use two-step path)
    "List the parties to whom I need to make the payment this week",
    # 2. GET_TOP_DEBTORS (global, should use ledger summary fast path)  
    "Top 10 outstanding receivables",
    # 3. GET_RECEIVABLES with specific ledger (should use existing fast path)
    "Show outstanding for Rashmi Traders",
]

for i, q in enumerate(queries):
    print(f"\n{'='*80}")
    print(f"QUERY {i+1}: {q}")
    print(f"{'='*80}")
    t0 = time.time()
    result = _query_tally_internal(q)
    elapsed = time.time() - t0
    print(f"TIME: {elapsed:.2f}s")
    # Print first 800 chars of result
    print(f"RESULT (first 800 chars):\n{result[:800]}")
    print(f"{'='*80}")
