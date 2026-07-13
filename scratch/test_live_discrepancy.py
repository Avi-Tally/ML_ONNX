import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from mcp_server import _query_tally_internal
import json

query = "Total overdue payable till 26-11-25"
print(f"Executing query: '{query}'")

res = _query_tally_internal(query)
print("\nResponse:")
print(res)
