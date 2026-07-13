import time
import sys
sys.stdout.reconfigure(encoding='utf-8')

from mcp_server import _query_tally_internal

def test():
    query = "What is the balance outstanding for bill 613 in Modi Chemplast as of today?"
    print(f"Query: {query}")
    print(_query_tally_internal(query))
    
    print("-" * 40)
    query = "What is the balance outstanding for bill MCPMPL/1206/15-16 in Modi Chemplast?"
    print(f"Query: {query}")
    print(_query_tally_internal(query))

if __name__ == "__main__":
    test()
