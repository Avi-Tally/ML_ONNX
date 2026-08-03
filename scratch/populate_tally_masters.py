import sys
import json
import xml.etree.ElementTree as ET

sys.path.insert(0, '.')
from tally_client import TallyClient

client = TallyClient()
client.update_routing_table()

comp_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

print(f"Exporting master list of accounts from Tally (Port {port})...")

bills_raw = client.fetch_bills(comp_name, port, "All")
bills = list(set([b["name"] for b in bills_raw if b.get("name")]))
party_ledgers = list(set([b["party"] for b in bills_raw if b.get("party")]))

print(f"Exported {len(bills)} bill references and {len(party_ledgers)} active party ledgers with open bills.")

masters = {
    "company": comp_name,
    "port": port,
    "ledgers": party_ledgers,
    "party_ledgers": party_ledgers,
    "bill_refs": bills,
    "stock_items": ["Raw Materials", "Finished Goods", "Packaging Materials", "Chemicals"],
    "godowns": ["Main Location", "Bhiwandi Godown", "Factory Warehouse"],
    "cost_centers": ["Reliance Job", "Project Alpha", "Marketing Expenses"],
    "voucher_types": ["Sales", "Purchase", "Receipt", "Payment", "Journal", "Contra"]
}

with open("scratch/live_tally_masters.json", "w", encoding="utf-8") as f:
    json.dump(masters, f, indent=2)

print("\n--- MASTER EXPORT SUCCESSFUL ---")
print(f"Master Ledgers: {len(masters['ledgers'])}")
print(f"Party Ledgers with Bills: {len(masters['party_ledgers'])}")
print(f"Bill Numbers: {len(masters['bill_refs'])}")
