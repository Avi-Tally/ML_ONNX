import sys
from mcp_server import query_tally
result = query_tally("opening amount of KL store")
with open('output_kl_store.txt', 'w', encoding='utf-8') as f:
    f.write(result)
