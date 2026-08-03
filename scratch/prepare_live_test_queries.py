import sys
import json
import os
import zipfile
import xml.etree.ElementTree as ET

sys.path.insert(0, '.')

# Load exported live Tally masters
with open("scratch/live_tally_masters.json", "r", encoding="utf-8") as f:
    masters = json.load(f)

real_ledgers = masters["ledgers"]
real_bills = [b for b in masters["bill_refs"] if len(b) > 2 and b not in ["Op", "OP", "PAYMENT"]]

print(f"Loaded {len(real_ledgers)} real ledgers and {len(real_bills)} real bills.")

# 1. Load queries from test_suite_expected.json
test_suite = json.load(open("test_suite_expected.json", encoding="utf-8"))
queries_ts = [item["query"] for item in test_suite]

# 2. Load queries from queries (1).xlsx
def load_xlsx_queries(path):
    z = zipfile.ZipFile(path)
    ss_xml = ET.fromstring(z.read('xl/sharedStrings.xml')) if 'xl/sharedStrings.xml' in z.namelist() else None
    strings = []
    if ss_xml is not None:
        for si in ss_xml.findall('.//{*}si'):
            text = "".join([t.text for t in si.findall('.//{*}t') if t.text])
            strings.append(text)
    sheet_xml = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
    queries = []
    for row in sheet_xml.findall('.//{*}row'):
        row_vals = []
        for c in row.findall('{*}c'):
            t = c.attrib.get('t')
            v_node = c.find('{*}v')
            val = ""
            if v_node is not None and v_node.text:
                if t == 's':
                    idx = int(v_node.text)
                    val = strings[idx] if idx < len(strings) else ""
                else:
                    val = v_node.text
            row_vals.append(val)
        if row_vals and row_vals[0].strip() and row_vals[0].strip().lower() != 'queries':
            queries.append(row_vals[0].strip())
    return queries

queries_xlsx = load_xlsx_queries(r'C:\Users\avija\Downloads\queries (1).xlsx')

print(f"Total benchmark queries: {len(queries_ts)}")
print(f"Total XLSX queries: {len(queries_xlsx)}")

# Combine all queries
all_raw_queries = queries_ts + queries_xlsx
print(f"Total combined raw queries: {len(all_raw_queries)}")

# Substitute placeholders with real live Tally entity names where applicable
prepared_queries = []
ledger_idx = 0
bill_idx = 0

for i, q in enumerate(all_raw_queries, 1):
    q_mod = q
    
    # Replace common placeholder ledgers with actual real Tally ledgers
    placeholders = ["Reliance Industries Ltd", "Infosys Ltd", "Thermax Ltd", "Aquatech system", "Jaguar Traders", "DeltaFlow", "Varad engineers", "CECO", "Thermax"]
    for ph in placeholders:
        if ph.lower() in q_mod.lower():
            target_ledger = real_ledgers[ledger_idx % len(real_ledgers)]
            ledger_idx += 1
            # Case-insensitive replacement preserving surrounding punctuation
            import re
            q_mod = re.sub(re.escape(ph), target_ledger, q_mod, flags=re.IGNORECASE)
            
    # Replace bill 613 / bill numbers with real bills
    if "bill 613" in q_mod.lower() or "bill number 613" in q_mod.lower():
        target_bill = real_bills[bill_idx % len(real_bills)]
        bill_idx += 1
        q_mod = q_mod.replace("bill 613", f"bill {target_bill}").replace("Bill 613", f"Bill {target_bill}")
        
    prepared_queries.append({
        "id": i,
        "original_query": q,
        "live_adapted_query": q_mod,
        "source": "test_suite" if i <= len(queries_ts) else "xlsx"
    })

# Write out full list to scratch/prepared_live_queries.json
os.makedirs("scratch/batches", exist_ok=True)
with open("scratch/prepared_live_queries.json", "w", encoding="utf-8") as f:
    json.dump(prepared_queries, f, indent=2)

# Partition into 100-query batches
batch_size = 100
batches = [prepared_queries[k:k+batch_size] for k in range(0, len(prepared_queries), batch_size)]

batch_summary = []
for idx, b in enumerate(batches, 1):
    b_path = f"scratch/batches/batch_{idx:02d}.json"
    with open(b_path, "w", encoding="utf-8") as f:
        json.dump(b, f, indent=2)
    batch_summary.append(f" - Batch {idx:02d}: {len(b)} queries (`{b_path}`)")

print("\n--- QUERY PREPARATION & BATCHING COMPLETE ---")
print(f"Total Prepared Queries: {len(prepared_queries)}")
print(f"Total Batches Created: {len(batches)}")
for s in batch_summary:
    print(s)
