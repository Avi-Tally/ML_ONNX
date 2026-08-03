import sys
sys.path.append('.')
from mcp_server import _query_tally_internal

queries = [
    ('Tier 1 - Receivables', 'What are my total receivables all time?'),
    ('Tier 1 - Comparative', 'Show comparative summary of receivables vs payables all time'),
    ('Tier 2 - Sorting', 'Who are my top 5 debtors all time?'),
    ('Tier 3 - Filtering', 'Show me bills for all time'),
    ('Tier 4 - Ledger', 'What is the balance for aakash kumar sharma all time?')
]

with open('scratch/detailed_benchmark_v2.md', 'w', encoding='utf-8') as f:
    for name, q in queries:
        f.write(f'# {name}: {q}\n')
        try:
            res = _query_tally_internal(q)
            f.write(res + '\n\n')
        except Exception as e:
            f.write(f'Error: {e}\n\n')
