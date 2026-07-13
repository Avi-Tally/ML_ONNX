import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from mcp_server import _query_tally_internal

q1 = "Total overdue payable till 26-11-25 age < 30 days"
print(f"Executing: '{q1}'")
print(_query_tally_internal(q1))

q2 = "Total overdue payable till 26-11-25 age > 30 days"
print(f"\nExecuting: '{q2}'")
print(_query_tally_internal(q2))
