import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
from nlp_engine import NLPEngine

client = TallyClient()
client.update_routing_table()

engine = NLPEngine(client)
query = "List total payable amount whose age > 30 days on 26-nov-2025"
res = engine.parse_query(query)
import json
print(json.dumps(res, indent=2))
