import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET
from tally_client import TallyClient

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# We will execute the XML request directly to fetch all bills with their ParentGroup
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

creditor_bills = []
debtor_bills = []

import datetime
today = datetime.datetime(2025, 11, 26)
from analytics_engine import AnalyticsEngine
ae = AnalyticsEngine()

for elem in bills:
    name = elem.findtext("NAME") or ""
    party = elem.findtext("PARENT") or ""
    date_str = elem.findtext("BILLDATE") or ""
    due_str = elem.findtext("BILLCREDITPERIOD") or date_str
    amt = elem.findtext("CLOSINGBALANCE") or "0"
    open_amt = elem.findtext("OPENINGBALANCE") or "0"
    parent_group = elem.findtext("PARENTGROUP") or ""
    cleared_on = elem.findtext("CLEAREDON") or ""
    
    try:
        val = float(amt.strip())
    except:
        val = 0.0
        
    try:
        open_val = float(open_amt.strip())
    except:
        open_val = 0.0
        
    # Parse dates
    dt = ae._parse_date(date_str)
    
    # Calculate due date
    if "day" in due_str.lower():
        try:
            days_to_add = int(due_str.lower().split("day")[0].strip())
            due_dt = dt + datetime.timedelta(days=days_to_add)
        except:
            due_dt = ae._parse_date(due_str)
    else:
        due_dt = ae._parse_date(due_str)
        
    due_dt_used = due_dt if due_dt != datetime.datetime.min else dt
    age_days = (today - due_dt_used).days
    
    is_cleared = cleared_on.strip() != "" or val == 0
    
    # We only care about pending (non-cleared) bills that are dated <= 26-Nov-2025
    if dt == datetime.datetime.min or dt > today:
        continue
    if is_cleared:
        continue
        
    bill_info = {
        "name": name,
        "party": party,
        "date": date_str,
        "due_date": due_str,
        "amount": val,
        "opening_amount": open_val,
        "parent_group": parent_group,
        "age_days": age_days
    }
    
    if "creditor" in parent_group.lower():
        creditor_bills.append(bill_info)
    elif "debtor" in parent_group.lower():
        debtor_bills.append(bill_info)

print(f"Total Creditor pending bills: {len(creditor_bills)}")
print(f"Total Debtor pending bills: {len(debtor_bills)}")

# Now let's calculate:
# 1. Total Payables till 26-Nov-2025
# 2. Overdue Payables till 26-Nov-2025 (age > 0)
# 3. Overdue Payables age < 30 days (0 < age < 30)
# 4. Overdue Payables age > 30 days (age > 30)

total_all = 0.0
total_overdue = 0.0
total_under_30 = 0.0
total_over_30 = 0.0

for b in creditor_bills:
    # In Tally, Credit is positive and Debit is negative for payables.
    # Outstanding report nets them out.
    amt = b["amount"]
    age = b["age_days"]
    
    total_all += amt
    if age > 0:
        total_overdue += amt
        if age <= 30:
            total_under_30 += amt
        else:
            total_over_30 += amt

print(f"\nCalculated Creditor Outstanding:")
print(f" - Total Outstanding: ₹ {total_all:,.2f}")
print(f" - Total Overdue (age > 0): ₹ {total_overdue:,.2f}")
print(f" - Overdue <= 30 days: ₹ {total_under_30:,.2f}")
print(f" - Overdue > 30 days: ₹ {total_over_30:,.2f}")
