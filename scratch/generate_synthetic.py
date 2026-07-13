import json
import random

def generate_queries():
    intents = ["GET_RECEIVABLES", "GET_PAYABLES", "GET_TOP_CREDITORS", "GET_TOP_DEBTORS", "GET_AGEING"]
    groups = ["Group Expenses", "North Zone Customers", "Retailers", "Key Accounts", "Wholesalers", 
              "Hardware Suppliers", "VIP Clients", "Sundry Debtors", "Sundry Creditors", "South Region Debtors", 
              "East Zone Dealers", "Marketing Expenses", "Key Vendors", "Local Suppliers"]
    
    queries = []
    
    # Highly complex templates
    templates = [
        # Template 1: GET_RECEIVABLES combining Date, Group, Amount (Between), Sort, Bill Query
        {
            "q": "Show me individual pending bills for {group} generated this month where the amount is between {min_a} and {max_a} sorted by highest amount first",
            "intent": "GET_RECEIVABLES",
            "entities": lambda g, d, min_a, max_a, lim: {
                "ledger_name": g,
                "date_filter": {"type": "this_month"},
                "age_filter": None,
                "amount_filter": {"operator": "between", "min": float(min_a), "max": float(max_a)},
                "limit": None,
                "sort": {"field": "amount", "order": "desc"},
                "reference_date": None,
                "is_bill_query": True,
                "document_ref": None,
                "date_target": "bill_date",
                "count_only": False,
                "sum_only": False,
                "status_filter": "pending"
            }
        },
        # Template 2: GET_TOP_DEBTORS combining Group, Limit, Age (>), and Amount (>)
        {
            "q": "Who are my top {lim} debtors from {group} having outstanding older than {d} days with balances exceeding {max_a}?",
            "intent": "GET_TOP_DEBTORS",
            "entities": lambda g, d, min_a, max_a, lim: {
                "ledger_name": g,
                "date_filter": None,
                "age_filter": {"operator": ">", "days": d},
                "amount_filter": {"operator": ">", "value": float(max_a)},
                "limit": lim,
                "sort": {"field": "amount", "order": "desc"},
                "reference_date": None,
                "is_bill_query": False,
                "document_ref": None,
                "date_target": "due_date",
                "count_only": False,
                "sum_only": False,
                "status_filter": "pending"
            }
        },
        # Template 3: GET_PAYABLES combining Group, Limit, Date (last N days), Status
        {
            "q": "What is the total sum of payables for {group} from the last {d} days where the bill value was under {min_a}?",
            "intent": "GET_PAYABLES",
            "entities": lambda g, d, min_a, max_a, lim: {
                "ledger_name": g,
                "date_filter": {"type": "last_days", "days": d},
                "age_filter": None,
                "amount_filter": {"operator": "<", "value": float(min_a)},
                "limit": None,
                "sort": None,
                "reference_date": None,
                "is_bill_query": False,
                "document_ref": None,
                "date_target": "due_date",
                "count_only": False,
                "sum_only": True,
                "status_filter": None
            }
        },
        # Template 4: GET_TOP_CREDITORS vs Debtors styling but for one intent
        {
            "q": "Compare top {lim} creditors in {group} who have pending bills between {min_a} and {max_a} overdue by {d} days",
            "intent": "GET_TOP_CREDITORS",
            "entities": lambda g, d, min_a, max_a, lim: {
                "ledger_name": g,
                "date_filter": None,
                "age_filter": {"operator": ">", "days": d},
                "amount_filter": {"operator": "between", "min": float(min_a), "max": float(max_a)},
                "limit": lim,
                "sort": {"field": "amount", "order": "desc"},
                "reference_date": None,
                "is_bill_query": True,
                "document_ref": None,
                "date_target": "due_date",
                "count_only": False,
                "sum_only": False,
                "status_filter": "pending"
            }
        },
        # Template 5: GET_AGEING combining Age range, Amount, Group
        {
            "q": "Give me an ageing summary of {group} for invoices due in the next {d} days ranging from {min_a} to {max_a}",
            "intent": "GET_AGEING",
            "entities": lambda g, d, min_a, max_a, lim: {
                "ledger_name": g,
                "date_filter": {"type": "next_days", "days": d},
                "age_filter": None,
                "amount_filter": {"operator": "between", "min": float(min_a), "max": float(max_a)},
                "limit": None,
                "sort": None,
                "reference_date": None,
                "is_bill_query": False,
                "document_ref": None,
                "date_target": "due_date",
                "count_only": False,
                "sum_only": False,
                "status_filter": "pending"
            }
        },
        # Template 6: Highly complex combination 
        {
            "q": "Count only the top {lim} oldest bills for {group} with value strictly > {max_a} and age < {d} days",
            "intent": "GET_RECEIVABLES",
            "entities": lambda g, d, min_a, max_a, lim: {
                "ledger_name": g,
                "date_filter": None,
                "age_filter": {"operator": "<", "days": d},
                "amount_filter": {"operator": ">", "value": float(max_a)},
                "limit": lim,
                "sort": {"field": "bill_date", "order": "asc"},
                "reference_date": None,
                "is_bill_query": True,
                "document_ref": None,
                "date_target": "bill_date",
                "count_only": True,
                "sum_only": False,
                "status_filter": None
            }
        }
    ]
    
    idx = 0
    while len(queries) < 125:
        template = templates[idx % len(templates)]
        g = random.choice(groups)
        min_a = random.choice([1000, 2500, 5000, 7500, 10000])
        max_a = min_a + random.choice([2500, 5000, 10000, 20000])
        lim = random.choice([3, 5, 7, 10, 15, 20])
        d = random.choice([7, 15, 30, 45, 60, 90, 120])
        
        q_str = template["q"].format(group=g, min_a=min_a, max_a=max_a, lim=lim, d=d)
        
        mutations = [
            q_str,
            q_str.replace("Show me", "Retrieve").replace("Give me", "Fetch"),
            q_str.replace("between", "in the range of").replace("ranging from", "between"),
            q_str.lower(),
            q_str.upper()[0] + q_str[1:] + " please"
        ]
        
        final_q = mutations[len(queries) % len(mutations)]
        # ensure unique queries by adding a slight deterministic noise if needed, but the combinations are huge.
        
        ent = template["entities"](g, d, min_a, max_a, lim)
        
        # ensure no exact duplicate queries
        if not any(q['query'] == final_q for q in queries):
            queries.append({
                "query": final_q,
                "intent": template["intent"],
                "expected_entities": ent
            })
        
        idx += 1
        
        # mix some direct ones based on prompt hint
        if len(queries) == 120:
            queries.append({
                "query": "what is the total outstanding for Group Expenses for amounts between 5000 and 10000",
                "intent": "GET_PAYABLES",
                "expected_entities": {
                    "ledger_name": "Group Expenses",
                    "date_filter": None,
                    "age_filter": None,
                    "amount_filter": {"operator": "between", "min": 5000.0, "max": 10000.0},
                    "limit": None,
                    "sort": None,
                    "reference_date": None,
                    "is_bill_query": False,
                    "document_ref": None,
                    "date_target": "due_date",
                    "count_only": False,
                    "sum_only": True,
                    "status_filter": "pending"
                }
            })
        if len(queries) == 121:
            queries.append({
                "query": "top 5 creditors vs top 10 debtors report for amounts > 50000",
                "intent": "GET_TOP_CREDITORS",
                "expected_entities": {
                    "ledger_name": None,
                    "date_filter": None,
                    "age_filter": None,
                    "amount_filter": {"operator": ">", "value": 50000.0},
                    "limit": 5,
                    "sort": None,
                    "reference_date": None,
                    "is_bill_query": False,
                    "document_ref": None,
                    "date_target": "due_date",
                    "count_only": False,
                    "sum_only": False,
                    "status_filter": None
                }
            })

    with open("c:\\Users\\avija\\projects\\ML_ONNX\\scratch\\synthetic_4.json", "w") as f:
        json.dump(queries[:125], f, indent=4)

    print("Generated", len(queries[:125]), "queries.")

if __name__ == "__main__":
    generate_queries()
