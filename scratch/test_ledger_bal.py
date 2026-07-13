import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))
from mcp_server import query_tally
print(query_tally('ledger balance of Anand Cargo'))
