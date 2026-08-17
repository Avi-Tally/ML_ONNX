import os
import sys
import io
import json
import re

# Ensure UTF-8 output encoding across Windows PowerShell and CMD
if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'buffer'):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

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
                            current_query = f"{current_query} $C({selected})"
                        elif amb_type == "LEDGER_SELECTION":
                            extracted = payload.get("extracted") or ""
                            if extracted and extracted.lower() in current_query.lower():
                                pattern = re.compile(re.escape(extracted), re.IGNORECASE)
                                current_query = pattern.sub(f"$L({selected})", current_query, count=1)
                            else:
                                current_query = f"{current_query} $L({selected})"
                        elif amb_type == "DIRECTIONAL_SELECTION":
                            if "payable" in selected.lower():
                                current_query = f"{current_query} payables"
                            else:
                                current_query = f"{current_query} receivables"
                        elif amb_type == "DATE_SELECTION":
                            if "today" in selected.lower():
                                current_query = f"{current_query} as of today"
                            elif "specific date" in selected.lower():
                                user_date = input("Enter specific date (e.g. 11-Aug-2017): ").strip()
                                current_query = f"{current_query} on {user_date}"
                            elif "fiscal year" in selected.lower():
                                user_fy = input("Enter fiscal year (e.g. FY 17-18): ").strip()
                                current_query = f"{current_query} for {user_fy}"
                            elif "month" in selected.lower():
                                user_month = input("Enter month (e.g. Aug 2017): ").strip()
                                current_query = f"{current_query} in {user_month}"
                            elif "custom" in selected.lower() or "range" in selected.lower():
                                user_range = input("Enter date range (e.g. from 01-Apr-2017 to 11-Aug-2017): ").strip()
                                current_query = f"{current_query} {user_range}"
                        print(f"--> Re-submitting query: '{current_query}'")
                        continue
                else:
                    # Allow user to directly type their date or clarification text
                    if amb_type == "DATE_SELECTION":
                        current_query = f"{current_query} {choice}"
                        print(f"--> Re-submitting query: '{current_query}'")
                        continue
                print("Invalid selection. Please try again.")
                continue
            except Exception as e:
                print(f"[Ambiguity Handler Error]: {e}")
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
