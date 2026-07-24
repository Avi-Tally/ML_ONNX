# ==============================================================================
# MODULE: CHRONOLOGICAL PIPELINE TELEMETRY PROFILER (pipeline_profiler.py)
# 
# PURPOSE:
#   Tracks, measures, and logs latency (nanoseconds/milliseconds) and memory usage
#   (RAM allocation in MB) for LITERALLY EVERY STAGE of the live query pipeline.
#
# METRICS TRACKED PER STAGE:
#   - Stage Name & Sequence Index
#   - Elapsed Duration (Δt in milliseconds via time.perf_counter_ns)
#   - Current Heap RAM Allocation (via tracemalloc)
#   - Peak Heap RAM Allocation (via tracemalloc)
#   - RAM Delta (ΔRAM in MB)
# ==============================================================================

import time
import tracemalloc
import json
import os
from datetime import datetime

class PipelineProfiler:
    """
    High-precision nanosecond latency and RAM profiler for the NLP & TDL execution engine.
    """
    def __init__(self, log_path=None):
        if log_path is None:
            log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "telemetry.jsonl")
        self.log_path = log_path
        self.stages = []
        self.start_total_ns = 0
        self.is_tracing = False

    def start_pipeline(self):
        """Starts the global pipeline timer and memory tracker."""
        self.stages = []
        self.start_total_ns = time.perf_counter_ns()
        if not tracemalloc.is_tracing():
            tracemalloc.start()
            self.is_tracing = True
        else:
            self.is_tracing = False

    def record_stage(self, stage_name: str, details: dict = None):
        """Records a single stage's time and memory metrics chronologically."""
        now_ns = time.perf_counter_ns()
        prev_ns = self.stages[-1]["end_ns"] if self.stages else self.start_total_ns
        delta_t_ms = (now_ns - prev_ns) / 1e6
        
        current_ram_bytes, peak_ram_bytes = tracemalloc.get_traced_memory()
        current_ram_mb = current_ram_bytes / (1024 * 1024)
        peak_ram_mb = peak_ram_bytes / (1024 * 1024)
        
        prev_ram_mb = self.stages[-1]["current_ram_mb"] if self.stages else (current_ram_mb)
        delta_ram_mb = current_ram_mb - prev_ram_mb

        stage_record = {
            "step": len(self.stages) + 1,
            "stage_name": stage_name,
            "delta_t_ms": round(delta_t_ms, 3),
            "current_ram_mb": round(current_ram_mb, 3),
            "peak_ram_mb": round(peak_ram_mb, 3),
            "delta_ram_mb": round(delta_ram_mb, 3),
            "end_ns": now_ns,
            "details": details or {}
        }
        self.stages.append(stage_record)

    def stop_pipeline(self, query_text: str = ""):
        """Stops the global pipeline tracker and flushes telemetry logs."""
        end_total_ns = time.perf_counter_ns()
        total_time_ms = (end_total_ns - self.start_total_ns) / 1e6
        
        telemetry_entry = {
            "timestamp": datetime.now().isoformat(),
            "query": query_text,
            "total_time_ms": round(total_time_ms, 3),
            "stages": self.stages
        }
        
        # Flush log entry to telemetry.jsonl silently
        try:
            with open(self.log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(telemetry_entry) + "\n")
        except Exception:
            pass
            
        return telemetry_entry

    def render_markdown_telemetry(self, telemetry_entry: dict) -> str:
        """Renders an expandable HTML <details> collapsible footer for MCP markdown responses."""
        lines = [
            "\n\n<details>",
            "<summary>⏱️ <b>Chronological Pipeline Telemetry (Click to expand)</b></summary>",
            "",
            f"**Total Query Duration:** `{telemetry_entry['total_time_ms']:.2f} ms` | **Telemetry Logged:** `diagnostics/telemetry.jsonl`",
            "",
            "| Step | Pipeline Stage | Duration (Δt) | Heap RAM | Δ RAM | Details / Context |",
            "| :---: | :--- | :---: | :---: | :---: | :--- |"
        ]
        
        for s in telemetry_entry["stages"]:
            details_str = ", ".join([f"{k}: {v}" for k, v in s["details"].items()]) if s["details"] else "-"
            lines.append(
                f"| {s['step']} | **{s['stage_name']}** | `{s['delta_t_ms']:.3f} ms` | `{s['current_ram_mb']:.2f} MB` | `{s['delta_ram_mb']:+.2f} MB` | {details_str} |"
            )
            
        lines.append("</details>")
        return "\n".join(lines)
