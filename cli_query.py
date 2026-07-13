import os
import sys
from mcp_server import query_tally
from tally_client import TallyClient

def main():
    print("=" * 65)
    print("TallyPrime Local NLP Bridge - Interactive Manual Test CLI")
    print("=" * 65)
    print("Detecting running TallyPrime instances...")
    
    client = TallyClient()
    if not client.routing_table:
        print("ERROR: No active TallyPrime HTTP servers detected on ports 9000 or 9001.")
        print("Please verify that TallyPrime is running and HTTP configuration is enabled.")
        sys.exit(1)
        
    print("\nConnected Instances discovered:")
    for comp_lower, info in client.routing_table.items():
        print(f" - Port {info['port']} -> {info['name']}")
    print("=" * 65)
    print("Type your financial query in plain English (e.g. 'balance of aarkay', 'show stock summary')")
    print("To switch companies explicitly, add 'for Bella Casa' or 'for Modi Chemplast' to the query.")
    print("Type 'exit' or 'quit' to close.")
    print("=" * 65)
    
    while True:
        try:
            query = input("\nQuery > ")
            if not query.strip():
                continue
            if query.lower() in ['exit', 'quit', 'q']:
                print("Goodbye!")
                break
                
            # Execute the same tool method that the MCP server exposes
            response = query_tally(query)
            print("\nResponse:")
            print(response)
            print("-" * 65)
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError executing query: {e}")

if __name__ == "__main__":
    main()
