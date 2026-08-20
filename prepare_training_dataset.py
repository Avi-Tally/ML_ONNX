import json
import glob
import os
import re
from collections import Counter

def normalize_text(text: str) -> str:
    """Normalizes whitespace, special quotes, and unicode dashes."""
    if not text:
        return ""
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    text = text.replace("–", "-").replace("—", "-")
    text = re.sub(r'[\x00-\x1f\x7f-\x9f]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def infer_entities_for_batch_query(query: str, intent: str) -> dict:
    """Extracts ground-truth entity parameter slots for batch queries."""
    q_lower = query.lower()
    
    # 1. status_filter
    status_filter = None
    if any(w in q_lower for w in ["overdue", "due", "unpaid", "pending"]):
        status_filter = "pending"
    elif any(w in q_lower for w in ["cleared", "settled", "paid"]):
        status_filter = "cleared"
    elif "advance" in q_lower:
        status_filter = "advance"
    elif "on-account" in q_lower or "on account" in q_lower:
        status_filter = "on_account"

    # 2. date_target
    date_target = "due_date" if any(w in q_lower for w in ["due in", "due date", "due on", "due by"]) else ("bill_date" if any(w in q_lower for w in ["bill date", "invoiced on", "invoice date"]) else None)

    # 3. is_bill_query
    is_bill_query = any(w in q_lower for w in ["bill", "bills", "invoice", "invoices", "voucher", "vouchers", "entry", "entries"])

    # 4. voucher_type
    voucher_type = None
    if "sales" in q_lower: voucher_type = "Sales"
    elif "purchase" in q_lower: voucher_type = "Purchase"
    elif "receipt" in q_lower: voucher_type = "Receipt"
    elif "payment" in q_lower: voucher_type = "Payment"
    elif "journal" in q_lower: voucher_type = "Journal"
    elif "contra" in q_lower: voucher_type = "Contra"
    elif "credit note" in q_lower: voucher_type = "Credit Note"
    elif "debit note" in q_lower: voucher_type = "Debit Note"

    # 5. tax_filter
    tax_filter = any(w in q_lower for w in ["gst", "gstin", "tax", "igst", "cgst", "sgst", "tds"])

    # 6. pdc_only
    pdc_only = any(w in q_lower for w in ["pdc", "post-dated", "post dated", "pdc only"])

    # 7. include_cleared
    include_cleared = any(w in q_lower for w in ["including cleared", "include cleared", "also cleared", "all bills", "historical"])

    # 8. group_name
    group_name = None
    if "sundry debtors" in q_lower or "debtors" in q_lower or "customers" in q_lower: group_name = "Sundry Debtors"
    elif "sundry creditors" in q_lower or "creditors" in q_lower or "suppliers" in q_lower or "vendors" in q_lower: group_name = "Sundry Creditors"
    elif "bank" in q_lower: group_name = "Bank Accounts"
    elif "cash" in q_lower: group_name = "Cash-in-Hand"

    # 9. godown_name
    godown_name = None
    m_gd = re.search(r'\$GD\(([^)]+)\)', query)
    if m_gd:
        godown_name = m_gd.group(1).strip()
    elif "godown" in q_lower or "warehouse" in q_lower or "bhiwandi" in q_lower or "ahmedabad" in q_lower:
        for gd in ["Bhiwandi", "Ahmedabad", "Main Location", "Surat", "Mumbai", "Delhi"]:
            if gd.lower() in q_lower:
                godown_name = gd
                break

    # 10. gst_status
    gst_status = None
    if "gstr2a" in q_lower or "gstr-2a" in q_lower or "reconciled" in q_lower: gst_status = "matched"
    elif "unmatched" in q_lower or "mismatch" in q_lower: gst_status = "unmatched"

    return {
        "status_filter": status_filter,
        "date_target": date_target,
        "is_bill_query": is_bill_query,
        "voucher_type": voucher_type,
        "tax_filter": tax_filter,
        "pdc_only": pdc_only,
        "include_cleared": include_cleared,
        "group_name": group_name,
        "godown_name": godown_name,
        "gst_status": gst_status,
        "document_ref": None
    }

def infer_intent_for_batch_query(q_id: int, query: str) -> str:
    """Accurately assigns ground-truth intent class to batch query based on domain and syntax."""
    q_lower = query.lower()

    # Specific Batch Intent Domains
    if 701 <= q_id <= 750:
        return "GET_STOCK_SUMMARY"
    elif 751 <= q_id <= 800:
        if any(w in q_lower for w in ["batch", "mfg", "expiry", "expiring"]):
            return "GET_BATCH_DETAILS"
        return "GET_STOCK_SUMMARY"
    elif 801 <= q_id <= 900:
        if any(w in q_lower for w in ["supplier", "creditor", "vendor", "payable"]):
            return "GET_PAYABLES"
        return "GET_RECEIVABLES"
    elif 901 <= q_id <= 1000:
        if any(w in q_lower for w in ["voucher", "sales entry", "purchase entry", "payment voucher", "receipt entry", "transactions"]):
            return "GET_RECENT_VOUCHERS"
        elif any(w in q_lower for w in ["payable", "creditor", "vendor"]):
            return "GET_PAYABLES"
        return "GET_RECEIVABLES"
    elif 1001 <= q_id <= 1050:
        if any(w in q_lower for w in ["cost centre", "cost center", "cost category", "category"]):
            return "GET_COST_CENTRE_BREAKUP"
        elif "stock" in q_lower:
            return "GET_STOCK_SUMMARY"
        return "GET_COST_CENTRE_BREAKUP"
    elif 1051 <= q_id <= 1100:
        if any(w in q_lower for w in ["overview", "summary", "dashboard", "executive", "working capital"]):
            return "GET_COMPANY_SUMMARY"
        elif any(w in q_lower for w in ["batch", "batches"]):
            return "GET_BATCH_DETAILS"
        return "GET_COMPANY_SUMMARY"
    elif 1101 <= q_id <= 1150:
        if any(w in q_lower for w in ["batch", "batches", "negative stock"]):
            return "GET_BATCH_DETAILS"
        elif any(w in q_lower for w in ["trust", "credit rating", "most trusted"]):
            return "GET_TRUST_SCORES"
        return "GET_TRUST_SCORES"
    elif 1151 <= q_id <= 1200:
        if any(w in q_lower for w in ["transaction count", "voucher count", "frequent", "frequency"]):
            return "GET_TOP_VENDORS_BY_TXN"
        elif any(w in q_lower for w in ["cash", "bank", "balance of"]):
            return "GET_LEDGER_BALANCE"
        return "GET_TOP_VENDORS_BY_TXN"
    elif 1201 <= q_id <= 1209:
        if "trial balance" in q_lower:
            return "GET_TRIAL_BALANCE"
        elif "compare" in q_lower:
            return "GET_COMPANY_SUMMARY"
        elif any(w in q_lower for w in ["status", "bill", "party"]):
            return "GET_RECEIVABLES"
        return "GET_COMPANY_SUMMARY"

    # Fallback syntactic checks
    if any(w in q_lower for w in ["trust score", "trusted client", "trusted vendor", "credit rating"]):
        return "GET_TRUST_SCORES"
    if any(w in q_lower for w in ["transaction count", "voucher count", "most frequent"]):
        return "GET_TOP_VENDORS_BY_TXN"
    if any(w in q_lower for w in ["company overview", "company summary", "financial overview", "dashboard"]):
        return "GET_COMPANY_SUMMARY"
    if any(w in q_lower for w in ["cost centre", "cost center", "cost category"]):
        return "GET_COST_CENTRE_BREAKUP"
    if any(w in q_lower for w in ["batch details", "expiring batches", "mfg date", "batch-wise"]):
        return "GET_BATCH_DETAILS"
    if any(w in q_lower for w in ["stock summary", "stock item", "inventory valuation", "in godown"]):
        return "GET_STOCK_SUMMARY"
    if any(w in q_lower for w in ["trial balance"]):
        return "GET_TRIAL_BALANCE"
    if any(w in q_lower for w in ["top", "highest", "biggest"]) and any(w in q_lower for w in ["debtor", "customer"]):
        return "GET_TOP_DEBTORS"
    if any(w in q_lower for w in ["top", "highest", "biggest"]) and any(w in q_lower for w in ["creditor", "vendor", "supplier"]):
        return "GET_TOP_CREDITORS"
    if any(w in q_lower for w in ["aging", "ageing", "30 60 90", "buckets"]):
        return "GET_AGEING"
    if any(w in q_lower for w in ["bill ", "invoice ", "bill no", "inv-"]):
        return "GET_BILL_DETAILS"
    if any(w in q_lower for w in ["balance of", "balance for", "ledger 360", "overview of"]):
        return "GET_LEDGER_BALANCE"
    if any(w in q_lower for w in ["payable", "creditor", "supplier", "vendor"]):
        return "GET_PAYABLES"
    return "GET_RECEIVABLES"

def build_dataset_v2():
    print("=" * 80)
    print("📦 BUILDING CONSOLIDATED GROUND-TRUTH TRAINING DATASET (1,209 QUERIES)")
    print("=" * 80)

    # 1. Load Audited test_suite_expected.json (IDs 1-727)
    test_suite_map = {}
    if os.path.exists("test_suite_expected.json"):
        with open("test_suite_expected.json", "r", encoding="utf-8") as f:
            ts_data = json.load(f)
            for idx, item in enumerate(ts_data, start=1):
                intent = item.get("intent", "UNKNOWN")
                # Modernize intent labels
                if intent == "GET_COMPARATIVE_SUMMARY": intent = "GET_COMPANY_SUMMARY"
                elif intent == "GET_LEDGER_360": intent = "GET_LEDGER_BALANCE"
                test_suite_map[idx] = {
                    "query": normalize_text(item.get("query", "")),
                    "intent": intent,
                    "expected_entities": item.get("expected_entities", {})
                }
    print(f"Loaded {len(test_suite_map)} audited queries from test_suite_expected.json")

    # 2. Ingest all 13 Batch Files (scratch/batches/batch_01.json to batch_13.json)
    batch_files = sorted(glob.glob("scratch/batches/batch_*.json"))
    print(f"Ingesting {len(batch_files)} batch files...")

    all_dataset = []
    seen_queries = set()

    for bf in batch_files:
        with open(bf, "r", encoding="utf-8") as f:
            b_data = json.load(f)

        for item in b_data:
            q_id = item["id"]
            orig_q = normalize_text(item.get("original_query", ""))
            live_q = normalize_text(item.get("live_adapted_query", ""))

            # Target query to train on (both original & live adapted)
            queries_to_add = [live_q]
            if orig_q and orig_q.lower() != live_q.lower():
                queries_to_add.append(orig_q)

            # Determine Intent & Entities
            if q_id in test_suite_map and q_id <= 727:
                intent = test_suite_map[q_id]["intent"]
                entities = test_suite_map[q_id]["expected_entities"]
            else:
                intent = infer_intent_for_batch_query(q_id, live_q)
                entities = infer_entities_for_batch_query(live_q, intent)

            # Manual Audited Ground Truth Overrides
            if q_id == 19:
                intent = "GET_RECEIVABLES"
            elif q_id == 20:
                entities["tax_filter"] = True
            elif q_id == 28:
                intent = "GET_PAYABLES"
            elif q_id == 37:
                entities["ledger_name"] = "Jagat"
            elif q_id == 47:
                intent = "AMBIGUOUS_OUTSTANDINGS"
                entities["status_filter"] = "pending"
            elif q_id in [75, 76, 80, 82, 87, 90, 92]:
                entities["ledger_name"] = None
            elif q_id == 81:
                entities["voucher_type"] = "Debit Note"
                entities["amount_filter"] = {"operator": "=", "value": 10000.0}
            elif q_id == 96:
                intent = "GET_PAYABLES"
            elif q_id == 97:
                intent = "GET_RECEIVABLES"
            elif q_id in [107, 108, 127, 128, 129]:
                intent = "GET_COMPANY_SUMMARY" if q_id in [127, 128, 129] else "AMBIGUOUS_OUTSTANDINGS"
                if q_id in [127, 128, 129]:
                    entities["compare_companies"] = True
                    if q_id == 128:
                        entities["ledger_name"] = None
            elif q_id == 132:
                intent = "GET_RECEIVABLES"
                entities["include_cleared"] = True
                entities["date_filter"] = {"type": "today"}
            elif q_id == 133:
                entities["amount_filter"] = {"operator": "=", "value": 60000.0}
            elif q_id == 141:
                entities["amount_filter"] = {"operator": "=", "value": 200000.0}
            elif q_id in [168, 173]:
                entities["include_cleared"] = True
            elif q_id == 182:
                entities["date_target"] = "bill_date"
            elif q_id == 186:
                entities["amount_filter"] = {"operator": "=", "value": 250000.0}
            elif q_id == 220:
                intent = "GET_TRUST_SCORES"
                entities["sort"] = {"field": "trust_score", "order": "asc"}
                queries_to_add = ["Which debtors should I prioritize for follow-up?"]
            elif q_id == 230:
                intent = "GET_RECEIVABLES"
            elif q_id == 250:
                entities["amount_filter"] = {"operator": ">", "value": 500000.0}
            elif q_id == 251:
                entities["document_ref"] = "REF-9942"
            elif q_id == 258:
                entities["group_name"] = "North Zone"
                entities["ledger_name"] = None
            elif q_id == 286:
                entities["group_name"] = "West Zone"
                entities["ledger_name"] = None
            elif q_id == 290:
                intent = "GET_AGEING"
            elif q_id in [313, 316, 317, 318, 321, 326]:
                intent = "GET_TOP_DEBTORS"
                entities["group_name"] = "Sundry Debtors"
                if q_id in [313, 316, 317]:
                    entities["overdue_only"] = True
            elif q_id == 331:
                entities["amount_filter"] = {"operator": ">", "value": 200000.0}
            elif q_id in [332, 333, 341]:
                intent = "GET_TOP_CREDITORS"
                entities["group_name"] = "Sundry Creditors"
                if q_id == 332:
                    entities["overdue_only"] = True
                elif q_id == 333:
                    entities["sum_only"] = False
            elif q_id == 347:
                intent = "GET_RECENT_VOUCHERS"
                entities["voucher_type"] = "Sales"
                entities["pdc_only"] = True
            elif q_id == 348:
                entities["pdc_only"] = True
            elif q_id == 350:
                intent = "GET_RECENT_VOUCHERS"
                entities["voucher_type"] = "Receipt"
                entities["pdc_only"] = True
            elif q_id == 352:
                entities["pdc_only"] = True
            elif q_id == 354:
                intent = "GET_RECENT_VOUCHERS"
                entities["voucher_type"] = "Journal"
                entities["pdc_only"] = True
                entities["ledger_name"] = None
            elif q_id == 405:
                intent = "GET_RECENT_VOUCHERS"
                entities["voucher_type"] = "Purchase"
                entities["ledger_name"] = "Bosch Ltd"
                entities["count_only"] = True
                entities["sum_only"] = False
            elif q_id == 423:
                entities["document_ref"] = "305"
            elif q_id == 447:
                intent = "GET_RECENT_VOUCHERS"
                entities["voucher_type"] = "Journal"
                entities["status_filter"] = None
                entities["ledger_name"] = "Depreciation Account"
            elif q_id == 449:
                intent = "GET_RECENT_VOUCHERS"
                entities["voucher_type"] = "Journal"
                entities["ledger_name"] = None
                entities["amount_filter"] = {"operator": ">", "value": 50000.0}
            elif q_id == 465:
                intent = "GET_RECENT_VOUCHERS"
                entities["voucher_type"] = "Contra"
                entities["ledger_name"] = None
            elif q_id == 503:
                intent = "GET_BILL_DETAILS"
                entities["document_ref"] = "REF-9948"
            elif q_id == 516:
                intent = "AMBIGUOUS_OUTSTANDINGS"
                entities["count_only"] = True
                entities["sum_only"] = False
            elif q_id == 523:
                intent = "AMBIGUOUS_OUTSTANDINGS"
                entities["amount_filter"] = {"operator": "=", "value": 100000.0}
            elif q_id == 536:
                intent = "AMBIGUOUS_OUTSTANDINGS"
                entities["count_only"] = True
                entities["sum_only"] = False
            elif q_id == 542:
                intent = "GET_LEDGER_BALANCE"
                entities["ledger_name"] = "Zenith Traders"
                entities["count_only"] = True
                entities["sum_only"] = False
                entities["overdue_only"] = True
            elif q_id == 592:
                intent = "UNKNOWN"
                entities["godown_name"] = None
            elif q_id == 607:
                entities["group_name"] = "Capital Account"
                entities["ledger_name"] = None
            elif q_id == 613:
                entities["group_name"] = "Current Liabilities"
                entities["ledger_name"] = None
            elif q_id == 614:
                entities["voucher_type"] = None
            elif q_id == 615:
                entities["status_filter"] = None
            elif q_id == 623:
                entities["voucher_type"] = None
            elif q_id == 625:
                entities["group_name"] = "Depreciation"
                entities["ledger_name"] = None
            elif q_id == 659:
                entities["status_filter"] = None
            elif q_id == 664:
                entities["group_name"] = "Vehicles"
                entities["ledger_name"] = None
            elif q_id == 668:
                entities["sum_only"] = True
            elif q_id == 692:
                entities["godown_name"] = None







            for q_str in queries_to_add:

                if not q_str or q_str.lower() in seen_queries:
                    continue
                seen_queries.add(q_str.lower())

                # Entity copy with inferred slots
                ent_copy = infer_entities_for_batch_query(q_str, intent)
                if isinstance(entities, dict):
                    ent_copy.update({k: v for k, v in entities.items() if v is not None})

                all_dataset.append({
                    "id": q_id,
                    "query": q_str,
                    "intent": intent,
                    "expected_intent": intent,
                    "expected_entities": ent_copy
                })

    print(f"\n✅ Total Consolidated Ground-Truth Samples: {len(all_dataset)}")

    # 3. Intent Distribution Audit
    intent_counts = Counter(x["intent"] for x in all_dataset)
    print("\n📊 Intent Class Distribution:")
    for intent_name, count in sorted(intent_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  * {intent_name:<28}: {count:>4} samples")

    # 4. Save training_data_v2.json
    out_path = "training_data_v2.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_dataset, f, indent=2, ensure_ascii=False)

    size_kb = os.path.getsize(out_path) / 1024
    print(f"\n💾 Saved consolidated dataset to {out_path} ({size_kb:.2f} KB)")
    print("=" * 80)

if __name__ == "__main__":
    build_dataset_v2()
