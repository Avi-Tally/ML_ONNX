import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient

client = TallyClient()
print("Routing Table:")
for co, port in client.routing_table.items():
    print(f"  Company: '{co}' -> Port: {port}")
