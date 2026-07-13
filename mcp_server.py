import sys
from mcp.server.fastmcp import FastMCP
from tally_client import TallyClient
from nlp_engine import NLPEngine
from analytics_engine import AnalyticsEngine

# Initialize the MCP server
mcp = FastMCP("TallyPrime Local Bridge")

# Initialize Tally Client and NLP Engine
tally_client = TallyClient()
nlp_engine = NLPEngine(tally_client)

import time

@mcp.tool()
def query_tally(query: str) -> str:
    """
    Query the running local TallyPrime instances using natural language.
    Supports:
      - Listing loaded companies (e.g., "what companies are loaded?")
      - Ledger balances (e.g., "what is the balance of Aarkay Enterprises?")
      - Trial Balance reports (e.g., "show trial balance for Modi Chemplast")
      - Stock Summary/Inventory reports (e.g., "inventory summary for Bella Casa")
    Automatically detects and routes queries to port 9000 or 9001.
    """
    start_time = time.time()
    res = _query_tally_internal(query)
    elapsed = time.time() - start_time
    return res + f"\n\n*(Query executed in {elapsed:.2f} seconds)*"


import datetime
def resolve_date_range(params, context):
    ref_date = params.get("reference_date")
    ref_today = ref_date if ref_date else context.get("current_date")
    
    from_date = context.get("from_date")
    to_date = context.get("to_date")
    
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

def _query_tally_internal(query: str) -> str:
    """
    Query the running local TallyPrime instances using natural language.
    Supports:
      - Listing loaded companies (e.g., "what companies are loaded?")
      - Ledger balances (e.g., "what is the balance of Aarkay Enterprises?")
      - Trial Balance reports (e.g., "show trial balance for Modi Chemplast")
      - Stock Summary/Inventory reports (e.g., "inventory summary for Bella Casa")
    Automatically detects and routes queries to port 9000 or 9001.
    """
    try:
        # Re-probe ports in case a company was loaded/unloaded since start
        tally_client.update_routing_table()
    except Exception as e:
        return f"Error: Could not establish connection to TallyPrime. Details: {e}"

    if not tally_client.routing_table:
        return "Error: No active TallyPrime instances detected on ports 9000 or 9001. Please ensure TallyPrime is running and HTTP server is enabled."

    # Parse query through NLP engine
    try:
        parsed = nlp_engine.parse_query(query)
    except Exception as e:
        return f"Error parsing NLP query: {e}"

    intent = parsed["intent"]
    port = parsed["port"]
    company_name = parsed["resolved_company"]
    context_dict = parsed.get("context", {})
    
    # Overwrite today_str if reference_date is parsed (helps with aging relative to a historical date)
    ref_date = parsed.get("parameters", {}).get("reference_date")
    today_str = ref_date if ref_date else context_dict.get("current_date")
    
    f_date, t_date = resolve_date_range(parsed.get("parameters", {}), context_dict)

    def _execute():
        # 1. LIST_COMPANIES
        if intent == "LIST_COMPANIES":
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
                vouchers = tally_client.fetch_recent_vouchers(company_name, port, from_date=f_date, to_date=t_date)
                if not vouchers:
                    return f"[{company_name}] No recent transactions found in the Day Book."

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
                bills = tally_client.fetch_bills(company_name, port, "All", from_date=None, to_date=None)
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
                resolved_ledger = parsed.get("resolved_ledger")
                
                if resolved_ledger or intent == "GET_AGEING" or "bill" in query.lower() or "invoice" in query.lower():
                    report_type = "All"
                else:
                    report_type = "Payable" if intent == "GET_PAYABLES" or "payable" in query.lower() or "creditor" in query.lower() or "supplier" in query.lower() or "payment" in query.lower() else "Receivable"
                
                # If target is due_date, we pull all bills and filter in python, so we don't pass f_date and t_date to TDL
                date_target = parsed.get("parameters", {}).get("date_target", "bill_date")
                tdl_f_date = None if date_target == "due_date" else f_date
                tdl_t_date = None if date_target == "due_date" else t_date
                
                bills = tally_client.fetch_bills(
                    company_name, 
                    port, 
                    report_type, 
                    from_date=tdl_f_date, 
                    to_date=tdl_t_date, 
                    status_filter=parsed.get("parameters", {}).get("status_filter"),
                    reference_date=parsed.get("parameters", {}).get("reference_date")
                )
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
                        net_total = 0.0
                        for b in final_bills:
                            if intent == "GET_RECEIVABLES":
                                net_total += b.get("normalized_receivables_amount", 0.0)
                            else: # GET_PAYABLES
                                net_total += b.get("normalized_payables_amount", 0.0)


                        if params.get("count_only") or params.get("sum_only"):
                            if params.get("count_only") and params.get("sum_only"):
                                md.append(f"**Total Bills:** {len(final_bills)}  |  **Total Value:** ₹ {net_total:,.2f}\n")
                            elif params.get("sum_only"):
                                md.append(f"**Total Value:** ₹ {net_total:,.2f}\n")
                            else:
                                md.append(f"**Total Bills:** {len(final_bills)}\n")
                            return "\n".join(md)
                        else:
                            md.append(f"**Total Outstanding:** ₹ {net_total:,.2f}\n")

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
            except Exception as e:
                return f"Error retrieving analytical data for {company_name}: {e}"

        return f"I understood the query but could not resolve an actionable intent. (Detected: {intent})"

    
    result = _execute()
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
            return header + result
    return result

if __name__ == "__main__":
    # Start stdio server
    mcp.run()