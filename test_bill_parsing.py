import sys
from mcp_server import _query_tally_internal

def test():
    query = "What is the balance outstanding for bill 613 as of today?"
    print(f"Query 1: {query}")
    print(_query_tally_internal(query))
    print("-" * 50)

    query = "Display the Opening Amount, pending and final balance of payables as on 02-03-2025"
    print(f"Query 2: {query}")
    print(_query_tally_internal(query))
    print("-" * 50)

    query = "What is the status of bill 52?"
    print(f"Query 3: {query}")
    print(_query_tally_internal(query))

if __name__ == "__main__":
    test()
