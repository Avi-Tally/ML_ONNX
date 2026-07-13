import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
from analytics_engine import AnalyticsEngine
from nlp_engine import NLPEngine

client = TallyClient()
client.update_routing_table()

# Use Bella Casa on port 9001
company = "Bella Casa Data for User Activity"
port = 9001

engine = NLPEngine(client)
query = "List outstanding payable amount whose age < 40 days on 08-Oct-2017"
parsed = engine.parse_query(query)
params = parsed["parameters"]

print("Parsed parameters:", params)

# Fetch actual bills
bills = client.fetch_bills(company, port, report_type="Payable")
print(f"Total bills fetched: {len(bills)}")

analytics = AnalyticsEngine()
processed = analytics.process_bills(bills, parsed["intent"], params, today_str=params["reference_date"])

print(f"Total bills after processing/filtering: {len(processed)}")

negative_age_bills = [b for b in processed if b["age_days"] < 0]
print(f"Negative age bills: {len(negative_age_bills)}")
for b in negative_age_bills[:5]:
    print(f"Name: {b['name']} | Party: {b['party']} | Age: {b['age_days']}")
    
positive_age_bills = [b for b in processed if b["age_days"] >= 0]
print(f"Positive/Zero age bills (correctly included): {len(positive_age_bills)}")
for b in positive_age_bills[:5]:
    print(f"Name: {b['name']} | Party: {b['party']} | Age: {b['age_days']}")
