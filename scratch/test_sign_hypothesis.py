import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient
from analytics_engine import AnalyticsEngine
import datetime

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000
today = datetime.datetime(2025, 11, 26)

payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>CustomBillCollection</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="CustomBillCollection">
                        <TYPE>Bill</TYPE>
                        <FETCH>Name, BillDate, BillCreditPeriod, ClosingBalance, OpeningBalance, Parent, ClearedOn</FETCH>
                        <COMPUTE>ParentGroup: $Parent:Ledger:$Parent</COMPUTE>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

res = client.execute_xml_request(port, payload)
root = ET.fromstring(res)
bills = root.findall(".//BILL")

ae = AnalyticsEngine()

# We will calculate sums under different filtering strategies:
# Strategy 1: All bills where ClosingBalance > 0
# Strategy 2: All bills where ClosingBalance < 0
# Strategy 3: All bills where ClosingBalance is positive, but net out negative ones (i.e. positive_sum - negative_sum)

s1_total = 0.0
s1_under_30 = 0.0
s1_over_30 = 0.0

s2_total = 0.0
s2_under_30 = 0.0
s2_over_30 = 0.0

s3_total = 0.0
s3_under_30 = 0.0
s3_over_30 = 0.0

for elem in bills:
    date_str = elem.findtext("BILLDATE") or ""
    due_str = elem.findtext("BILLCREDITPERIOD") or date_str
    amt = elem.findtext("CLOSINGBALANCE") or "0"
    cleared_on = elem.findtext("CLEAREDON") or ""
    
    try:
        val = float(amt.strip())
    except:
        val = 0.0
        
    dt = ae._parse_date(date_str)
    if dt == datetime.datetime.min or dt > today:
        continue
    if cleared_on.strip() != "" or val == 0:
        continue
        
    # Calculate age
    if "day" in due_str.lower():
        try:
            days_to_add = int(due_str.lower().split("day")[0].strip())
            due_dt = dt + datetime.timedelta(days=days_to_add)
        except:
            due_dt = ae._parse_date(due_str)
    else:
        due_dt = ae._parse_date(due_str)
        
    due_dt_used = due_dt if due_dt != datetime.datetime.min else dt
    age = (today - due_dt_used).days
    
    # We only count overdue bills (age > 0)
    if age > 0:
        # Strategy 1: val > 0 (strictly positive in XML)
        if val > 0:
            s1_total += val
            if age < 30:
                s1_under_30 += val
            else:
                s1_over_30 += val
                
        # Strategy 2: val < 0 (strictly negative in XML)
        if val < 0:
            abs_val = abs(val)
            s2_total += abs_val
            if age < 30:
                s2_under_30 += abs_val
            else:
                s2_over_30 += abs_val
                
        # Strategy 3: Netted (sum of all values, where positive is Credit and negative is Debit)
        # So we add positive values and subtract negative values!
        s3_val = val # positive is positive, negative is negative.
        s3_total += s3_val
        if age < 30:
            s3_under_30 += s3_val
        else:
            s3_over_30 += s3_val

print("Strategy 1 (Positive XML amounts = Payables):")
print(f" - Total Overdue: ₹ {s1_total:,.2f}")
print(f" - Overdue < 30 days: ₹ {s1_under_30:,.2f}")
print(f" - Overdue > 30 days: ₹ {s1_over_30:,.2f}")

print("\nStrategy 2 (Negative XML amounts = Payables):")
print(f" - Total Overdue: ₹ {s2_total:,.2f}")
print(f" - Overdue < 30 days: ₹ {s2_under_30:,.2f}")
print(f" - Overdue > 30 days: ₹ {s2_over_30:,.2f}")

print("\nStrategy 3 (Netted: Positive - Negative):")
print(f" - Total Overdue: ₹ {s3_total:,.2f}")
print(f" - Overdue < 30 days: ₹ {s3_under_30:,.2f}")
print(f" - Overdue > 30 days: ₹ {s3_over_30:,.2f}")
