import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

from tally_client import TallyClient
import xml.etree.ElementTree as ET

client = TallyClient()
company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# We will execute the XML request directly to see what Tally is sending back in raw form!
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
print(f"Raw Response Length: {len(res)} characters")

# Parse raw response
root = ET.fromstring(res)
bills = root.findall(".//BILL")
print(f"Total BILL tags in raw XML: {len(bills)}")

abs_sum_all = 0.0
net_sum_all = 0.0
for b in bills:
    amt = b.findtext("CLOSINGBALANCE") or "0"
    try:
        val = float(amt.strip())
    except:
        val = 0.0
    abs_sum_all += abs(val)
    net_sum_all += val

print(f"Sum of ALL bills in raw XML (Absolute): ₹ {abs_sum_all:,.2f}")
print(f"Sum of ALL bills in raw XML (Netted): ₹ {net_sum_all:,.2f}")
