import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from nlp_engine import NLPEngine
from tally_client import TallyClient
import mcp_server

mcp_server.tally_client = TallyClient()
mcp_server.nlp = NLPEngine()

q = "List outstanding payables whose age > 40 days on 29-nov-2025"
print(f"Executing Query: '{q}'")
res = mcp_server._query_tally_internal(q)
print(res)
