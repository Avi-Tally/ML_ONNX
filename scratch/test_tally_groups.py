from tally_client import TallyClient

client = TallyClient()
port = client.routing_table[list(client.routing_table.keys())[0]]["port"]
company = client.routing_table[list(client.routing_table.keys())[0]]["name"]

payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>GroupListWithBalance</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="GroupListWithBalance">
                        <TYPE>Group</TYPE>
                        <FETCH>Name, ClosingBalance</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

res = client.execute_xml_request(port, payload)
import xml.etree.ElementTree as ET
root = ET.fromstring(res)
for group_elem in root.findall(".//GROUP")[:10]:
    name = group_elem.findtext("NAME") or group_elem.attrib.get("NAME", "")
    bal = group_elem.findtext("CLOSINGBALANCE") or "0.00"
    print(f"Group: {name} | Balance: {bal}")
