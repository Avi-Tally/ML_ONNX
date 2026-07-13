import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient

client = TallyClient()
company = "Bella Casa Data for User Activity"
port = 9001

group_map = client.get_group_hierarchy_map(company, port)
print(f"Group map keys count: {len(group_map)}")
print("Sample entries:")
for k, v in list(group_map.items())[:15]:
    print(f"  '{k}' -> '{v}'")
