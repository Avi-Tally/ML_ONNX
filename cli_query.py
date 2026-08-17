import os
import sys
import json
from mcp_server import query_tally
from tally_client import TallyClient

def execute_with_interactivity(query: str) -> str:
    """
    Executes a query via query_tally and intercepts __AMBIGUITY__: responses.
    Presents an interactive numbered menu in CLI to get user clarification and re-submits automatically.
    """
    current_query = query
    while True:
        response = query_tally(current_query)
        if isinstance(response, str) and response.startswith("__AMBIGUITY__:"):
            raw_json = response[len("__AMBIGUITY__:"):]
            try:
                payload = json.loads(raw_json)
                amb_type = payload.get("type")
                prompt = payload.get("prompt")
                options = payload.get("options", [])
                
                print(f"\n[CLARIFICATION REQUIRED] {prompt}")
                for idx, opt in enumerate(options, 1):
                    print(f"  [{idx}] {opt}")
                print("  [c] Cancel query")
                
                choice = input("\nSelection > ").strip()
                if choice.lower() == 'c':
                    return "Query cancelled by user."
                
                if choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(options):
                        selected = options[idx]
                        if amb_type == "COMPANY_SELECTION":
                            current_query = f"{current_query} for {selected}"
                        elif amb_type == "LEDGER_SELECTION":
                            current_query = f"{current_query} for {selected}"
                        elif amb_type == "DIRECTIONAL_SELECTION":
                            if "payable" in selected.lower():
                                current_query = f"{current_query} payables"
                            else:
                                current_query = f"{current_query} receivables"
                        print(f"--> Re-submitting query: '{current_query}'")
                        continue
                print("Invalid selection. Please try again.")
                continue
            except Exception as e:
                return response
        else:
            return response

def main():
    print("=" * 65)
    print("TallyPrime Local NLP Bridge - Interactive Manual Test CLI")
    print("=" * 65)
    print("Detecting running TallyPrime instances...")
    
    client = TallyClient()
    if not client.routing_table:
        port_range_str = f"{min(client.ports)}-{max(client.ports)}" if client.ports else "configured ports"
        print(f"ERROR: No active TallyPrime HTTP servers detected on ports {port_range_str}.")
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
                
            # Execute with interactive disambiguation menu handler
            response = execute_with_interactivity(query)
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
