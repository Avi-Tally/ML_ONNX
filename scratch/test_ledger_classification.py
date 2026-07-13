import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
import xml.etree.ElementTree as ET

client = TallyClient()

def get_group_parents(port, company_name):
    payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>GroupParents</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="GroupParents">
                        <TYPE>Group</TYPE>
                        <FETCH>Name, Parent</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""
    try:
        response_xml = client.execute_xml_request(port, payload)
        root = ET.fromstring(response_xml)
        group_parents = {}
        for g in root.findall(".//GROUP"):
            name = g.attrib.get("NAME", "").strip().lower()
            parent = g.findtext("PARENT", "").strip().lower()
            if name:
                group_parents[name] = parent
        return group_parents
    except Exception as e:
        print(f"Error fetching groups for {company_name}: {e}")
        return {}

def classify_bill(bill, group_parents):
    pg = bill.get("parent_group", "").strip().lower()
    party = bill.get("party", "").strip().lower()
    
    # Recursive check helper
    def belongs_to(grp, targets):
        curr = grp
        visited = set()
        while curr and curr not in visited:
            if any(t in curr for t in targets):
                return True
            visited.add(curr)
            curr = group_parents.get(curr, "")
        return False

    # 1. Check recursive hierarchy
    is_creditor_group = belongs_to(pg, ["sundry creditors", "trade payables", "creditors"])
    is_debtor_group = belongs_to(pg, ["sundry debtors", "trade receivables", "debtors"])
    
    if is_creditor_group and not is_debtor_group:
        return "Payable"
    if is_debtor_group and not is_creditor_group:
        return "Receivable"
        
    # 2. Keyword checks on group name
    if any(w in pg for w in ["creditor", "payable", "supplier", "vendor"]):
        return "Payable"
    if any(w in pg for w in ["debtor", "receivable", "customer", "client", "sales"]):
        return "Receivable"
        
    # 3. Keyword checks on party name
    if any(w in party for w in ["creditor", "supplier", "vendor"]):
        return "Payable"
    if any(w in party for w in ["debtor", "customer", "client"]):
        return "Receivable"
        
    # 4. Fallback to amount sign
    try:
        amt = float(bill.get("amount", "0"))
    except:
        amt = 0.0
    return "Payable" if amt > 0 else "Receivable"

# Test on Bella Casa
port = 9001
company_name = "Bella Casa Data for User Activity"
group_parents = get_group_parents(port, company_name)
bills = client.fetch_bills(company_name, port, "All")
print(f"\nBella Casa:")
print(f"Total bills: {len(bills)}")

payables = 0
receivables = 0
for b in bills:
    c = classify_bill(b, group_parents)
    if c == "Payable":
        payables += 1
    else:
        receivables += 1
print(f"Classified Payables: {payables}, Receivables: {receivables}")
