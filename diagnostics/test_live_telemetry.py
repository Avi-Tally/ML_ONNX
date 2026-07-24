import sys
import os
sys.path.append(os.path.abspath('.'))
from mcp_server import query_tally

queries = [
    "Show trial balance",
    "Show me the overdue invoices of Jagat",
    "What is the total outstanding for Bella Casa"
]

print("=== TESTING CHRONOLOGICAL PIPELINE TELEMETRY SUITE ===")
for q in queries:
    print(f"\n[QUERY]: '{q}'")
    out = query_tally(q)
    print("--> MCP Response Output Tail (Telemetry Footer):\n")
    safe_out = out.encode('ascii', errors='backslashreplace').decode('ascii')
    print("\n".join(safe_out.splitlines()[-15:]))
    print("=" * 80)
