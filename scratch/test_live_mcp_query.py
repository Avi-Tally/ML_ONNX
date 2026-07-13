import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from nlp_engine import NLPEngine
from tally_client import TallyClient
from analytics_engine import AnalyticsEngine
import mcp_server

# Mock the company and port resolution
mcp_server.tally_client = TallyClient()
mcp_server.nlp = NLPEngine()

# Run query 1
q1 = "List outstanding payables whose age < 40 days on 29-nov-2025"
print(f"Executing Query 1: '{q1}'")
res1 = mcp_server._query_tally_internal(q1)
print(res1)
print("\n" + "="*80 + "\n")

# Run query 2
q2 = "List outstanding payables whose age < 40 days on 29-oct-2025"
print(f"Executing Query 2: '{q2}'")
res2 = mcp_server._query_tally_internal(q2)
print(res2)
