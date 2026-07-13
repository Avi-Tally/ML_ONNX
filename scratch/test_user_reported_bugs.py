import sys
import os
import codecs
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from mcp_server import query_tally

queries = [
    "What’s the total overdue payable beyond 30 days till 26-11-25",
    "Total overdue payable age > 30 days till 26-11-25",
    "Total overdue payable age < 30 days till 26-11-25"
]

for idx, q in enumerate(queries, 1):
    print(f"\n==================================================")
    print(f"Executing User Bug Case #{idx}:")
    print(f"'{q}'")
    print(f"==================================================")
    response = query_tally(q)
    print(response)
