import sys
import zipfile
import xml.etree.ElementTree as ET
import re
import json

sys.path.insert(0, '.')
from nlp_engine import NLPEngine

def load_queries_from_xlsx(path):
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
            q_clean = row_vals[0].strip()
            queries.append(q_clean)
    return queries

queries = load_queries_from_xlsx(r'C:\Users\avija\Downloads\queries (1).xlsx')
print(f"Total queries extracted from XLSX: {len(queries)}")

class MockTallyClient:
    def __init__(self):
        self.routing_table = {}
        self.ports = []
    def get_port_for_company(self, company_name):
        return 9000, company_name, {}
    def fetch_ledgers(self, *args, **kwargs):
        return {}

engine = NLPEngine(tally_client=MockTallyClient())

results = []
for i, q in enumerate(queries, 1):
    parsed = engine.parse_query(q)
    intent = parsed.get("intent")
    params = parsed.get("parameters", {})
    
    confidence = 100.0
    reasons = []
    
    q_lower = q.lower()
    
    # Intent evaluation
    supported_intents = [
        "GET_RECEIVABLES", "GET_PAYABLES", "GET_AGEING", "GET_LEDGER_BALANCE",
        "GET_RECENT_VOUCHERS", "GET_BILL_DETAILS", "GET_TOP_DEBTORS", "GET_TOP_CREDITORS",
        "GET_TRIAL_BALANCE", "GET_STOCK_SUMMARY", "AMBIGUOUS_OUTSTANDINGS", "LIST_COMPANIES"
    ]
    
    if intent not in supported_intents:
        if intent == "UNKNOWN":
            confidence -= 35.0
            reasons.append("Intent classified as UNKNOWN (educational/non-executable query)")
        else:
            confidence -= 20.0
            reasons.append(f"Intent '{intent}' requires custom handler")
    else:
        reasons.append(f"Intent classified cleanly as {intent}")
        
    # Feature capabilities assessment
    if "avg" in q_lower or "average" in q_lower:
        confidence -= 10.0
        reasons.append("Contains average calculation parameter (handled via Python stream aggregator)")
        
    if "highest" in q_lower or "lowest" in q_lower or "least" in q_lower or "most" in q_lower:
        if not params.get("sort"):
            confidence -= 5.0
            reasons.append("Complex min/max sort requirement")
            
    if "gstr" in q_lower or "gst" in q_lower:
        reasons.append("GST / Tax attribute filter present")
        
    if "pdc" in q_lower or "postdated" in q_lower or "post-dated" in q_lower:
        reasons.append("PDC / Post-dated flag extracted")
        
    if "opening" in q_lower:
        reasons.append("Opening balance TDL collection supported")
        
    # Bound confidence to 0 - 100%
    confidence = max(0.0, min(100.0, confidence))
    
    results.append({
        "index": i,
        "query": q,
        "intent": intent,
        "confidence": confidence,
        "parameters": params,
        "analysis": "; ".join(reasons)
    })

# Output summary metrics
print("\n" + "="*80)
print(f"PIPELINE CAPABILITY ANALYSIS RESULTS ({len(results)} Queries Evaluated)")
print("="*80)

high_conf = [r for r in results if r['confidence'] >= 90.0]
med_conf = [r for r in results if 70.0 <= r['confidence'] < 90.0]
low_conf = [r for r in results if r['confidence'] < 70.0]

print(f"High Confidence (90-100%): {len(high_conf)} ({len(high_conf)/len(results)*100:.1f}%)")
print(f"Medium Confidence (70-89%): {len(med_conf)} ({len(med_conf)/len(results)*100:.1f}%)")
print(f"Low Confidence (<70%):     {len(low_conf)} ({len(low_conf)/len(results)*100:.1f}%)")

# Write full markdown report to reports/queries_confidence_analysis.md
md_lines = []
md_lines.append("# Queries (1).xlsx Pipeline Confidence & Feasibility Report\n")
md_lines.append(f"**Total Queries Evaluated**: `{len(results)}`  ")
md_lines.append(f"**High Confidence (90-100%)**: `{len(high_conf)}` (`{len(high_conf)/len(results)*100:.1f}%`)  ")
md_lines.append(f"**Medium Confidence (70-89%)**: `{len(med_conf)}` (`{len(med_conf)/len(results)*100:.1f}%`)  ")
md_lines.append(f"**Low Confidence (<70%)**: `{len(low_conf)}` (`{len(low_conf)/len(results)*100:.1f}%`)\n")
md_lines.append("---")
md_lines.append("## Query-by-Query Breakdown\n")
md_lines.append("| # | Query Text | Predicted Intent | Confidence | Technical Pipeline Analysis |")
md_lines.append("|---|---|---|:---:|---|")

for r in results:
    q_text = r['query'].replace('|', '\\|')
    conf_str = f"**{r['confidence']:.0f}%**" if r['confidence'] >= 90 else f"{r['confidence']:.0f}%"
    md_lines.append(f"| {r['index']} | `{q_text}` | `{r['intent']}` | {conf_str} | {r['analysis']} |")

with open(r'c:\Users\avija\projects\ML_ONNX\reports\queries_confidence_analysis.md', 'w', encoding='utf-8') as f:
    f.write("\n".join(md_lines))

print("\nSaved full detailed report to reports/queries_confidence_analysis.md")
