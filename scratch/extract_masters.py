import sys
import json
import xml.etree.ElementTree as ET

sys.path.insert(0, '.')
from tally_client import TallyClient

def get_collection(client, port, company, coll_name, fetch_fields):
    payload = f"""<ENVELOPE>
    <HEADER><VERSION>1</VERSION><TALLYREQUEST>Export</TALLYREQUEST><TYPE>Collection</TYPE><ID>{coll_name}</ID></HEADER>
    <BODY><DESC>
        <STATICVARIABLES><SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT><SVCURRENTCOMPANY>{company}</SVCURRENTCOMPANY></STATICVARIABLES>
        <TDL><TDLMESSAGE>
            <COLLECTION NAME="{coll_name}">
                <TYPE>{coll_name.replace('List', '')}</TYPE>
                <FETCH>{fetch_fields}</FETCH>
            </COLLECTION>
        </TDLMESSAGE></TDL>
    </DESC></BODY>
    </ENVELOPE>"""
    try:
        res = client.execute_xml_request(port, payload, timeout=5.0)
        root = ET.fromstring(res)
        items = []
        for elem in root.findall(f".//{coll_name.replace('List', '').upper()}"):
            name = elem.findtext("NAME") or elem.attrib.get("NAME", "")
            if name:
                items.append(name.strip())
        return list(set(items))
    except Exception as e:
        print(f"Error fetching {coll_name}: {e}")
        return []

client = TallyClient()
if not client.routing_table:
    print("No active Tally companies found.")
    sys.exit(1)

port, company, ctx = client.get_port_for_company()
print(f"Connected to Tally port {port}, company: {company}")

masters = {
    "ledgers": get_collection(client, port, company, "Ledger", "Name"),
    "cost_centres": get_collection(client, port, company, "CostCentre", "Name"),
    "stock_items": get_collection(client, port, company, "StockItem", "Name"),
    "stock_categories": get_collection(client, port, company, "StockCategory", "Name"),
    "godowns": get_collection(client, port, company, "Godown", "Name")
}

with open("scratch/tally_masters.json", "w", encoding="utf-8") as f:
    json.dump(masters, f, indent=2)

print("Saved Tally masters to scratch/tally_masters.json")
