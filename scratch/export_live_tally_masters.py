import sys
import json
import xml.etree.ElementTree as ET

sys.path.insert(0, '.')
from tally_client import TallyClient

client = TallyClient()
client.update_routing_table()

masters = {
    "companies": list(client.routing_table.keys()),
    "ledgers": [],
    "bill_refs": [],
    "stock_items": [],
    "godowns": [],
    "cost_centers": [],
    "voucher_types": ["Sales", "Purchase", "Receipt", "Payment", "Journal", "Contra"]
}

for comp_key, info in client.routing_table.items():
    comp_name = info["name"]
    port = info["port"]
    print(f"Exporting masters for {comp_name} on port {port}...")
    
    # 1. Ledgers
    try:
        ledgers = client.fetch_ledgers(comp_name, port)
        for l in ledgers.keys():
            if l and l not in masters["ledgers"]:
                masters["ledgers"].append(l)
        print(f"  Exported {len(ledgers)} ledgers.")
    except Exception as e:
        print(f"  Error fetching ledgers: {e}")

    # 2. Bills
    try:
        bills = client.fetch_bills(comp_name, port, report_type="All")
        for b in bills:
            b_name = b.get("name")
            if b_name and b_name not in masters["bill_refs"]:
                masters["bill_refs"].append(b_name)
        print(f"  Exported {len(bills)} bills.")
    except Exception as e:
        print(f"  Error fetching bills: {e}")

    # 3. Stock Items
    try:
        payload_stock = """<ENVELOPE>
            <HEADER><TALLYREQUEST>Export Data</TALLYREQUEST></HEADER>
            <BODY>
                <EXPORTDATA>
                    <REQUESTDESC>
                        <REPORTNAME>List of Accounts</REPORTNAME>
                        <STATICVARIABLES>
                            <SVEXPLICITSTATIONARY>No</SVEXPLICITSTATIONARY>
                            <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                            <ACCOUNTTYPE>Stock Items</ACCOUNTTYPE>
                        </STATICVARIABLES>
                    </REQUESTDESC>
                </EXPORTDATA>
            </BODY>
        </ENVELOPE>"""
        res = client.execute_xml_request(port, payload_stock)
        if res:
            root = ET.fromstring(res)
            for item in root.findall(".//STOCKITEM"):
                name = item.attrib.get("NAME") or item.findtext("NAME")
                if name and name.strip() not in masters["stock_items"]:
                    masters["stock_items"].append(name.strip())
        print(f"  Exported {len(masters['stock_items'])} stock items.")
    except Exception as e:
        print(f"  Error fetching stock items: {e}")

    # 4. Godowns
    try:
        payload_godown = """<ENVELOPE>
            <HEADER><TALLYREQUEST>Export Data</TALLYREQUEST></HEADER>
            <BODY>
                <EXPORTDATA>
                    <REQUESTDESC>
                        <REPORTNAME>List of Accounts</REPORTNAME>
                        <STATICVARIABLES>
                            <SVEXPLICITSTATIONARY>No</SVEXPLICITSTATIONARY>
                            <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                            <ACCOUNTTYPE>Godowns</ACCOUNTTYPE>
                        </STATICVARIABLES>
                    </REQUESTDESC>
                </EXPORTDATA>
            </BODY>
        </ENVELOPE>"""
        res = client.execute_xml_request(port, payload_godown)
        if res:
            root = ET.fromstring(res)
            for g in root.findall(".//GODOWN"):
                name = g.attrib.get("NAME") or g.findtext("NAME")
                if name and name.strip() not in masters["godowns"]:
                    masters["godowns"].append(name.strip())
        print(f"  Exported {len(masters['godowns'])} godowns.")
    except Exception as e:
        print(f"  Error fetching godowns: {e}")

    # 5. Cost Centres
    try:
        payload_cc = """<ENVELOPE>
            <HEADER><TALLYREQUEST>Export Data</TALLYREQUEST></HEADER>
            <BODY>
                <EXPORTDATA>
                    <REQUESTDESC>
                        <REPORTNAME>List of Accounts</REPORTNAME>
                        <STATICVARIABLES>
                            <SVEXPLICITSTATIONARY>No</SVEXPLICITSTATIONARY>
                            <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                            <ACCOUNTTYPE>Cost Centres</ACCOUNTTYPE>
                        </STATICVARIABLES>
                    </REQUESTDESC>
                </EXPORTDATA>
            </BODY>
        </ENVELOPE>"""
        res = client.execute_xml_request(port, payload_cc)
        if res:
            root = ET.fromstring(res)
            for cc in root.findall(".//COSTCENTRE"):
                name = cc.attrib.get("NAME") or cc.findtext("NAME")
                if name and name.strip() not in masters["cost_centers"]:
                    masters["cost_centers"].append(name.strip())
        print(f"  Exported {len(masters['cost_centers'])} cost centers.")
    except Exception as e:
        print(f"  Error fetching cost centers: {e}")

with open("scratch/live_tally_masters.json", "w", encoding="utf-8") as f:
    json.dump(masters, f, indent=2)

print("\n--- MASTER EXPORT FINISHED ---")
print(f"Saved {len(masters['ledgers'])} ledgers, {len(masters['bill_refs'])} bills, {len(masters['stock_items'])} stock items, {len(masters['godowns'])} godowns, {len(masters['cost_centers'])} cost centers to scratch/live_tally_masters.json")
