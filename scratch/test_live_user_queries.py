import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from mcp_server import _query_tally_internal

q1 = "List total payable amount whose age > 30 days on 26-nov-2025"
print(f"Executing: '{q1}'")
print(_query_tally_internal(q1))

q2 = "List total payable amount on 26-nov-2025"
print(f"\nExecuting: '{q2}'")
print(_query_tally_internal(q2))
