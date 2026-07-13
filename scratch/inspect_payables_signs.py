import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
from analytics_engine import AnalyticsEngine
from nlp_engine import NLPEngine

client = TallyClient()
engine = AnalyticsEngine()
nlp = NLPEngine(client)

# Parse parameters for: "Total overdue payable till 26-11-25"
params = nlp.parse_query("Total overdue payable till 26-11-25")["parameters"]
print("Parsed Parameters:", params)

# Fetch all payables from Port 9000 (Modi Chemplast)
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

bills = client.fetch_bills(company_name, port, "Payable", from_date=None, to_date="26-Nov-2025")
final_bills = engine.process_bills(bills, "GET_PAYABLES", params, today_str="26-Nov-2025")

abs_sum = 0.0
net_sum = 0.0
dr_bills = []
cr_bills = []

for b in final_bills:
    try:
        raw_amt = float(b["amount"])
    except:
        raw_amt = 0.0
        
    abs_amt = abs(raw_amt)
    abs_sum += abs_amt
    
    # In Tally XML, negative amounts indicate Debit (Receivable / Advance to supplier),
    # positive amounts indicate Credit (Payable).
    if raw_amt < 0: # Dr
        net_sum -= abs_amt
        dr_bills.append(b)
    else: # Cr
        net_sum += abs_amt
        cr_bills.append(b)

print(f"\nTotal Bills matched: {len(final_bills)}")
print(f"Absolute Sum: ₹ {abs_sum:,.2f}")
print(f"Netted Sum (Credit - Debit): ₹ {net_sum:,.2f}")
print(f"Number of Debit (Dr) Bills: {len(dr_bills)}")
print(f"Number of Credit (Cr) Bills: {len(cr_bills)}")

if dr_bills:
    print("\nSample Debit (Dr) Bills in Payables:")
    for b in dr_bills[:5]:
        print(f" - Bill: {b.get('name')}, Party: {b.get('party')}, Amount: ₹ {b.get('amount')} (Dr), Age: {b.get('age_days')}d")
