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
import re                       # IMPORT RATIONALE: Regular expressions for token sanitation and entity validation.
from mcp.server.fastmcp import FastMCP # IMPORT RATIONALE: High-performance Anthropic FastMCP server framework.
from tally_client import TallyClient, TallyConnectionError   # IMPORT RATIONALE: Low-level TDL socket transport instance and crash exception.
from nlp_engine import NLPEngine       # IMPORT RATIONALE: Hybrid ONNX/Regex NLU engine instance.
from analytics_engine import AnalyticsEngine # IMPORT RATIONALE: Advanced financial analytics and delay scoring utilities.
import constants
import date_utils
from diagnostics.pipeline_profiler import PipelineProfiler

# Initialize the MCP server instance named 'TallyPrime Local Bridge'
mcp = FastMCP("TallyPrime Local Bridge")

# Global Singleton Adapter Instances
tally_client = TallyClient()
nlp_engine = NLPEngine(tally_client)
analytics_engine = AnalyticsEngine()
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


def resolve_date_range(params, context):
    return date_utils.resolve_date_range(params, context)


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
    today_str = ref_date if ref_date else (context_dict.get("current_date") or datetime.date.today().strftime("%d-%b-%Y"))
    
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

        def _is_valid_party_name(p_str):
            if not p_str or not isinstance(p_str, str):
                return False
            cleaned = p_str.strip(",.!? \t\n").lower()
            if len(cleaned) < 3:
                return False
            generic_words = {
                "in", "of", "for", "to", "from", "at", "by", "on", "the", "a", "an", "what", "how", "total", 
                "all", "overdue", "pending", "bills", "bill", "amount", "balance", "items", "item", "list", 
                "show", "get", "is", "are", "was", "were", "much", "many", "unpaid", "paid", "due", "recent",
                "entries", "vouchers", "transactions", "ledger", "account", "accounts", "details", "summary",
                "report", "last month", "this month", "last year", "this year", "customer", "customers",
                "debtor", "debtors", "creditor", "creditors", "supplier", "suppliers", "vendor", "vendors"
            }
            if cleaned in generic_words:
                return False
            tokens = [t for t in re.split(r'\W+', cleaned) if t]
            if not tokens or all(t in generic_words for t in tokens):
                return False
            return True

        # ======================================================================
        # INTERCEPTOR 1: Multi-Ledger Ambiguity Guardrail
        # PURPOSE:
        #   If a query contains a short or generic party name (e.g., 'Reliance'),
        #   and Tally contains matching ledgers, halt execution and return candidate options.
        # ======================================================================
        if parsed.get("ambiguous_candidates") and _is_valid_party_name(parsed.get("extracted_ledger")):
            extracted = parsed.get("extracted_ledger", "the requested party")
            payload = {
                "type": "LEDGER_SELECTION",
                "prompt": f"[{company_name}] I found multiple accounts matching '{extracted}'. Did you mean:",
                "options": parsed["ambiguous_candidates"],
                "extracted": extracted,
                "original_query": query
            }
            return f"__AMBIGUITY__:{json.dumps(payload)}"

        # When no explicit date is provided, default seamlessly to active Tally company date context
        intent = parsed.get("intent")

        # ======================================================================
        # INTERCEPTOR 2: Directional Ambiguity Guardrail (AMBIGUOUS_OUTSTANDINGS)
        # PURPOSE:
        #   Queries like 'Show pending bills' lack direction. If no specific party is
        #   specified, we return the Executive Outstandings & Financial Position Dashboard.
        # ======================================================================
        if intent == "AMBIGUOUS_OUTSTANDINGS":
            extracted_party = parsed.get("extracted_ledger") or parsed.get("parameters", {}).get("party_name")
            resolved_party = parsed.get("resolved_ledger")
            
            if resolved_party:
                parsed["intent"] = "GET_RECEIVABLES"
                intent = "GET_RECEIVABLES"
            elif extracted_party and _is_valid_party_name(extracted_party):
                payload = {
                    "type": "DIRECTIONAL_SELECTION",
                    "prompt": f"[{company_name}] Is '{extracted_party}' a Customer (Receivables) or a Supplier (Payables)?",
                    "options": [
                        f"Bills Receivable (Customer: {extracted_party})",
                        f"Bills Payable (Supplier: {extracted_party})"
                    ],
                    "original_query": query
                }
                return f"__AMBIGUITY__:{json.dumps(payload)}"
            else:
                # General company-wide outstandings / pending summary inquiry -> Executive Dashboard
                try:
                    rec_data = tally_client.fetch_party_outstandings(company_name, port, report_type="Receivables", from_date=f_date, to_date=t_date)
                    pay_data = tally_client.fetch_party_outstandings(company_name, port, report_type="Payables", from_date=f_date, to_date=t_date)

                    rec_parties = rec_data.get("parties", [])
                    pay_parties = pay_data.get("parties", [])

                    tot_rec = sum(abs(float(p.get("amount", 0.0))) for p in rec_parties)
                    tot_pay = sum(abs(float(p.get("amount", 0.0))) for p in pay_parties)
                    net_pos = tot_rec - tot_pay
                    net_str = f"₹ {abs(net_pos):,.2f} {'Dr (Net Receivable)' if net_pos >= 0 else 'Cr (Net Payable)'}"

                    rec_sorted = sorted(rec_parties, key=lambda x: abs(float(x.get("amount", 0.0))), reverse=True)
                    pay_sorted = sorted(pay_parties, key=lambda x: abs(float(x.get("amount", 0.0))), reverse=True)

                    md = [
                        f"## 📊 Executive Company Outstandings & Financial Position: {company_name} (Port {port})\n",
                        "> **Real-Time Financial Position Summary**\n",
                        "### 💼 Overall Outstandings Breakdown",
                        "| Classification | Actionable Accounts | Total Balance (₹) | Direction / Financial Significance |",
                        "| :--- | :---: | :---: | :--- |",
                        f"| **Bills Receivable (Sundry Debtors)** | {len(rec_parties)} | ₹ {tot_rec:,.2f} | Money owed to company by customers |",
                        f"| **Bills Payable (Sundry Creditors)** | {len(pay_parties)} | ₹ {tot_pay:,.2f} | Money company owes to suppliers |",
                        f"| **Net Working Capital Exposure** | — | **{net_str}** | Net outstandings balance |"
                    ]

                    if rec_sorted:
                        md.extend([
                            "\n### 🎯 Top Critical Customer Receivables (Highest Outstanding)",
                            "| Rank | Customer Account Name | Group Lineage | Outstanding (₹) | Collection Follow-Up |",
                            "| :---: | :--- | :--- | :---: | :--- |"
                        ])
                        for i, p in enumerate(rec_sorted[:5], 1):
                            p_amt = abs(float(p.get("amount", 0.0)))
                            p_name = p.get("party", "Unknown")
                            p_grp = p.get("parent", "Sundry Debtors")
                            recom = "🔴 Immediate Action" if p_amt >= 10000000.0 else ("🟠 High Priority" if p_amt >= 2500000.0 else "🟡 Regular Follow-Up")
                            md.append(f"| {i} | {p_name} | {p_grp} | ₹ {p_amt:,.2f} | {recom} |")

                    if pay_sorted:
                        md.extend([
                            "\n### 🏷️ Top Critical Vendor Payables (Highest Pending)",
                            "| Rank | Vendor Account Name | Group Lineage | Pending Amount (₹) |",
                            "| :---: | :--- | :--- | :---: |"
                        ])
                        for i, p in enumerate(pay_sorted[:5], 1):
                            p_amt = abs(float(p.get("amount", 0.0)))
                            p_name = p.get("party", "Unknown")
                            p_grp = p.get("parent", "Sundry Creditors")
                            md.append(f"| {i} | {p_name} | {p_grp} | ₹ {p_amt:,.2f} |")

                    return "\n".join(md)
                except Exception as e:
                    return f"Error retrieving company outstandings summary for {company_name}: {e}"

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

        # 2. GET_COMPANY_SUMMARY (Executive Financial Dashboard)
        elif intent in ["GET_COMPANY_SUMMARY", "GET_COMPARATIVE_SUMMARY"] or ("summary" in query.lower() and not parsed.get("resolved_ledger") and not parsed.get("parameters", {}).get("stock_group") and not parsed.get("parameters", {}).get("godown_name") and not parsed.get("parameters", {}).get("cost_center")):
            try:
                dash = tally_client.fetch_company_dashboard(company_name, port, from_date=f_date, to_date=t_date)
                period_str = f"Period: {f_date} to {t_date}" if f_date and t_date else (f"as of {t_date}" if t_date else "Active Financial Year")
                
                md = [
                    f"## 📊 Executive Financial Dashboard: {company_name} ({period_str}) (Port {port})\n",
                    "### 1. Working Capital & Liquidity Snapshot",
                    "| Financial Metric | Amount (₹) | Status / Details |",
                    "| :--- | :--- | :--- |",
                    f"| **Sundry Debtors (Receivables)** | ₹ {dash['receivables_total']:,.2f} | {dash['total_debtors_count']} Active Debtors |",
                    f"| **Sundry Creditors (Payables)** | ₹ {dash['payables_total']:,.2f} | {dash['total_creditors_count']} Active Creditors |",
                    f"| **Net Working Capital Position** | ₹ {dash['net_working_capital']:,.2f} | {'Net Receivable' if dash['net_working_capital'] >= 0 else 'Net Payable'} |",
                    f"| **Bank Accounts Balance** | ₹ {dash['bank_balance']:,.2f} | Available Bank Funds |",
                    f"| **Cash-in-Hand** | ₹ {dash['cash_balance']:,.2f} | Liquid Cash Reserves |",
                    f"| **Total Liquid Reserves** | ₹ {dash['total_liquidity']:,.2f} | Total Cash + Bank |",
                    f"| **Total Inventory Valuation** | ₹ {dash['stock_valuation']:,.2f} | {dash['active_stock_items_count']} Active Stock Items |\n"
                ]

                # Top 5 Debtors
                if dash.get("top_debtors"):
                    md.append("### 2. Top 5 Outstanding Debtors (Receivables)")
                    md.append("| Rank | Debtor / Customer Name | Outstanding Balance (₹) |")
                    md.append("| :---: | :--- | :--- |")
                    for i, d in enumerate(dash["top_debtors"]):
                        p_name = d.get('party') or d.get('name', '')
                        amt = abs(d.get('amount', 0) or d.get('closing_balance', 0))
                        md.append(f"| {i+1} | {p_name} | ₹ {amt:,.2f} |")
                    md.append("")

                # Top 5 Creditors
                if dash.get("top_creditors"):
                    md.append("### 3. Top 5 Outstanding Creditors (Payables)")
                    md.append("| Rank | Creditor / Vendor Name | Outstanding Balance (₹) |")
                    md.append("| :---: | :--- | :--- |")
                    for i, c in enumerate(dash["top_creditors"]):
                        p_name = c.get('party') or c.get('name', '')
                        amt = abs(c.get('amount', 0) or c.get('closing_balance', 0))
                        md.append(f"| {i+1} | {p_name} | ₹ {amt:,.2f} |")
                    md.append("")


                return "\n".join(md)
            except Exception as e:
                return f"Error generating Company Dashboard for {company_name}: {e}"

        # 3. GET_LEDGER_BALANCE (4-Card Single Ledger Dashboard)
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

            ref_date = parsed.get("parameters", {}).get("reference_date") or t_date
            if ref_date:
                dated_res = tally_client.fetch_ledger_dated_balance(company_name, port, resolved, reference_date=ref_date)
                if dated_res["is_nil"] or dated_res["abs_val"] == 0.0:
                    display_balance = "Nil (0.00)"
                else:
                    drcr_label = f"({dated_res['drcr']}/Receivable)" if dated_res['drcr'] == "Dr" else f"({dated_res['drcr']}/Payable)"
                    display_balance = f"₹ {dated_res['abs_val']:,.2f} {drcr_label}"
                date_info = f" as of **{dated_res['as_of_date']}**"
            else:
                bal_str = str(balance).strip()
                if not bal_str or bal_str == "0.00":
                    display_balance = "Nil (0.00)"
                else:
                    try:
                        bal_val = float(bal_str)
                        abs_val = abs(bal_val)
                        if bal_val < 0:
                            display_balance = f"₹ {abs_val:,.2f} (Dr/Receivable)"
                        else:
                            display_balance = f"₹ {abs_val:,.2f} (Cr/Payable)"
                    except:
                        if bal_str.startswith("-"):
                            display_balance = f"₹ {bal_str.lstrip('-')} (Dr/Receivable)"
                        else:
                            display_balance = f"₹ {bal_str} (Cr/Payable)"
                date_info = ""

            # Check if this is a rich 360 / dashboard query
            is_deep_query = any(w in query.lower() for w in ["overview", "360", "details", "dashboard", "history", "trend", "breakup", "profile", "drilldown"])

            if not is_deep_query:
                return f"In **{company_name}** (Port `{port}`), the closing balance for **{resolved}**{date_info} is **{display_balance}**.\n*(Resolved from query '{extracted}' with {score:.1f}% confidence)*"

            # Render Complete 4-Card Single Ledger Dashboard
            cards = [
                f"## 📇 Ledger 360° Dashboard: {resolved} - {company_name} (Port {port})\n",
                "### 🎴 Card 1: Balance & Settlement Status",
                f"- **Account Name:** `{resolved}`",
                f"- **Dated Closing Balance:** **{display_balance}**{date_info}",
                f"- **Resolution Confidence:** `{score:.1f}%` (from query token: *'{extracted}'*)\n"
            ]

            # Card 2: Pending Bills & Aging
            bills_res = tally_client.fetch_bills(company_name, port, "All", ledger_filter=resolved, from_date=f_date, to_date=t_date)
            bills = bills_res[0] if isinstance(bills_res, tuple) else bills_res
            cards.append("### 🎴 Card 2: Pending Outstanding Bills & Overdue Status")
            if bills:
                cards.append(f"**Total Pending Bills:** `{len(bills)}`\n")
                cards.append("| Bill Reference | Bill Date | Due Date | Outstanding Amount | Age |")
                cards.append("| :--- | :--- | :--- | :--- | :---: |")
                for b in bills[:10]:
                    try:
                        amt = abs(float(b.get("amount", 0)))
                    except:
                        amt = 0.0
                    cards.append(f"| {b.get('name', '')} | {b.get('date', '')} | {b.get('due_date', '')} | ₹ {amt:,.2f} | {b.get('age_days', 0)}d |")
                if len(bills) > 10:
                    cards.append(f"\n*(Showing top 10 out of {len(bills)} pending bills)*")
            else:
                cards.append("> ℹ️ *No pending overdue bills found for this account.*\n")

            # Card 3: Monthly Financial Trend (12 Months)
            monthly = tally_client.fetch_ledger_monthly_summary(company_name, port, resolved, from_date=f_date, to_date=t_date)
            cards.append("\n### 🎴 Card 3: 12-Month Financial Movement Trajectory")
            if monthly:
                cards.append("| Month | Debit Movement (₹) | Credit Movement (₹) | Closing Balance |")
                cards.append("| :--- | :--- | :--- | :--- |")
                for m in monthly:
                    cards.append(f"| {m.get('month', '')} | ₹ {m.get('debit', 0.0):,.2f} | ₹ {m.get('credit', 0.0):,.2f} | {m.get('closing_balance', '₹ 0.00')} |")
            else:
                cards.append("> ℹ️ *No monthly summary data recorded for active FY.*\n")

            # Card 4: Recent Vouchers
            vouchers = tally_client.fetch_recent_vouchers(company_name, port, from_date=f_date, to_date=t_date)
            party_vouchers = [v for v in vouchers if resolved.lower() in str(v.get("party", "")).lower()][:5]
            cards.append("\n### 🎴 Card 4: Recent Transaction Activity")
            if party_vouchers:
                cards.append("| Date | Type | Voucher No | Amount (₹) | Narration |")
                cards.append("| :--- | :--- | :--- | :--- | :--- |")
                for v in party_vouchers:
                    cards.append(f"| {v.get('date', '')} | {v.get('type', '')} | {v.get('number', '')} | {v.get('amount', '')} | {v.get('narration', '')} |")
            else:
                cards.append("> ℹ️ *No recent posted vouchers found in active FY period.*\n")

            return "\n".join(cards)


        # 3. GET_TRIAL_BALANCE
        elif intent == "GET_TRIAL_BALANCE":
            try:
                tb = tally_client.fetch_trial_balance(company_name, port, from_date=f_date, to_date=t_date)
                if not tb:
                    return f"[{company_name}] The Trial Balance report is empty or could not be loaded."

                # Format as Markdown Table
                period_str = f"Period: {f_date} to {t_date}" if f_date and t_date else (f"as of {t_date}" if t_date else "Current Fiscal Period")
                md = [
                    f"### Trial Balance: {company_name} ({period_str})",
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

        # 4. GET_STOCK_SUMMARY & INVENTORY ANALYTICS
        elif intent in ["GET_STOCK_SUMMARY", "GET_BATCH_DETAILS"] or ("stock" in query.lower() and intent == "GET_LEDGER_BALANCE" and not parsed.get("resolved_ledger")):
            try:
                params = parsed.get("parameters", {})
                stock_grp = params.get("stock_group")
                stock_cat = params.get("stock_category")
                godown = params.get("godown_name")
                item_name = params.get("item_name")
                as_of_date = params.get("reference_date") or t_date

                # Check if batch/expiry details are specifically requested
                if intent == "GET_BATCH_DETAILS" or any(w in query.lower() for w in ["batch", "batches", "expiry", "mfg date", "manufacturing date", "expiring"]):
                    batches = tally_client.fetch_batch_details(company_name, port, stock_item=item_name, godown_name=godown, as_of_date=as_of_date)
                    if not batches:
                        item_msg = f" for '{item_name}'" if item_name else ""
                        return f"[{company_name}] No batch tracking records{item_msg} found."

                    md = [
                        f"### Batch Tracking Details: {company_name} (Port {port})",
                        "| Item Name | Batch No | Godown / Location | Quantity | Rate | Closing Value | Mfg Date | Expiry Date |",
                        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |"
                    ]
                    for b in batches:
                        md.append(f"| {b.get('item', '')} | {b.get('batch', '')} | {b.get('godown', '')} | {b.get('quantity', '')} | {b.get('rate', '')} | {b.get('value', '')} | {b.get('mfg_date', 'N/A')} | {b.get('expiry_date', 'N/A')} |")
                    return "\n".join(md)

                # Standard Multi-Dimensional Stock Summary
                stock = tally_client.fetch_stock_summary(
                    company_name, port,
                    stock_group=stock_grp,
                    stock_category=stock_cat,
                    godown_name=godown,
                    item_name=item_name,
                    as_of_date=as_of_date
                )
                if not stock:
                    scope_parts = []
                    if stock_grp: scope_parts.append(f"Group '{stock_grp}'")
                    if stock_cat: scope_parts.append(f"Category '{stock_cat}'")
                    if godown: scope_parts.append(f"Godown '{godown}'")
                    if item_name: scope_parts.append(f"Item '{item_name}'")
                    scope_msg = f" for {', '.join(scope_parts)}" if scope_parts else ""
                    return f"[{company_name}] The Stock Summary report{scope_msg} is empty or could not be loaded."

                # Format as Markdown Table
                hdr_parts = []
                if godown: hdr_parts.append(f"Godown: {godown}")
                if stock_grp: hdr_parts.append(f"Group: {stock_grp}")
                if stock_cat: hdr_parts.append(f"Category: {stock_cat}")
                if item_name: hdr_parts.append(f"Item: {item_name}")
                if as_of_date: hdr_parts.append(f"As of: {as_of_date}")
                hdr_info = f" ({' | '.join(hdr_parts)})" if hdr_parts else ""

                md = [
                    f"### Stock Summary: {company_name}{hdr_info} (Port {port})",
                    "| Item Name | Category / Location | Quantity | Rate | Closing Value |",
                    "| :--- | :--- | :--- | :--- | :--- |"
                ]

                for item in stock:
                    val = item['value']
                    if val.startswith("-"):
                        val = f"{val.lstrip('-')} (Negative)"
                    cat_loc = item.get('category') or item.get('parent') or '-'
                    md.append(f"| {item['item']} | {cat_loc} | {item['quantity']} | {item['rate']} | {val} |")

                return "\n".join(md)
            except Exception as e:
                return f"Error retrieving Stock Summary for {company_name}: {e}"


        # 5. GET_COST_CENTRE_BREAKUP / SUMMARY
        elif intent in ["GET_COST_CENTRE_BREAKUP", "GET_COST_CENTRE_SUMMARY"] or (parsed.get("parameters", {}).get("cost_center") and intent not in ["GET_RECEIVABLES", "GET_PAYABLES", "GET_BILL_DETAILS"]):
            try:
                params = parsed.get("parameters", {})
                cc_name = params.get("cost_center")

                breakup = tally_client.fetch_cost_centre_breakup(company_name, port, cost_centre=cc_name, from_date=f_date, to_date=t_date)
                if not breakup:
                    cc_msg = f" for Cost Centre '{cc_name}'" if cc_name else ""
                    return f"[{company_name}] No Cost Centre records{cc_msg} found."

                if cc_name:
                    md = [
                        f"### Cost Centre Breakup: {cc_name} - {company_name} (Port {port})",
                        "| Particulars (Ledger) | Debit (₹) | Credit (₹) | Net Balance (₹) |",
                        "| :--- | :--- | :--- | :--- |"
                    ]
                    for row in breakup:
                        md.append(f"| {row.get('particulars', '')} | {row.get('debit', '0.00')} | {row.get('credit', '0.00')} | {row.get('net_balance', '0.00')} |")
                else:
                    md = [
                        f"### Cost Centres Summary: {company_name} (Port {port})",
                        "| Cost Centre | Category | Parent | Closing Balance (₹) |",
                        "| :--- | :--- | :--- | :--- |"
                    ]
                    for row in breakup:
                        md.append(f"| {row.get('name', '')} | {row.get('category', '')} | {row.get('parent', '')} | {row.get('balance', '0.00')} |")

                return "\n".join(md)
            except Exception as e:
                return f"Error retrieving Cost Centre details for {company_name}: {e}"

        # 6. GET_RECENT_VOUCHERS
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

                # Limit to top recent vouchers to prevent bloating context
                for v in vouchers[:constants.VOUCHER_DISPLAY_LIMIT]:
                    md.append(f"| {v['date']} | {v['type']} | {v['number']} | {v['party']} | {v['amount']} | {v['narration']} |")

                return "\n".join(md)
            except Exception as e:
                return f"Error retrieving recent transactions for {company_name}: {e}"

        # 7. BUSINESS INTELLIGENCE: TRUST SCORES & TRANSACTION ANALYTICS
        elif intent == "GET_TRUST_SCORES":
            try:
                ref_date = parsed.get("parameters", {}).get("reference_date")
                ref_dt = analytics_engine._parse_date(ref_date or t_date or today_str)
                if ref_dt == datetime.datetime.min:
                    ref_dt = datetime.datetime.now()

                grp = parsed.get("parameters", {}).get("group_name") or "Sundry Debtors"
                metrics = tally_client.fetch_trust_score_metrics(company_name, port, group_name=grp, from_date=f_date, to_date=t_date)
                scores = analytics_engine.compute_trust_scores(
                    party_metrics=metrics,
                    reference_date=ref_dt
                )
                
                display_limit = parsed.get("parameters", {}).get("limit") or constants.DEFAULT_DISPLAY_LIMIT

                if scores:
                    md = [
                        f"## 🏆 Business Intelligence: Counterparty Trust Scores - {company_name} (Port {port})\n",
                        "| Rank | Party Name | Trust Score | Credit Rating | Settlement Rate | Txns | Total Volume (₹) | Overdue (₹) |",
                        "| :---: | :--- | :---: | :--- | :---: | :---: | :--- | :--- |"
                    ]
                    for i, s in enumerate(scores[:display_limit]):
                        md.append(f"| {i+1} | {s['party']} | **{s['trust_score']}%** | {s['rating']} | {s['settlement_rate']}% | {s['txn_count']} | ₹ {s['total_volume']:,.2f} | ₹ {s['overdue_amount']:,.2f} |")
                    if len(scores) > display_limit:
                        md.append(f"\n*(Showing top {display_limit} out of {len(scores)} scored counterparties)*")
                    return "\n".join(md)
                else:
                    # Debtor follow-up prioritization fallback using fast native party balances
                    out_data = tally_client.fetch_party_outstandings(company_name, port, report_type="Receivables", from_date=f_date, to_date=t_date)
                    parties = out_data.get("parties", [])
                    if not parties:
                        return f"[{company_name}] No debtor accounts found for follow-up prioritization."
                    
                    # Sort by outstanding amount descending
                    parties_sorted = sorted(parties, key=lambda x: abs(float(x.get("amount", 0.0))), reverse=True)
                    tot_rec = out_data.get("total_receivable", 0.0)
                    
                    md = [
                        f"## 🎯 Collection Priority & Debtor Follow-Up Dashboard: {company_name} (Port {port})\n",
                        f"> **Total Outstanding Receivables:** ₹ {tot_rec:,.2f} | **Actionable Counterparties:** {len(parties_sorted)}\n",
                        "| Priority Rank | Debtor Account Name | Group Classification | Pending Balance | Follow-Up Recommendation |",
                        "| :---: | :--- | :--- | :---: | :--- |"
                    ]
                    
                    for i, p in enumerate(parties_sorted[:display_limit]):
                        p_amt = abs(float(p.get("amount", 0.0)))
                        p_name = p.get("party", "Unknown")
                        p_grp = p.get("parent", "Sundry Debtors")
                        
                        if i == 0 or p_amt >= 10000000.0:
                            recom = "🔴 **Immediate Action** (Critical Exposure)"
                        elif p_amt >= 2500000.0:
                            recom = "🟠 **High Priority** (Formal Reminder)"
                        elif p_amt >= 500000.0:
                            recom = "🟡 **Routine Follow-Up** (Statement of Acct)"
                        else:
                            recom = "🟢 **Low Risk** (Regular Follow-Up)"
                            
                        md.append(f"| {i+1} | {p_name} | {p_grp} | ₹ {p_amt:,.2f} | {recom} |")
                        
                    if len(parties_sorted) > display_limit:
                        md.append(f"\n*(Showing top {display_limit} out of {len(parties_sorted)} debtors prioritized for follow-up)*")
                        
                    return "\n".join(md)
            except Exception as e:
                return f"Error computing Trust Scores for {company_name}: {e}"

        elif intent == "GET_TOP_VENDORS_BY_TXN":
            try:
                p_filter = parsed.get("parameters", {}).get("date_filter")
                f_dt = f_date if (p_filter and p_filter.get("type") == "explicit_range") else None
                grp = parsed.get("parameters", {}).get("group_name") or "Sundry Creditors"
                stats = tally_client.fetch_party_voucher_counts(company_name, port, group_name=grp, from_date=f_dt, to_date=t_date)
                if not stats:
                    return f"[{company_name}] No transaction counts found for the specified period."

                md = [
                    f"## 📈 Transaction Analytics: Most Frequent Counterparties - {company_name} (Port {port})\n",
                    "| Rank | Party Name | Voucher Count | Total Turnover (₹) | Last Transaction Date |",
                    "| :---: | :--- | :---: | :--- | :--- |"
                ]

                display_limit = parsed.get("parameters", {}).get("limit") or constants.DEFAULT_DISPLAY_LIMIT
                for i, s in enumerate(stats[:display_limit]):
                    md.append(f"| {i+1} | {s['party']} | **{s['voucher_count']}** | ₹ {s['total_amount']:,.2f} | {s['last_date']} |")

                if len(stats) > display_limit:
                    md.append(f"\n*(Showing top {display_limit} out of {len(stats)} active parties)*")

                return "\n".join(md)
            except Exception as e:
                return f"Error retrieving transaction frequency analytics for {company_name}: {e}"

        # 8. BILL/VOUCHER INTENTS
        elif intent == "GET_BILL_DETAILS":

            try:
                document_ref = parsed.get("parameters", {}).get("document_ref")
                if not document_ref:
                    return f"[{company_name}] I couldn't identify the bill number in your query."
                
                # Fetch bills — push bill name filter ($Name) to TDL for fast indexed lookup.
                # Also use resolved party ledger as $Parent filter to narrow scope if available.
                # DO NOT pass document_ref as ledger_filter — $Parent is the party name, not bill name.
                exclude_pdc = not any(k in query.lower() for k in ["net outstanding", "net payable", "net receivable", "netting", "after pdc"])
                resolved_party = parsed.get("resolved_ledger")
                doc_res = tally_client.fetch_bills(company_name, port, "All", from_date=None, to_date=None, exclude_pdc=exclude_pdc, ledger_filter=resolved_party, bill_name_filter=document_ref)
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
                
                is_group_target = resolved_ledger in [constants.GROUP_SUNDRY_DEBTORS, constants.GROUP_SUNDRY_CREDITORS, "Sundry Debtors", "Sundry Creditors", "Debtors", "Creditors"]
                target_single_ledger = None if is_group_target else resolved_ledger

                # Route 1: Fast Master Ledger Summary Route
                # Evaluates party balances when no specific single ledger or specific document lookup is requested
                is_party_summary = (not target_single_ledger) and (not params.get("document_ref")) and (intent in ["GET_RECEIVABLES", "GET_PAYABLES", "GET_TOP_DEBTORS", "GET_TOP_CREDITORS", "GET_AGEING"])
                
                # For party summary, ensure explicit reference_date or t_date is passed as cutoff
                tdl_f_date = f_date
                tdl_t_date = params.get("reference_date") or t_date
                if is_party_summary:
                    q_lower = query.lower()
                    has_rec = any(w in q_lower for w in ["receivable", "debtor", "customer", "client", "collect", "collection"])
                    has_pay = any(w in q_lower for w in ["payable", "creditor", "vendor", "supplier", "paid", "payment to"])
                    
                    if has_pay and not has_rec:
                        r_type = "Payables"
                    elif has_rec and not has_pay:
                        r_type = "Receivables"
                    elif intent in ["GET_PAYABLES", "GET_TOP_CREDITORS"]:
                        r_type = "Payables"
                    elif intent in ["GET_TOP_DEBTORS"]:
                        r_type = "Receivables"
                    else:
                        r_type = "Receivables"

                    party_data = tally_client.fetch_party_outstandings(company_name, port, report_type=r_type, from_date=tdl_f_date, to_date=tdl_t_date, max_limit=constants.MAX_FETCH_LIMIT)
                    tot_out = party_data.get("total_outstanding", 0.0)
                    tot_parties = party_data.get("total_party_count", 0)
                    parties = party_data.get("parties", [])
                    
                    if not parties:
                        return f"[{company_name}] No party outstandings details could be retrieved for the specified period."

                    if params.get("count_only"):
                        return f"[{company_name}] Total {r_type} party count: **{tot_parties}** with total balance of **₹ {tot_out:,.2f}** as of {tdl_t_date or today_str}."

                    if params.get("sum_only"):
                        return f"[{company_name}] Total {r_type} outstanding amount: **₹ {tot_out:,.2f}** across **{tot_parties}** parties as of {tdl_t_date or today_str}."

                    # Apply sorting if specified
                    if params.get("sort"):
                        s_order = params["sort"].get("order", "desc")
                        parties.sort(key=lambda x: x["amount"], reverse=(s_order == "desc"))

                    disp_limit = params.get("limit") or constants.DEFAULT_DISPLAY_LIMIT
                    md = [
                        f"### Analytical Report: Party-Wise {r_type} - {company_name} (Port {port})",
                        f"**Total Outstanding:** ₹ {tot_out:,.2f} | **Total Parties Count:** {tot_parties:,}\n",
                        "| Party Name | Group Lineage | Outstanding Balance | Type |",
                        "| :--- | :--- | :--- | :---: |"
                    ]
                    for p in parties[:disp_limit]:
                        md.append(f"| {p['party']} | {p['parent']} | ₹ {p['amount']:,.2f} | {p['type']} |")
                        
                    if len(parties) > disp_limit:
                        md.append(f"\n*(Showing top {disp_limit} out of {tot_parties} parties)*")
                    return "\n".join(md)
                
                if target_single_ledger or intent == "GET_AGEING":
                    report_type = "All"
                else:
                    report_type = "Payable" if intent == "GET_PAYABLES" or "payable" in query.lower() or "creditor" in query.lower() or "supplier" in query.lower() or "payment" in query.lower() else "Receivable"
                
                # Pass resolved from_date and to_date to TDL to constrain search window
                tdl_f_date = f_date
                tdl_t_date = t_date
                
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
                    ledger_filter=target_single_ledger
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
                        if resolved_ledger.lower() == constants.GROUP_SUNDRY_CREDITORS.lower():
                            group_bills = [b for b in bills if constants.GROUP_SUNDRY_CREDITORS.lower() in b.get("parent_group", "").lower() or "creditor" in b.get("parent_group", "").lower()]
                        elif resolved_ledger.lower() == constants.GROUP_SUNDRY_DEBTORS.lower():
                            group_bills = [b for b in bills if constants.GROUP_SUNDRY_DEBTORS.lower() in b.get("parent_group", "").lower() or "debtor" in b.get("parent_group", "").lower()]
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
                    intervals = params.get("ageing_intervals", constants.DEFAULT_AGEING_INTERVALS)

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
                    # Check for party summary report request (either group-level or dated general query without 'bill'/'invoice')
                    is_party_dated_summary = (not resolved_ledger) and ("bill" not in query.lower()) and ("invoice" not in query.lower())
                    is_group_party_summary = ("party" in query.lower() or "each" in query.lower() or "opening" in query.lower() or "balance" in query.lower()) and resolved_ledger and resolved_ledger.lower() in ["sundry creditors", "sundry debtors"]
                    
                    if is_party_dated_summary:
                        party_groups = {}
                        for b in final_bills:
                            p = b["party"]
                            if p not in party_groups:
                                party_groups[p] = {"pending": 0.0, "parent": b.get("parent_group", ""), "type": "Dr" if intent == "GET_RECEIVABLES" else "Cr"}
                            try:
                                p_val = abs(float(b.get("amount", 0) or 0.0))
                                party_groups[p]["pending"] += p_val
                            except:
                                pass
                        
                        total_pending = sum(v["pending"] for v in party_groups.values())
                        tot_parties = len(party_groups)
                        r_label = "Receivables" if intent == "GET_RECEIVABLES" else "Payables"
                        
                        md = [
                            f"### Analytical Report: Party-Wise {r_label} - {company_name} (Port {port})",
                            f"**Total Outstanding:** ₹ {total_pending:,.2f} | **Total Parties Count:** {tot_parties:,}\n",
                            "| Party Name | Group Lineage | Outstanding Balance | Type |",
                            "| :--- | :--- | :--- | :---: |"
                        ]
                        display_limit = params.get("limit") or constants.DEFAULT_DISPLAY_LIMIT
                        sorted_parties = sorted(party_groups.items(), key=lambda x: x[1]["pending"], reverse=True)
                        for p, vals in sorted_parties[:display_limit]:
                            md.append(f"| {p} | {vals['parent']} | ₹ {vals['pending']:,.2f} | {vals['type']} |")
                            
                        if len(sorted_parties) > display_limit:
                            md.append(f"\n*(Showing top {display_limit} out of {tot_parties} parties)*")
                        return "\n".join(md)
                    
                    elif is_group_party_summary:
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
                        
                        display_limit = params.get("limit") or constants.DEFAULT_DISPLAY_LIMIT
                        sorted_parties = sorted(party_groups.items(), key=lambda x: x[1]["pending"], reverse=True)
                        for p, vals in sorted_parties[:display_limit]:
                            settled = vals["opening"] - vals["pending"]
                            md.append(f"| {p} | ₹ {vals['opening']:,.2f} | ₹ {settled:,.2f} | ₹ {vals['pending']:,.2f} |")
                            
                        if len(sorted_parties) > display_limit:
                            md.append(f"\n*(Showing top {display_limit} out of {len(sorted_parties)} parties)*")
                        return "\n".join(md)
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