import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
import json

client = TallyClient()
client.update_routing_table()
print(json.dumps(client.routing_table, indent=2))
