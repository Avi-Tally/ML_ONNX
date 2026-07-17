import sys
import os
sys.path.append(os.path.abspath('.'))

import json
from mcp_server import _query_tally_internal
from tally_client import TallyClient

def main():
    client = TallyClient()
    company = "Modi Chemplast Materials Pvt Ltd"
    port = 9001
    date = "29-Nov-2025"
    
    bills = client.fetch_bills(
        company, 
        port, 
        report_type="Payable", 
        status_filter="pending", 
        reference_date=date,
        exclude_pdc=True
    )
    
    # Check for the 5 target bills cleared by Receipt #368
    target_refs = ["MODI/25-26/231", "MODI/25-26/440", "MODI/25-26/439", "MODI/25-26/438", "MODI/25-26/426"]
    
    print("Checking if the 5 post-dated bills are excluded (when exclude_pdc=True):")
    for r in target_refs:
        matching = [b for b in bills if b.get("name") == r]
        if matching:
            print(f"  Ref: {r} is PRESENT (Closing Bal: {matching[0].get('amount')})")
        else:
            print(f"  Ref: {r} is EXCLUDED (Cleared by post-dated voucher)")

if __name__ == "__main__":
    main()
