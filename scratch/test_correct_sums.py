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

def get_group_hierarchy_map(company, port):
    payload = f"""<ENVELOPE>
        <HEADER>
            <VERSION>1</VERSION>
            <TALLYREQUEST>Export</TALLYREQUEST>
            <TYPE>Collection</TYPE>
            <ID>GroupList</ID>
        </HEADER>
        <BODY>
            <DESC>
                <STATICVARIABLES>
                    <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                    <SVCURRENTCOMPANY>{company}</SVCURRENTCOMPANY>
                </STATICVARIABLES>
                <TDL>
                    <TDLMESSAGE>
                        <COLLECTION NAME="GroupList">
                            <TYPE>Group</TYPE>
                            <FETCH>Name, Parent</FETCH>
                        </COLLECTION>
                    </TDLMESSAGE>
                </TDL>
            </DESC>
        </BODY>
    </ENVELOPE>"""
    res = client.execute_xml_request(port, payload)
    root = ET.fromstring(res)
    groups = root.findall(".//GROUP")
    group_parents = {}
    for g in groups:
        name = g.findtext("NAME") or g.attrib.get("NAME", "")
        parent = g.findtext("PARENT") or ""
        if name:
            group_parents[name.strip().lower()] = parent.strip().lower()
    return group_parents

group_map = get_group_hierarchy_map(company_name, port)

# 2. Fetch all raw bills
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

def is_group_under(group_name, target_parent, g_map):
    curr = group_name.strip().lower()
    target = target_parent.strip().lower()
    visited = set()
    while curr and curr not in visited:
        if curr == target:
            return True
        visited.add(curr)
        curr = g_map.get(curr)
    return False

payables = []
for elem in bills:
    name = elem.findtext("NAME") or ""
    party = elem.findtext("PARENT") or ""
    date_str = elem.findtext("BILLDATE") or ""
    due_str = elem.findtext("BILLCREDITPERIOD") or date_str
    amt = elem.findtext("CLOSINGBALANCE") or "0"
    parent_group = elem.findtext("PARENTGROUP") or ""
    cleared_on = elem.findtext("CLEAREDON") or ""
    
    try:
        val = float(amt.strip())
    except:
        val = 0.0
        
    dt = ae._parse_date(date_str)
    # Filter till 26-Nov-2025
    if dt == datetime.datetime.min or dt > today:
        continue
        
    is_cleared = (cleared_on.strip() != "" or val == 0)
    if is_cleared:
        continue
        
    # In Tally:
    # A bill belongs to Payables if its ledger parent group is under "Sundry Creditors".
    # BUT wait! What if the ledger group is Sundry Debtors but the bill is Credit (negative)?
    # Wait, in the screenshot:
    # The bills under Bills Payable include RELIANCE NEW SOLAR ENERGY LIMITED (which is Sundry Debtors!).
    # So Tally's Bills Payable includes BOTH:
    # 1. Ledgers under Sundry Creditors (regardless of bill sign).
    # 2. Ledgers under Sundry Debtors but ONLY if their bill sign is Credit (negative)!
    # Let's check:
    # If the ledger is under Sundry Debtors, it normally has Debit (positive) bills.
    # But if it has a Credit (negative) bill, it is a payable to that customer (advance/credit note).
    # So it should be included in Bills Payable!
    # And conversely, for Bills Receivable:
    # 1. Ledgers under Sundry Debtors (regardless of bill sign).
    # 2. Ledgers under Sundry Creditors but ONLY if their bill sign is Debit (positive) (advances/debit notes to suppliers)!
    # Let's check if this is exactly how Tally defines Payables and Receivables!
    # Let's run this classification logic:
    
    is_creditor_ledger = is_group_under(parent_group, "Sundry Creditors", group_map)
    is_debtor_ledger = is_group_under(parent_group, "Sundry Debtors", group_map)
    
    is_payable_bill = False
    if is_creditor_ledger:
        is_payable_bill = True
    elif is_debtor_ledger and val < 0: # Debtor advance/credit note is a payable!
        is_payable_bill = True
        
    if is_payable_bill:
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
        
        payables.append({
            "name": name,
            "party": party,
            "amount": val,
            "age_days": age,
            "is_creditor_ledger": is_creditor_ledger
        })

print(f"Total payables matched in Python: {len(payables)}")

total_pending = 0.0
under_30 = 0.0
over_30 = 0.0

for p in payables:
    # How to compute the outstanding value for the payable?
    # In Tally XML:
    # - Credit is negative (e.g. -3388.00). In payables, a Credit is a positive payable amount. So net_val = -amount.
    # - Debit is positive (e.g. 17855.00). In payables, a Debit is a negative payable (advance). So net_val = -amount.
    # So net_val is ALWAYS -amount!
    net_val = -p["amount"]
    age = p["age_days"]
    
    # Overdue means age > 0.
    if age > 0:
        total_pending += net_val
        if age <= 30: # Wait, is it <= 30 or < 30? The screenshot says "< 30 days" and "> 30 days".
            # Let's check both options to see which matches the screenshot!
            under_30 += net_val
        else:
            over_30 += net_val

print(f"\nCalculated Totals:")
print(f" - Total Pending Overdue: ₹ {total_pending:,.2f}")
print(f" - Overdue <= 30 days: ₹ {under_30:,.2f}")
print(f" - Overdue > 30 days: ₹ {over_30:,.2f}")
