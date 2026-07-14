import sys
import os

# Ensure Rupee symbol prints correctly on Windows
sys.stdout.reconfigure(encoding='utf-8')

# Import the query runner from our MCP server
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from mcp_server import query_tally

def main():
    print("======================================================")
    print(" TallyPrime Semantic Query CLI (ONNX + MiniLM)")
    print("======================================================")
    print("Type your natural language query and press Enter.")
    print("Type 'exit' or 'quit' to close.")
    print("------------------------------------------------------")
    
    while True:
        try:
            query = input("\n> ")
            query_clean = query.strip()
            
            if not query_clean:
                continue
                
            if query_clean.lower() in ["exit", "quit"]:
                break
                
            print("\n[Thinking...]")
            result = query_tally(query_clean)
            print("-" * 50)
            print(result)
            print("-" * 50)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
