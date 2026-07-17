import sys
import os
sys.path.append(os.path.abspath('.'))

from mcp_server import _query_tally_internal

def main():
    query = "List outstanding payables whose age > 40 days on 29-nov-2025"
    print(f"Executing query E2E: '{query}'")
    
    # We call the internal handler of the MCP server
    # It should automatically update the routing table, find Modi Chemplast on Port 9001,
    # and execute the query through the pipeline.
    response = _query_tally_internal(query)
    with open("scratch/mcp_query_output.md", "w", encoding="utf-8") as f:
        f.write(response)
    print("Success: Wrote response to scratch/mcp_query_output.md")

if __name__ == "__main__":
    main()
