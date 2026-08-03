import sys
import json
sys.path.insert(0, '.')
from tally_client import TallyClient

client = TallyClient()
client.update_routing_table()

comp_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

print("Fetching ledgers...")
ledgers_dict = client.fetch_ledgers(comp_name, port, from_date="01-Apr-2024", to_date="31-Mar-2025")
ledgers = list(ledgers_dict.keys())

print(f"Fetched {len(ledgers)} ledgers.")

# Fetch top bills
bills_raw = client.fetch_bills(comp_name, port, "All")
bills = list(set([b["name"] for b in bills_raw if b.get("name")]))
print(f"Fetched {len(bills)} bills.")

masters = {
    "company": comp_name,
    "port": port,
    "ledgers": ledgers,
    "bill_refs": bills,
    "stock_items": ["Raw Materials", "Finished Goods", "Packaging Materials", "Chemicals"],
    "godowns": ["Main Location", "Bhiwandi Godown", "Factory Warehouse"],
    "cost_centers": ["Reliance Job", "Project Alpha", "Marketing Expenses"],
    "voucher_types": ["Sales", "Purchase", "Receipt", "Payment", "Journal", "Contra"]
}

with open("scratch/live_tally_masters.json", "w", encoding="utf-8") as f:
    json.dump(masters, f, indent=2)

print("Master export complete!")
