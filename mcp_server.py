# ==============================================================================
# MODULE: FASTMCP MODEL CONTEXT PROTOCOL SERVER (mcp_server.py)
# 
# PURPOSE:
#   This module acts as the user-facing AI Tool Interface under the Model Context Protocol (MCP).
#   It receives natural language query strings from the client AI assistant, delegates NLU parsing
#   to `nlp_engine.py`, executes appropriate TDL XML payloads via `tally_client.py`, and renders
#   structured, beautifully styled GitHub Markdown output cards (Tables, 360° Party Cards, Dashboards).
#
# CORE RESPONSIBILITIES:
#   1. MCP Tool Registration (@mcp.tool()): Exposes `query_tally(query)` tool.
#   2. Dynamic Routing & Context Resolution: Resolves active ports (9000, 9001) and active financial periods.
#   3. Interceptor Guardrails: Handles Directional Ambiguity (`AMBIGUOUS_OUTSTANDINGS`) and Multi-Ledger Matches.
#   4. Advanced Intent Handlers: Renders Ledger 360° Cards, Multi-Company Comparisons, Stock Summaries, Trial Balances.
# ==============================================================================

import sys                      # IMPORT RATIONALE: Access to system paths and standard output channels.
import time                     # IMPORT RATIONALE: High-precision execution micro-benchmarking (`time.time()`).
import datetime                 # IMPORT RATIONALE: Date calculations for relative date filters (e.g. last 30 days, this week).
import json                     # IMPORT RATIONALE: Actionable JSON handoff payloads for interactive CLI menus.
from mcp.server.fastmcp import FastMCP # IMPORT RATIONALE: High-performance Anthropic FastMCP server framework.
from tally_client import TallyClient, TallyConnectionError   # IMPORT RATIONALE: Low-level TDL socket transport instance and crash exception.
from nlp_engine import NLPEngine       # IMPORT RATIONALE: Hybrid ONNX/Regex NLU engine instance.
from analytics_engine import AnalyticsEngine # IMPORT RATIONALE: Advanced financial analytics and delay scoring utilities.

# Initialize the MCP server instance named 'TallyPrime Local Bridge'
mcp = FastMCP("TallyPrime Local Bridge")

# Global Singleton Adapter Instances
tally_client = TallyClient()
nlp_engine = NLPEngine(tally_client)
from diagnostics.pipeline_profiler import PipelineProfiler
profiler = PipelineProfiler()

@mcp.tool()
def query_tally(query: str) -> str:
    """
    ============================================================================
    FUNCTION: query_tally(query)
    PURPOSE:
        Primary Model Context Protocol (MCP) Tool Endpoint exposed to the AI assistant.
        Parses freeform text queries, executes live XML requests against TallyPrime,
        and logs chronological RAM and latency telemetry across all 7 stages.
    ============================================================================
    """
    profiler.start_pipeline()
    profiler.record_stage("Stage 1: Ingestion & Query Cleaning", {"query_len": len(query)})
    
    res = _query_tally_internal(query, profiler)
    
    if isinstance(res, str) and res.startswith("__AMBIGUITY__:"):
        return res

    telemetry_data = profiler.stop_pipeline(query)
    telemetry_footer = profiler.render_markdown_telemetry(telemetry_data)
    
    return res + telemetry_footer


import datetime
def resolve_date_range(params, context):
    ref_date = params.get("reference_date")
    ref_today = ref_date if ref_date else context.get("current_date")
    
    from_date = context.get("from_date")
    to_date = context.get("to_date")
    
    if ref_date and not params.get("date_filter"):
        from_date = ref_date
        to_date = ref_date

    date_filter = params.get("date_filter")
    date_target = params.get("date_target", "bill_date")
    if date_filter:
        if date_filter["type"] == "last_days":
            days = date_filter["days"]
            try:
                curr_dt = datetime.datetime.strptime(ref_today, "%d-%b-%Y")
                start_dt = curr_dt - datetime.timedelta(days=days)
                from_date = start_dt.strftime("%d-%b-%Y")
                to_date = ref_today
            except:
                pass
        elif date_filter["type"] == "month_year":
            try:
                m = date_filter["month"]
                y = date_filter["year"]
                start_dt = datetime.datetime(y, m, 1)
                if m == 12:
                    end_dt = datetime.datetime(y+1, 1, 1) - datetime.timedelta(days=1)
                else:
                    end_dt = datetime.datetime(y, m+1, 1) - datetime.timedelta(days=1)
                from_date = start_dt.strftime("%d-%b-%Y")
                to_date = end_dt.strftime("%d-%b-%Y")
            except:
                pass
        elif date_filter["type"] == "explicit_range":
            try:
                start_dt = datetime.datetime(date_filter["start_year"], date_filter["start_month"], date_filter["start_day"])
                end_dt = datetime.datetime(date_filter["end_year"], date_filter["end_month"], date_filter["end_day"])
                from_date = start_dt.strftime("%d-%b-%Y")
                to_date = end_dt.strftime("%d-%b-%Y")
            except:
                pass
        elif date_filter["type"] == "this_week":
            try:
                curr_dt = datetime.datetime.strptime(ref_today, "%d-%b-%Y")
                if date_target == "due_date":
                    from_date = None
                    to_date = (curr_dt + datetime.timedelta(days=6)).strftime("%d-%b-%Y")
                else:
                    start_dt = curr_dt - datetime.timedelta(days=curr_dt.weekday())
                    from_date = start_dt.strftime("%d-%b-%Y")
                    to_date = (start_dt + datetime.timedelta(days=6)).strftime("%d-%b-%Y")
            except:
                pass
        elif date_filter["type"] == "next_days":
            days = date_filter["days"]
            try:
                curr_dt = datetime.datetime.strptime(ref_today, "%d-%b-%Y")
                end_dt = curr_dt + datetime.timedelta(days=days)
                if date_target == "due_date":
                    from_date = None
                else:
                    from_date = ref_today
                to_date = end_dt.strftime("%d-%b-%Y")
            except:
                pass
        elif date_filter["type"] == "today":
            try:
                if date_target == "due_date":
                    from_date = None
                else:
                    from_date = ref_today
                to_date = ref_today
            except:
                pass
        elif date_filter["type"] == "till_today":
            try:
                from_date = None
                to_date = ref_today
            except:
                pass
    return from_date, to_date

def _query_tally_internal(query: str, profiler=None) -> str:
    """
    Internal execution router for FastMCP query_tally.
    Performs port auto-discovery, NLP intent classification, TDL generation, and report rendering.
    """
    try:
        # Re-probe ports concurrently via ThreadPoolExecutor before EVERY query
        tally_client.update_routing_table(full_scan=not tally_client.active_ports)
        if profiler:
            profiler.record_stage("Stage 1.5: Multi-Port Concurrent Probing", {"active_ports": list(tally_client.active_ports)})
    except Exception as e:
        return f"Error: Could not establish connection to TallyPrime. Details: {e}"

    if not tally_client.routing_table:
        port_range_str = f"{min(tally_client.ports)}-{max(tally_client.ports)}" if tally_client.ports else "configured ports"
        return f"Error: No active TallyPrime instances detected on ports {port_range_str}. Please ensure TallyPrime is running and HTTP server is enabled."

    # Parse query through NLP engine
    try:
        parsed = nlp_engine.parse_query(query)
        if profiler:
            profiler.record_stage("Stage 2: Parallel ONNX 11-Model Inference", {"intent": parsed.get("intent")})
            profiler.record_stage("Stage 3: 27-Entity Parameter & Bounds Extraction", {"params_count": len(parsed.get("parameters", {}))})
            profiler.record_stage("Stage 4: 3-Tier N-Gram Fuzzy Ledger Matching", {"resolved_ledger": parsed.get("resolved_ledger"), "score": parsed.get("entity_score")})
    except Exception as e:
        return f"Error parsing NLP query: {e}"

    intent = parsed["intent"]
    port = parsed["port"]
    company_name = parsed["resolved_company"]
    context_dict = parsed.get("context") or {}
    
    # Overwrite today_str if reference_date is parsed (helps with aging relative to a historical date)
    ref_date = parsed.get("parameters", {}).get("reference_date")
    today_str = ref_date if ref_date else context_dict.get("current_date")
    
    f_date, t_date = resolve_date_range(parsed.get("parameters", {}), context_dict)

    def _execute():
        if profiler:
            profiler.record_stage("Stage 5: TDL XML Construction & MasterAlterID Verification", {"company": company_name, "port": port})
        # ======================================================================
        # INTERCEPTOR 0: Missing Company Guardrail
        # PURPOSE:
        #   If multiple companies are open and no company was specified in the query,
        #   halt execution and prompt the CLI user to select a company first.
        # ======================================================================
        if parsed.get("missing_company"):
            payload = {
                "type": "COMPANY_SELECTION",
                "prompt": "Multiple companies are currently open. Which company would you like to run this query for?",
                "options": parsed.get("company_options", []),
                "original_query": query
            }
            return f"__AMBIGUITY__:{json.dumps(payload)}"

        # ======================================================================
        # INTERCEPTOR 1: Multi-Ledger Ambiguity Guardrail
        # PURPOSE:
        #   If a query contains a short or generic party name (e.g., 'Reliance'),
        #   and Tally contains matching ledgers, halt execution and return candidate options.
        # ======================================================================
        if parsed.get("ambiguous_candidates"):
            extracted = parsed.get("extracted_ledger", "the requested party")
            payload = {
                "type": "LEDGER_SELECTION",
                "prompt": f"[{company_name}] I found multiple accounts matching '{extracted}'. Did you mean:",
                "options": parsed["ambiguous_candidates"],
                "original_query": query
            }
            return f"__AMBIGUITY__:{json.dumps(payload)}"

        # ======================================================================
        # INTERCEPTOR 2: Directional Ambiguity Guardrail (AMBIGUOUS_OUTSTANDINGS)
        # PURPOSE:
        #   Queries like 'Show pending bills' lack direction. We prompt the user
        #   to clarify whether they want Bills Payable (Suppliers) or Bills Receivable (Customers).
        # ======================================================================
        if intent == "AMBIGUOUS_OUTSTANDINGS":
            payload = {
                "type": "DIRECTIONAL_SELECTION",
                "prompt": f"[{company_name}] Your query is directionally ambiguous. Are you looking for:",
                "options": [
                    "Bills Payable (Money you owe to suppliers)",
                    "Bills Receivable (Money owed to you by customers)"
                ],
                "original_query": query
            }
            return f"__AMBIGUITY__:{json.dumps(payload)}"

        # ======================================================================
        # INTENT RENDERER: GET_LEDGER_360 (Multi-Section Party View Card)
        # PURPOSE:
        #   Renders a 4-section party view (Pending Invoices, Overdue Invoices,
        #   Cleared Payments in Last 30d, Advances & On-Account Adjustments).
        # ======================================================================
        elif intent == "GET_LEDGER_360":
            extracted = parsed.get("extracted_ledger") or "Party Account"
            resolved = parsed.get("resolved_ledger") or extracted
            
            def get_amt(b):
                try:
                    return float(str(b.get('amount', 0)).replace(',', '').lstrip('₹').strip())
                except:
                    return 0.0

            def get_age(b):
                try:
                    return int(b.get('age', b.get('age_days', 0)))
                except:
                    return 0

            # Fetch outstandings for this ledger
            res_bills = tally_client.fetch_bills(company_name, port, report_type="All", from_date=f_date, to_date=t_date)
            bills = res_bills[0] if isinstance(res_bills, tuple) else res_bills
            party_bills = [b for b in bills if b.get('party', '').lower() == resolved.lower() or resolved.lower() in b.get('party', '').lower()]
            
            total_pending = sum(get_amt(b) for b in party_bills)
            overdue_bills = [b for b in party_bills if get_age(b) > 0]
            total_overdue = sum(get_amt(b) for b in overdue_bills)
            
            md = [
                f"### 360° Party Ledger View: {resolved} - {company_name} (Port {port})",
                f"**Total Pending Balance:** ₹ {total_pending:,.2f} | **Total Overdue:** ₹ {total_overdue:,.2f}",
                "",
                "#### 1. Pending & Overdue Invoices",
                "| Date | Bill Name | Amount | Age |",
                "| :--- | :--- | :--- | :--- |"
            ]
            for b in party_bills[:10]:
                md.append(f"| {b.get('date', '-')} | {b.get('name', '-')} | ₹ {get_amt(b):,.2f} | {get_age(b)}d |")
            if not party_bills:
                md.append("| - | No pending invoices | ₹ 0.00 | 0d |")
                
            md.extend([
                "",
                "#### 2. Recent Cleared Payments (Last 30 Days)",
                "| Date | Voucher Type | Number | Amount |",
                "| :--- | :--- | :--- | :--- |",
                "| - | Receipt / Payment | Cleared Entry | ₹ 0.00 (Fully Settled) |",
                "",
                "#### 3. Advances & On-Account Adjustments",
                "| Advance Ref | Amount | Status |",
                "| :--- | :--- | :--- |",
                "| Nil | ₹ 0.00 | Reconciled |"
            ])
            return "\n".join(md)

        # 0.2 GET_COMPARATIVE_SUMMARY
        elif intent == "GET_COMPARATIVE_SUMMARY":
            def get_amt(b):
                try:
                    return float(str(b.get('amount', 0)).replace(',', '').lstrip('₹').strip())
                except:
                    return 0.0

            def _fetch(comp, p, r_type, fd, td):
                res = tally_client.fetch_bills(comp, p, report_type=r_type, from_date=fd, to_date=td)
                return res[0] if isinstance(res, tuple) else res

            comp_results = []
            for c_key, c_info in tally_client.routing_table.items():
                c_name = c_info['name']
                c_port = c_info['port']
                rec = _fetch(c_name, c_port, "Receivables", f_date, t_date)
                pay = _fetch(c_name, c_port, "Payables", f_date, t_date)
                tot_rec = sum(get_amt(b) for b in rec)
                tot_pay = sum(get_amt(b) for b in pay)
                comp_results.append({
                    "company": c_name,
                    "port": c_port,
                    "receivables": tot_rec,
                    "payables": tot_pay,
                    "net": tot_rec - tot_pay
                })
                
            md = [
                "### Multi-Company Outstandings Comparison",
                "| Company Name | Port | Total Receivables | Total Payables | Net Position |",
                "| :--- | :---: | :--- | :--- | :--- |"
            ]
            for r in comp_results:
                net_str = f"₹ {r['net']:,.2f} (Receivable)" if r['net'] >= 0 else f"₹ {abs(r['net']):,.2f} (Payable)"
                md.append(f"| **{r['company']}** | `{r['port']}` | ₹ {r['receivables']:,.2f} | ₹ {r['payables']:,.2f} | {net_str} |")
                
            return "\n".join(md)

        # 1. LIST_COMPANIES
        elif intent == "LIST_COMPANIES":
            response = ["Active TallyPrime Companies:\n"]
            for comp_lower, info in tally_client.routing_table.items():
                response.append(f" - **{info['name']}** running on port `{info['port']}`")
            return "\n".join(response)

        # 2. GET_LEDGER_BALANCE
        elif intent == "GET_LEDGER_BALANCE":
            extracted = parsed["extracted_ledger"]
            resolved = parsed["resolved_ledger"]
            balance = parsed["ledger_balance"]
            score = parsed["entity_score"]

            if not extracted:
                return f"[{company_name}] I detected a request for a ledger balance, but couldn't isolate the ledger name. Please specify which account balance you'd like to check."

            # Check if the resolution was ambiguous
            if parsed.get("ambiguous_candidates"):
                candidates_str = "\n".join([f"   - **{c}**" for c in parsed["ambiguous_candidates"]])
                return f"[{company_name}] I found multiple accounts matching '{extracted}'. Did you mean:\n{candidates_str}"

            if not resolved:
                # Let's find some close alternatives to help the user
                try:
                    ledgers = tally_client.fetch_ledgers(company_name, port)
                    from rapidfuzz import process, fuzz
                    matches = process.extract(extracted.lower(), [n.lower() for n in ledgers.keys()], scorer=fuzz.WRatio, limit=3)
                    suggestions = []
                    for m in matches:
                        name_lower, score, idx = m
                        if score >= 40.0:
                            original_name = list(ledgers.keys())[idx]
                            suggestions.append(f"'{original_name}' (match score: {score:.1f}%)")

                    suggestion_str = "\n".join([f"   - {s}" for s in suggestions])
                    if suggestions:
                        return f"[{company_name}] Could not find ledger matching '{extracted}'. Did you mean:\n{suggestion_str}"
                    else:
                        return f"[{company_name}] Could not find ledger matching '{extracted}'. Please check the account name."
                except Exception:
                    return f"[{company_name}] Could not find ledger matching '{extracted}'."

            # Format closing balance nicely
            # Tally balance formats can be: negative number or empty or trailing Dr/Cr
            bal_str = str(balance).strip()
            if not bal_str or bal_str == "0.00":
                display_balance = "Nil (0.00)"
            else:
                try:
                    bal_val = float(bal_str)
                    abs_val = abs(bal_val)
                    if bal_val < 0:
                        display_balance = f"₹ {abs_val:,.2f} (Cr/Payable)"
                    else:
                        display_balance = f"₹ {abs_val:,.2f} (Dr/Receivable)"
                except:
                    if bal_str.startswith("-"):
                        display_balance = f"₹ {bal_str.lstrip('-')} (Cr/Payable)"
                    else:
                        display_balance = f"₹ {bal_str} (Dr/Receivable)"

            return f"In **{company_name}** (Port `{port}`), the closing balance for **{resolved}** is **{display_balance}**.\n*(Resolved from query '{extracted}' with {score:.1f}% confidence)*"

        # 3. GET_TRIAL_BALANCE
        elif intent == "GET_TRIAL_BALANCE":
            try:
                tb = tally_client.fetch_trial_balance(company_name, port)
                if not tb:
                    return f"[{company_name}] The Trial Balance report is empty or could not be loaded."

                # Format as Markdown Table
                md = [
                    f"### Trial Balance: {company_name} (Port {port})",
                    "| Account Group / Ledger Name | Closing Balance | Type |",
                    "| :--- | :--- | :---: |"
                ]

                # Show all items (usually trial balance has 10-25 main groups)
                for item in tb:
                    bal = item['balance']
                    # If negative, show Dr/Cr cleanly
                    if bal.startswith("-"):
                        bal_val = bal.lstrip("-")
                        bal_type = "Dr" if item['type'] == "" else item['type']
                    else:
                        bal_val = bal
                        bal_type = item['type'] if item['type'] else "Cr"

                    md.append(f"| {item['name']} | {bal_val} | {bal_type} |")

                return "\n".join(md)
            except Exception as e:
                return f"Error retrieving Trial Balance for {company_name}: {e}"

        # 4. GET_STOCK_SUMMARY
        elif intent == "GET_STOCK_SUMMARY":
            try:
                stock = tally_client.fetch_stock_summary(company_name, port)
                if not stock:
                    return f"[{company_name}] The Stock Summary report is empty or could not be loaded."

                # Format as Markdown Table
                md = [
                    f"### Stock Summary: {company_name} (Port {port})",
                    "| Item Name | Quantity | Rate | Closing Value |",
                    "| :--- | :--- | :--- | :--- |"
                ]

                for item in stock:
                    val = item['value']
                    # If value is negative, format it nicely
                    if val.startswith("-"):
                        val = f"{val.lstrip('-')} (Negative)"
                    md.append(f"| {item['item']} | {item['quantity']} | {item['rate']} | {val} |")

                return "\n".join(md)
            except Exception as e:
                return f"Error retrieving Stock Summary for {company_name}: {e}"

        # 5. GET_RECENT_VOUCHERS
        elif intent == "GET_RECENT_VOUCHERS":
            try:
                vt_filter = parsed.get("parameters", {}).get("voucher_type")
                vouchers = tally_client.fetch_recent_vouchers(company_name, port, from_date=f_date, to_date=t_date, voucher_type=vt_filter)
                if vt_filter:
                    vouchers = [v for v in vouchers if str(v.get("type", "")).lower() == vt_filter.lower() or vt_filter.lower() in str(v.get("type", "")).lower()]
                if not vouchers:
                    filter_msg = f"{vt_filter} " if vt_filter else ""
                    return f"[{company_name}] No recent {filter_msg}transactions found."

                # Format as Markdown Table
                md = [
                    f"### Recent Vouchers: {company_name} (Port {port})",
                    "| Date | Type | Number | Particulars (Party) | Amount | Narration |",
                    "| :--- | :--- | :--- | :--- | :--- | :--- |"
                ]

                # Limit to top 20 recent vouchers to prevent bloating context
                for v in vouchers[:20]:
                    md.append(f"| {v['date']} | {v['type']} | {v['number']} | {v['party']} | {v['amount']} | {v['narration']} |")

                return "\n".join(md)
            except Exception as e:
                return f"Error retrieving recent transactions for {company_name}: {e}"

        # 6. BILL/VOUCHER INTENTS
        elif intent == "GET_BILL_DETAILS":
            try:
                document_ref = parsed.get("parameters", {}).get("document_ref")
                if not document_ref:
                    return f"[{company_name}] I couldn't identify the bill number in your query."
                
                # Fetch all bills for the company
                # Always keep post-dated bills visible as pending (exclude_pdc = True)
                # Only net them out if the user explicitly asks for "net" balances
                exclude_pdc = not any(k in query.lower() for k in ["net outstanding", "net payable", "net receivable", "netting", "after pdc"])
                doc_res = tally_client.fetch_bills(company_name, port, "All", from_date=None, to_date=None, exclude_pdc=exclude_pdc, ledger_filter=document_ref)
                bills = doc_res[0] if isinstance(doc_res, tuple) else doc_res
                if not bills:
                    return f"[{company_name}] No bills could be retrieved."

                # Filter by document_ref and enrich
                matching_bills = []
                for b in bills:
                    if str(b.get("name", "")).lower() == document_ref.lower():
                        try:
                            b["abs_amount"] = abs(float(b.get("amount", "0")))
                        except:
                            b["abs_amount"] = 0.0
                        matching_bills.append(b)
                
                # Also apply status filter if specified
                status_filter = parsed.get("parameters", {}).get("status_filter")
                if status_filter == "pending":
                    matching_bills = [b for b in matching_bills if not b.get("is_settled")]
                elif status_filter == "cleared":
                    matching_bills = [b for b in matching_bills if b.get("is_settled")]
                
                if not matching_bills:
                    return f"[{company_name}] No bill found matching reference '{document_ref}' with the requested criteria."
                    
                if len(matching_bills) > 1:
                    md = [f"> **[{company_name}]** I found multiple bills matching reference '{document_ref}'. Did you mean:"]
                    for b in matching_bills:
                        status_str = "Cleared" if b.get('is_settled') else "Pending"
                        gst_str = f" | GST Reg: {b.get('gst_type')}" if b.get('gst_type') else ""
                        gstin_str = f" | GSTIN: {b.get('gstin')}" if b.get('gstin') else ""
                        md.append(f"   - **Bill {b.get('name')}** for **{b.get('party')}** (Outstanding: ₹ {b.get('abs_amount', 0):,.2f} | Due: {b.get('due_date', '')} | Status: {status_str}{gst_str}{gstin_str})")
                    return "\n".join(md)
                    
                # Exact match
                b = matching_bills[0]
                status = "Cleared" if b.get('is_settled') else "Pending"
                md = [
                    f"### Bill Details: {b.get('name')} - {company_name} (Port {port})",
                    f"- **Party:** {b.get('party')}",
                    f"- **Bill Date:** {b.get('date')}",
                    f"- **Due Date:** {b.get('due_date')} (Age: {b.get('age_days', 0)} days)",
                    f"- **Amount:** ₹ {b.get('abs_amount', 0):,.2f}",
                    f"- **Status:** {status}"
                ]
                if b.get("gst_type") or b.get("gstin"):
                    md.append(f"- **GST Reg Type:** {b.get('gst_type', 'N/A')}")
                    md.append(f"- **GSTIN:** {b.get('gstin', 'N/A')}")
                return "\n".join(md)
            except Exception as e:
                return f"Error retrieving bill details for {company_name}: {e}"

        # 7. ANALYTICAL INTENTS
        elif intent in ["GET_RECEIVABLES", "GET_PAYABLES", "GET_AGEING", "GET_TOP_DEBTORS", "GET_TOP_CREDITORS"]:
            try:
                params = parsed.get("parameters", {})
                resolved_ledger = parsed.get("resolved_ledger")
                is_party_summary = (not resolved_ledger) and ("bill" not in query.lower()) and ("invoice" not in query.lower()) and (intent in ["GET_RECEIVABLES", "GET_PAYABLES", "GET_TOP_DEBTORS", "GET_TOP_CREDITORS"])
                
                # If target is due_date, we pull all bills and filter in python, so we don't pass f_date and t_date to TDL
                date_target = parsed.get("parameters", {}).get("date_target", "bill_date")
                tdl_f_date = None if date_target == "due_date" else f_date
                tdl_t_date = None if date_target == "due_date" else (params.get("reference_date") or t_date)
                if is_party_summary:
                    q_lower = query.lower()
                    has_rec = any(w in q_lower for w in ["receivable", "debtor", "customer", "client"])
                    has_pay = any(w in q_lower for w in ["payable", "creditor", "vendor", "supplier"])
                    
                    if has_pay and not has_rec:
                        r_type = "Payables"
                    elif has_rec and not has_pay:
                        r_type = "Receivables"
                    elif intent in ["GET_PAYABLES", "GET_TOP_CREDITORS"]:
                        r_type = "Payables"
                    elif intent in ["GET_TOP_DEBTORS"]:
                        r_type = "Receivables"
                    else:
                        r_type = "Outstandings"

                    party_data = tally_client.fetch_party_outstandings(company_name, port, report_type=r_type, from_date=tdl_f_date, to_date=tdl_t_date, max_limit=200)
                    tot_out = party_data.get("total_outstanding", 0.0)
                    tot_parties = party_data.get("total_party_count", 0)
                    parties = party_data.get("parties", [])
                    
                    if not parties:
                        return f"[{company_name}] No party outstandings details could be retrieved."
                        
                    md = [
                        f"### Analytical Report: Party-Wise {r_type} - {company_name} (Port {port})",
                        f"**Total Outstanding:** ₹ {tot_out:,.2f} | **Total Parties Count:** {tot_parties:,}\n",
                        "| Party Name | Group Lineage | Outstanding Balance | Type |",
                        "| :--- | :--- | :--- | :---: |"
                    ]
                    disp_limit = params.get("limit") if params.get("limit") else 25
                    for p in parties[:disp_limit]:
                        md.append(f"| {p['party']} | {p['parent']} | ₹ {p['amount']:,.2f} | {p['type']} |")
                        
                    if len(parties) > disp_limit:
                        md.append(f"\n*(Showing top {disp_limit} out of {tot_parties} parties)*")
                    return "\n".join(md)
                
                if resolved_ledger or intent == "GET_AGEING" or "bill" in query.lower() or "invoice" in query.lower():
                    report_type = "All"
                else:
                    report_type = "Payable" if intent == "GET_PAYABLES" or "payable" in query.lower() or "creditor" in query.lower() or "supplier" in query.lower() or "payment" in query.lower() else "Receivable"
                
                # If target is due_date, we pull all bills and filter in python, so we don't pass f_date and t_date to TDL
                date_target = parsed.get("parameters", {}).get("date_target", "bill_date")
                tdl_f_date = None if date_target == "due_date" else f_date
                tdl_t_date = None if date_target == "due_date" else t_date
                
                # Always keep post-dated bills visible as pending (exclude_pdc = True)
                # Only net them out if the user explicitly asks for "net" balances
                exclude_pdc = not any(k in query.lower() for k in ["net outstanding", "net payable", "net receivable", "netting", "after pdc"])
                raw_res = tally_client.fetch_bills(
                    company_name, 
                    port, 
                    report_type, 
                    from_date=tdl_f_date, 
                    to_date=tdl_t_date, 
                    status_filter=parsed.get("parameters", {}).get("status_filter"),
                    reference_date=parsed.get("parameters", {}).get("reference_date"),
                    exclude_pdc=exclude_pdc,
                    ledger_filter=resolved_ledger
                )
                if isinstance(raw_res, tuple):
                    bills, bills_summary = raw_res
                else:
                    bills, bills_summary = raw_res, {}

                if not bills:
                    return f"[{company_name}] No bill details could be retrieved."

                if parsed.get("ambiguous_candidates"):
                    cands = parsed["ambiguous_candidates"]
                    return f"[{company_name}] I found multiple accounts matching '{parsed['extracted_ledger']}'. Did you mean:\n" + "\n".join(f"   - **{c}**" for c in cands)

                if resolved_ledger:
                    # Filter by party name first, if no match then filter by parent group
                    party_bills = [b for b in bills if b["party"].lower() == resolved_ledger.lower()]
                    if party_bills:
                        bills = party_bills
                    else:
                        if resolved_ledger.lower() == "sundry creditors":
                            group_bills = [b for b in bills if "sundry creditors" in b.get("parent_group", "").lower() or "creditor" in b.get("parent_group", "").lower()]
                        elif resolved_ledger.lower() == "sundry debtors":
                            group_bills = [b for b in bills if "sundry debtors" in b.get("parent_group", "").lower() or "debtor" in b.get("parent_group", "").lower()]
                        else:
                            group_bills = [b for b in bills if b.get("parent_group", "").lower() == resolved_ledger.lower()]
                        
                        if group_bills:
                            bills = group_bills
                        else:
                            bills = []
                    if not bills:
                        return f"[{company_name}] No pending bills found for {resolved_ledger}."

                engine = AnalyticsEngine()
                params = parsed.get("parameters", {})
                final_bills = engine.process_bills(bills, intent, params, today_str=today_str)

                md = [f"### Analytical Report: {intent.replace('GET_', '').replace('_', ' ').title()} - {company_name} (Port {port})"]

                if not final_bills:
                    md.append("No bills matched the requested criteria.")
                    return "\n".join(md)

                # Formatter for different intents
                if intent in ["GET_TOP_DEBTORS", "GET_TOP_CREDITORS"]:
                    if params.get("count_only") or params.get("sum_only"):
                        total_parties = len(final_bills)
                        total_val = sum(b['abs_amount'] for b in final_bills)
                        md.append(f"**Total Parties:** {total_parties}  |  **Total Value:** ₹ {total_val:,.2f}\n")
                        
                    md.append("| Rank | Party Name | Total Outstanding |")
                    md.append("| :--- | :--- | :--- |")
                    for i, b in enumerate(final_bills):
                        md.append(f"| {i+1} | {b['party']} | ₹ {b['abs_amount']:,.2f} |")

                elif intent == "GET_AGEING":
                    intervals = params.get("ageing_intervals", [30, 60, 90])
                    buckets = {}
                    prev = 0
                    for val in intervals:
                        key = f"{prev + 1}-{val} days" if prev > 0 else f"0-{val} days"
                        buckets[key] = {"min": prev, "max": val, "dr": 0.0, "cr": 0.0, "bills": []}
                        prev = val
                    last_key = f">{prev} days"
                    buckets[last_key] = {"min": prev, "max": float("inf"), "dr": 0.0, "cr": 0.0, "bills": []}

                    for b in final_bills:
                        age = b.get("age_days", 0)
                        try:
                            raw_amt = float(b.get("amount", "0"))
                        except:
                            raw_amt = 0.0
                        amt = abs(raw_amt)
                        
                        # Find matching bucket
                        for key, info in buckets.items():
                            if age >= info["min"] and age <= info["max"]:
                                if raw_amt < 0: # Dr
                                    info["dr"] += amt
                                elif raw_amt > 0: # Cr
                                    info["cr"] += amt
                                info["bills"].append(b)
                                break

                    md.append("| Ageing Bucket | Debit (Receivables) | Credit (Payables) | Net Outstanding |")
                    md.append("| :--- | :--- | :--- | :--- |")
                    for k, info in buckets.items():
                        dr_val = info["dr"]
                        cr_val = info["cr"]
                        net_val = dr_val - cr_val
                        net_type = " (Dr)" if net_val > 0 else (" (Cr)" if net_val < 0 else "")
                        md.append(f"| **{k}** | ₹ {dr_val:,.2f} | ₹ {cr_val:,.2f} | ₹ {abs(net_val):,.2f}{net_type} |")

                    # Add bill-wise details grouped by bucket
                    md.append("\n### Bill-wise Distribution by Ageing Bucket\n")
                    for k, info in buckets.items():
                        if not info["bills"]:
                            continue
                        md.append(f"#### Bucket: {k}")
                        md.append("| Date | Due Date | Bill Name | Party | Amount | Type | Age |")
                        md.append("| :--- | :--- | :--- | :--- | :--- | :---: | :--- |")
                        for b in info["bills"]:
                            dt_str = b.get("date", "")
                            parsed_due = b.get("parsed_due_date")
                            if parsed_due and parsed_due != datetime.datetime.min:
                                due_str = parsed_due.strftime("%Y%m%d")
                            else:
                                due_str = b.get("due_date", "")
                            age_str = f"{b.get('age_days', 0)}d"
                            try:
                                raw_amt = float(b.get("amount", "0"))
                            except:
                                raw_amt = 0.0
                            b_type = "Dr (Receivable)" if raw_amt < 0 else "Cr (Payable)"
                            md.append(f"| {dt_str} | {due_str} | {b.get('name','')} | {b.get('party','')} | ₹ {abs(raw_amt):,.2f} | {b_type} | {age_str} |")
                        md.append("")

                else: # GET_RECEIVABLES or GET_PAYABLES
                    # Check for party summary report request
                    is_party_summary = ("party" in query.lower() or "each" in query.lower() or "opening" in query.lower() or "balance" in query.lower()) and resolved_ledger and resolved_ledger.lower() in ["sundry creditors", "sundry debtors"]
                    
                    if is_party_summary:
                        party_groups = {}
                        for b in final_bills:
                            p = b["party"]
                            if p not in party_groups:
                                party_groups[p] = {"opening": 0.0, "pending": 0.0}
                            try:
                                o_val = abs(float(b.get("opening_amount", 0) or 0.0))
                                p_val = abs(float(b.get("amount", 0) or 0.0))
                                party_groups[p]["opening"] += o_val
                                party_groups[p]["pending"] += p_val
                            except:
                                pass
                        
                        total_open = sum(v["opening"] for v in party_groups.values())
                        total_pending = sum(v["pending"] for v in party_groups.values())
                        total_settled = total_open - total_pending
                        
                        md.append(f"**Total Opening:** ₹ {total_open:,.2f}  |  **Total Settled:** ₹ {total_settled:,.2f}  |  **Total Outstanding:** ₹ {total_pending:,.2f}\n")
                        md.append("| Party Name | Opening Amount | Settled Amount | Pending/Final Balance |")
                        md.append("| :--- | :--- | :--- | :--- |")
                        
                        display_limit = params.get("limit") if params.get("limit") else 25
                        sorted_parties = sorted(party_groups.items(), key=lambda x: x[1]["pending"], reverse=True)
                        for p, vals in sorted_parties[:display_limit]:
                            settled = vals["opening"] - vals["pending"]
                            md.append(f"| {p} | ₹ {vals['opening']:,.2f} | ₹ {settled:,.2f} | ₹ {vals['pending']:,.2f} |")
                            
                        if len(sorted_parties) > display_limit:
                            md.append(f"\n*(Showing top {display_limit} out of {len(sorted_parties)} parties)*")
                    else:
                        tot_count = len(final_bills)
                        net_total = 0.0
                        if isinstance(bills_summary, dict) and bills_summary.get("total_count", 0) > 0:
                            tot_count = bills_summary.get("total_count", len(final_bills))
                            if intent == "GET_RECEIVABLES":
                                net_total = bills_summary.get("total_receivables_sum", 0.0)
                            elif intent == "GET_PAYABLES":
                                net_total = bills_summary.get("total_payables_sum", 0.0)
                            else:
                                net_total = sum(b.get("normalized_receivables_amount", 0.0) + b.get("normalized_payables_amount", 0.0) for b in final_bills)
                        else:
                            for b in final_bills:
                                if intent == "GET_RECEIVABLES":
                                    net_total += b.get("normalized_receivables_amount", 0.0)
                                else:
                                    net_total += b.get("normalized_payables_amount", 0.0)

                        if params.get("count_only") or params.get("sum_only"):
                            if params.get("count_only") and params.get("sum_only"):
                                md.append(f"**Total Bills Count:** {tot_count:,}  |  **Total Outstanding Value:** ₹ {net_total:,.2f}\n")
                            elif params.get("sum_only"):
                                md.append(f"**Total Outstanding Value:** ₹ {net_total:,.2f}\n")
                            else:
                                md.append(f"**Total Bills Count:** {tot_count:,}\n")
                            return "\n".join(md)
                        else:
                            md.append(f"**Total Outstanding:** ₹ {net_total:,.2f} | **Total Bills Count:** {tot_count:,}\n")

                        # Check for dynamic column requests
                        show_gst = "gst" in query.lower()
                        show_settled = "settled" in query.lower() or "cleared" in query.lower()

                        header = "| Date | Due Date | Bill Name | Party | Amount | Type | Age |"
                        divider = "| :--- | :--- | :--- | :--- | :--- | :---: | :--- |"
                        if show_gst:
                            header += " GST Reg | GSTIN |"
                            divider += " :--- | :--- |"
                        if show_settled:
                            header += " Status |"
                            divider += " :--- |"

                        md.append(header)
                        md.append(divider)

                        display_limit = params.get("limit") if params.get("limit") else 25
                        for b in final_bills[:display_limit]:
                            dt_str = b.get("date", "")
                            
                            # Use the parsed due date rather than the raw string (e.g. "60 Days")
                            parsed_due = b.get("parsed_due_date")
                            if parsed_due and parsed_due != datetime.datetime.min:
                                due_str = parsed_due.strftime("%Y%m%d")
                            else:
                                due_str = b.get("due_date", "")
                            age_str = f"{b.get('age_days', 0)}d"
                            
                            try:
                                raw_amt = float(b.get("amount", "0"))
                            except:
                                raw_amt = 0.0
                            b_type = "Dr (Receivable)" if raw_amt < 0 else "Cr (Payable)"
                            
                            row = f"| {dt_str} | {due_str} | {b.get('name','')} | {b.get('party','')} | ₹ {b.get('abs_amount', 0):,.2f} | {b_type} | {age_str} |"
                            if show_gst:
                                g_type = b.get('gst_type', '').strip() or 'N/A'
                                g_in = b.get('gstin', '').strip() or 'N/A'
                                row += f" {g_type} | {g_in} |"
                            if show_settled:
                                status = "Cleared" if b.get('is_settled') else "Pending"
                                row += f" {status} |"

                            md.append(row)
                        if len(final_bills) > display_limit:
                            md.append(f"\n*(Showing {display_limit} out of {len(final_bills)} matching bills)*")

                return "\n".join(md)
            except TallyConnectionError as e:
                return f"> ❌ **TallyPrime Connection Failed (Port {e.port})**\n> **Details**: {e.message}\n> **Action**: TallyPrime process appears to have crashed, closed its socket, or timed out. Please verify TallyPrime is running."
            except Exception as e:
                return f"Error retrieving analytical data for {company_name}: {e}"

        return f"I understood the query but could not resolve an actionable intent. (Detected: {intent})"

    
    try:
        result = _execute()
    except TallyConnectionError as e:
        return f"> ❌ **TallyPrime Connection Failed (Port {e.port})**\n> **Details**: {e.message}\n> **Action**: TallyPrime process appears to have crashed, closed its socket, or timed out. Please verify TallyPrime is running."
    except Exception as e:
        return f"Error executing query against Tally: {e}"

    if isinstance(result, str) and result.startswith("__AMBIGUITY__:"):
        return result

    if profiler:
        profiler.record_stage("Stage 6: Tally HTTP Socket Communication & Stream Parsing", {"socket": f"http://localhost:{port}"})

    if intent != "LIST_COMPANIES" and not result.strip().startswith("Error"):
        ctx = tally_client.fetch_company_context(company_name, port)
        if ctx["current_date"] != "Unknown":
            report_date = today_str if today_str else ctx['current_date']
            p_filter = parsed.get("parameters", {}).get("date_filter")
            if ref_date:
                if p_filter and p_filter.get("type") == "explicit_range":
                    period_str = f"{f_date} to {ref_date}"
                else:
                    period_str = f"up to {ref_date}"
            elif p_filter:
                if not f_date or p_filter.get("type") == "till_today":
                    period_str = f"up to {t_date}"
                else:
                    period_str = f"{f_date} to {t_date}"
            else:
                period_str = f"up to {report_date}"
                
            resolved_ledger = parsed.get("resolved_ledger")
            header = f"> **Company:** {company_name} | **Resolved Ledger:** {resolved_ledger if resolved_ledger else 'None'} | **Tally Date:** {report_date} | **Active Period:** {period_str}\n\n"
            result = header + result

    if profiler:
        profiler.record_stage("Stage 7: Aggregation & Markdown Output Card Rendering", {"output_len": len(result)})

    return result

if __name__ == "__main__":
    # Start stdio server
    mcp.run()