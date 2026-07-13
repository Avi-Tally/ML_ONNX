from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tally_client import TallyClient
from nlp_engine import NLPEngine
from mcp_server import _query_tally_internal

app = FastAPI(title="TallyPrime NLP Bridge REST API", version="1.0.0")

# Reuse NLPEngine and TallyClient from mcp_server to avoid duplicate initialization
from mcp_server import tally_client, nlp_engine

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query: str
    intent: str
    company: str | None
    port: int | None
    resolved_ledger: str | None
    raw_response: str

@app.get("/companies")
def get_companies():
    """List all active TallyPrime companies and their active ports."""
    try:
        tally_client.update_routing_table()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to query TallyPrime: {e}")
    
    if not tally_client.routing_table:
        return {"companies": [], "message": "No active TallyPrime instances detected."}
    
    return {
        "companies": [
            {
                "name": info["name"],
                "port": info["port"],
                "context": info.get("context", {})
            }
            for info in tally_client.routing_table.values()
        ]
    }

@app.post("/query", response_model=QueryResponse)
def execute_query(request: QueryRequest):
    """Execute a natural language query against TallyPrime and return parsed metadata and the raw markdown response."""
    try:
        tally_client.update_routing_table()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update routing: {e}")
        
    if not tally_client.routing_table:
        raise HTTPException(status_code=503, detail="No active TallyPrime instances detected.")

    try:
        parsed = nlp_engine.parse_query(request.query)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"NLP Parser Error: {e}")

    try:
        response_markdown = _query_tally_internal(request.query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Execution Error: {e}")

    return QueryResponse(
        query=request.query,
        intent=parsed.get("intent", "UNKNOWN"),
        company=parsed.get("resolved_company"),
        port=parsed.get("port"),
        resolved_ledger=parsed.get("resolved_ledger"),
        raw_response=response_markdown
    )

@app.post("/parse")
def parse_query_only(request: QueryRequest):
    """Parse a natural language query and return the raw NLPEngine analysis JSON (ONNX + heuristics) without executing it against Tally."""
    try:
        parsed = nlp_engine.parse_query(request.query)
        return parsed
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"NLP Parser Error: {e}")

@app.get("/health")
def health_check():
    """Health check for service and Tally connection status."""
    try:
        tally_client.update_routing_table()
        tally_ok = len(tally_client.routing_table) > 0
    except:
        tally_ok = False
        
    return {
        "status": "healthy",
        "tally_connection": "connected" if tally_ok else "disconnected",
        "active_companies": len(tally_client.routing_table) if tally_ok else 0
    }
