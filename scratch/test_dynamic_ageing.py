import sys
import os
import codecs
sys.stdout.reconfigure(encoding='utf-8')

# Add workspace to path
sys.path.append(os.path.abspath('.'))

from mcp_server import query_tally

query = "Give me bills in the ageing buckets of 30 60 90 180 days for Jagat based on bill date with amount less than 5000000 showing top 20 sorted by due date descending"

print("==================================================")
print("Executing Custom Ageing Query:")
print(f"'{query}'")
print("==================================================")

response = query_tally(query)
print("\nResponse:")
print(response)
print("==================================================")
