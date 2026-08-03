import sys
import os
import json
import time
import argparse
from datetime import datetime

sys.path.insert(0, '.')
from mcp_server import _query_tally_internal, nlp_engine, tally_client, profiler

def run_batch(batch_num):
    batch_file = f"scratch/batches/batch_{batch_num:02d}.json"
    if not os.path.exists(batch_file):
        print(f"Batch file {batch_file} does not exist.")
        return

    queries = json.load(open(batch_file, encoding="utf-8"))
    print(f"\n================================================================================")
    print(f"STARTING LIVE PIPELINE EXECUTION FOR BATCH {batch_num:02d} ({len(queries)} Queries)")
    print(f"================================================================================\n")

    results = []
    
    os.makedirs(f"reports/live_testing/batch_{batch_num:02d}", exist_ok=True)
    out_json = f"reports/live_testing/batch_{batch_num:02d}/report.json"
    
    for i, item in enumerate(queries, 1):
        q_id = item["id"]
        q_text = item["live_adapted_query"]
        orig_text = item["original_query"]
        
        # We start the profiler exactly as FastMCP does
        profiler.start_pipeline()
        profiler.record_stage("Stage 1: Ingestion & Query Cleaning", {"query_len": len(q_text)})
        
        try:
            # Bypass the MCP wrapper to get the raw string and parsed NLP context dict
            parsed_ctx = nlp_engine.parse_query(q_text)
            raw_response = _query_tally_internal(q_text, profiler)
            status = "SUCCESS"
        except Exception as e:
            raw_response = f"ERROR: Execution failed with exception: {e}"
            parsed_ctx = {}
            status = "ERROR"
            
        # Stop profiler to capture timings and RAM array
        telemetry_data = profiler.stop_pipeline(q_text)
        
        # Construct the consolidated query report
        query_report = {
            "id": q_id,
            "original_query": orig_text,
            "executed_query": q_text,
            "status": status,
            "resolved_company": parsed_ctx.get("resolved_company", "N/A"),
            "resolved_ledger": parsed_ctx.get("resolved_ledger", "N/A"),
            "resolved_intent": parsed_ctx.get("intent", "N/A"),
            "date_bounds": {
                "reference_date": parsed_ctx.get("parameters", {}).get("reference_date", "N/A"),
                "date_filter": parsed_ctx.get("parameters", {}).get("date_filter", "N/A")
            },
            "output_response": raw_response.strip(),
            "telemetry": telemetry_data
        }
        
        results.append(query_report)

        # Save the comprehensive JSON array containing all queries for this batch incrementally
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)

        print(f"[{i}/{len(queries)}] Query #{q_id} processed in {telemetry_data.get('total_time_ms', 0):.1f}ms -> {status} [Peak RAM: {telemetry_data.get('stages', [{}])[-1].get('peak_ram_mb', 0)} MB]")
        time.sleep(0.2) # Tally server protection delay

    print(f"\nCompleted Batch {batch_num:02d}!")
    print(f"Saved comprehensive telemetry and output report to `{out_json}`")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Live Pipeline Batch Test")
    parser.add_argument("--batch", type=int, default=1, help="Batch number to run (1 to 13)")
    args = parser.parse_args()
    run_batch(args.batch)
