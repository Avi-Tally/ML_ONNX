import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
from nlp_engine import NLPEngine
import json

client = TallyClient()
# Mock routing table to simulate both companies online
client.routing_table = {
  "modi chemplast materials pvt ltd": {
    "name": "Modi Chemplast Materials Pvt Ltd",
    "port": 9000,
    "context": {
      "current_date": "26-Nov-2025",
      "from_date": "01-Apr-2025",
      "to_date": "31-Mar-2026"
    }
  },
  "bella casa data for user activity": {
    "name": "Bella Casa Data for User Activity",
    "port": 9001,
    "context": {
      "current_date": "08-Oct-2017",
      "from_date": "01-Apr-2017",
      "to_date": "31-Mar-2018"
    }
  }
}

engine = NLPEngine(client)
query = " List payables whose age > 40 days on 29 OCT 2025"
parsed = engine.parse_query(query)

print(json.dumps(parsed, indent=2))
