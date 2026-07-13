import json
import os
import time
from tally_client import TallyClient
from nlp_engine import NLPEngine

def build_mismatch_report(expected_path, output_path):
    if not os.path.exists(expected_path):
        print(f"Error: {expected_path} not found.")
        return

    with open(expected_path, 'r', encoding='utf-8') as f:
        try:
            expected_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return
            
    # Ensure all elements have normalized key mappings
    for item in expected_data:
        if "query" in item and "query_text" not in item:
            item["query_text"] = item["query"]
        if "intent" in item and "expected_intent" not in item:
            item["expected_intent"] = item["intent"]

    class MockTallyClient:
        def __init__(self, expected_data):
            self.routing_table = {"mock_company": {"port": 9000, "name": "Mock Company"}}
            self.ledgers = {}
            for q in expected_data:
                lname = q.get('expected_entities', {}).get('ledger_name')
                if lname:
                    self.ledgers[lname] = "0.00"
            
        def get_port_for_company(self, query):
            return 9000, "Mock Company", {}
        def fetch_ledgers(self, company, port):
            return self.ledgers
            
    client = MockTallyClient(expected_data)
    nlp = NLPEngine(client)

    mismatches = []
    matches = []
    total = len(expected_data)
    passed = 0
    failed = 0
    unknowns = 0

    for item in expected_data:
        query_text = item.get("query_text", item.get("query", ""))
        exp_intent = item.get("expected_intent", item.get("intent", "UNKNOWN"))
        exp_entities = item.get("expected_entities", {})

        if exp_intent == "UNKNOWN":
            unknowns += 1

        try:
            # Parse query using our actual Python engine
            parsed = nlp.parse_query(query_text)
            act_intent = parsed.get("intent")
            params = parsed.get("parameters", {})
            act_ledger = parsed.get("resolved_ledger")
            
            # Compare Intent
            intent_match = (act_intent == exp_intent)
            
            # Compare Ledger (case insensitive, allow None)
            exp_ledger = exp_entities.get("ledger_name")
            ledger_match = True
            if exp_intent != "UNKNOWN":
                if exp_ledger:
                    if not act_ledger or exp_ledger.lower() != act_ledger.lower():
                        ledger_match = False
                elif act_ledger and act_ledger != "":
                    # Expected None but got something
                    ledger_match = False

            # Compare Parameters Strictly
            def check_params_match(exp_dict, act_dict):
                for key, expected_val in exp_dict.items():
                    if key == "ledger_name":
                        continue  # Already checked above
                    
                    actual_val = act_dict.get(key)
                    if expected_val != actual_val:
                        return False, f"Param mismatch on {key}: Expected {expected_val}, Actual {actual_val}"
                return True, "Success"

            params_match, mismatch_reason = True, "Success"
            if exp_intent != "UNKNOWN":
                params_match, mismatch_reason = check_params_match(exp_entities, params)
            
            if intent_match and ledger_match and params_match:
                passed += 1
                matches.append({
                    "query": query_text,
                    "intent": exp_intent,
                    "ledger": exp_ledger,
                    "params": params
                })
            else:
                failed += 1
                
                # Determine primary reason for failure for logging
                if not intent_match:
                    fail_reason = f"Intent mismatch: Exp {exp_intent}, Act {act_intent}"
                elif not ledger_match:
                    fail_reason = f"Ledger mismatch: Exp {exp_ledger}, Act {act_ledger}"
                else:
                    fail_reason = mismatch_reason
                    
                mismatches.append({
                    "query": query_text,
                    "expected_intent": exp_intent,
                    "actual_intent": act_intent,
                    "expected_ledger": exp_ledger,
                    "actual_ledger": act_ledger,
                    "raw_params": params,
                    "exp_params": exp_entities,
                    "reason": fail_reason
                })
        except Exception as e:
            failed += 1
            mismatches.append({
                "query": query_text,
                "error": str(e)
            })

    # Write Mismatch Markdown Report
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# NLP Engine Mismatch Report\n\n")
        f.write(f"**Total Queries:** {total}\n")
        f.write(f"**Passed:** {passed}\n")
        f.write(f"**Failed:** {failed}\n")
        f.write(f"**Total FAQ/Unknown:** {unknowns}\n")
        f.write(f"**Pass Rate:** {(passed/total*100) if total > 0 else 0:.2f}%\n\n")
        
        f.write("## Mismatches\n\n")
        if not mismatches:
            f.write("No mismatches found! 100% Pass Rate.\n")
        else:
            for m in mismatches:
                f.write(f"### Query: `{m['query']}`\n")
                if "error" in m:
                    f.write(f"- **CRASH:** {m['error']}\n")
                else:
                    f.write(f"- **Expected Intent:** {m['expected_intent']} | **Actual Intent:** {m['actual_intent']}\n")
                    f.write(f"- **Expected Ledger:** {m['expected_ledger']} | **Actual Ledger:** {m['actual_ledger']}\n")
                    f.write(f"- **Fail Reason:** {m['reason']}\n")
                    f.write(f"- **Expected Params:** `{json.dumps(m['exp_params'])}`\n")
                    f.write(f"- **Extracted Params:** `{json.dumps(m['raw_params'])}`\n")
                f.write("\n---\n\n")
                
    # Write Matched Markdown Report
    matched_path = output_path.replace("mismatch_report", "matched_report")
    with open(matched_path, 'w', encoding='utf-8') as f:
        f.write("# NLP Engine Matched Report (True Passes)\n\n")
        f.write(f"**Total Queries:** {total}\n")
        f.write(f"**Passed:** {passed}\n")
        f.write(f"**Total FAQ/Unknown:** {unknowns}\n")
        f.write(f"**Pass Rate:** {(passed/total*100) if total > 0 else 0:.2f}%\n\n")
        
        f.write("## Matches\n\n")
        if not matches:
            f.write("No matches found yet.\n")
        else:
            for m in matches:
                f.write(f"### Query: `{m['query']}`\n")
                f.write(f"- **Intent:** `{m['intent']}`\n")
                f.write(f"- **Ledger:** `{m['ledger']}`\n")
                f.write(f"- **Parameters:** `{json.dumps(m['params'])}`\n")
                f.write("\n---\n\n")
                
    print(f"Validation complete. Mismatch report written to {output_path}")
    print(f"Matched report written to {matched_path}")

if __name__ == "__main__":
    build_mismatch_report("scratch/augmented_training_data.json", "mismatch_report.md")
