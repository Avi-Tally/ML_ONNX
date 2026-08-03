import sys
sys.path.insert(0, '.')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from mcp_server import query_tally

query = "opening balance of Aquatech system at start of FY 24-25"
print("Executing test query:", query)
result = query_tally(query)
print("\n=== QUERY RESPONSE ===")
print(result)
