import time
from tally_client import TallyClient
from nlp_engine import NLPEngine

def test():
    tally = TallyClient()
    tally.update_routing_table()
    for name, info in tally.routing_table.items():
        print(f"Company: {name}")
        start = time.time()
        try:
            bills = tally.fetch_bills(info['name'], info['port'], "All", None, None)
            print(f"Fetched {len(bills)} bills in {time.time()-start:.2f}s")
        except Exception as e:
            print(f"Failed to fetch bills: {e}")

if __name__ == "__main__":
    test()
