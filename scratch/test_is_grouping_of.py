import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
import xml.etree.ElementTree as ET

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Let's test different compute formulas for IsPayable / IsReceivable on the Bill collection!
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
                        <FETCH>Name, BillDate, ClosingBalance, Parent</FETCH>
                        <COMPUTE>IsPayable: $$IsGroupingOf:$$GroupSundryCreditors:$ParentGroup:Ledger:$Parent</COMPUTE>
                        <COMPUTE>IsReceivable: $$IsGroupingOf:$$GroupSundryDebtors:$ParentGroup:Ledger:$Parent</COMPUTE>
                        <COMPUTE>BillType: $BillType</COMPUTE>
                        <COMPUTE>ParentGroup: $ParentGroup:Ledger:$Parent</COMPUTE>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

res = client.execute_xml_request(port, payload)
root = ET.fromstring(res)
bills = root.findall(".//BILL")

print(f"Total bills: {len(bills)}")
print("Sample Bills with computed IsPayable/IsReceivable:")
for b in bills[:10]:
    name = b.findtext("NAME")
    party = b.findtext("PARENT")
    is_p = b.findtext("ISPAYABLE")
    is_r = b.findtext("ISRECEIVABLE")
    b_type = b.findtext("BILLTYPE")
    p_group = b.findtext("PARENTGROUP")
    amt = b.findtext("CLOSINGBALANCE")
    print(f" - Bill: {name}, Party: {party}, ParentGroup: {p_group}, Amt: {amt}, IsPayable: {is_p}, IsReceivable: {is_r}, BillType: {b_type}")
