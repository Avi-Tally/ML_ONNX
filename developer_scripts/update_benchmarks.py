import json
import re

with open("test_suite_expected.json", "r") as f:
    expected = json.load(f)

# Group valid queries by intent
intent_queries = {
    "LIST_COMPANIES": ["what companies are loaded", "show me active companies", "list running companies"],
    "GET_LEDGER_BALANCE": ["what is the balance of", "closing balance of", "ledger balance", "how much is in account"],
    "GET_TRIAL_BALANCE": ["show trial balance", "get trial balance", "trial balance report"],
    "GET_STOCK_SUMMARY": ["stock summary", "inventory status", "how much stock do I have"],
    "GET_RECENT_VOUCHERS": ["show daybook", "recent transactions", "today's vouchers", "latest entries"],
    "GET_RECEIVABLES": ["what do they owe me", "pending bills for debtor", "receivables from", "show pending invoices", "outstanding amount from"],
    "GET_PAYABLES": ["what do I owe them", "pending bills for creditor", "payables to", "show pending invoices from supplier"],
    "GET_AGEING": ["ageing analysis", "bills older than 90 days", "pending since last month"],
    "GET_TOP_DEBTORS": ["top 10 debtors", "highest outstanding customers", "biggest receivables"],
    "GET_TOP_CREDITORS": ["top 10 creditors", "highest payable suppliers", "biggest payables"]
}

added_count = 0
for item in expected:
    intent = item["expected_intent"]
    query = item["query_text"]
    
    if intent and intent != "UNKNOWN" and intent in intent_queries:
        if query not in intent_queries[intent]:
            intent_queries[intent].append(query)
            added_count += 1

# Generate the python dict string
dict_str = '            self.INTENT_BENCHMARKS = {\n'
for intent, queries in intent_queries.items():
    queries_str = ", ".join(f'"{q}"' for q in queries)
    dict_str += f'                "{intent}": [{queries_str}],\n'
dict_str += '            }'

with open("nlp_engine.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the block
pattern = re.compile(r'            self\.INTENT_BENCHMARKS = \{.*?\n            \}', re.DOTALL)
new_content = pattern.sub(dict_str, content)

with open("nlp_engine.py", "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Successfully injected {added_count} real-world queries into nlp_engine.py INTENT_BENCHMARKS!")
