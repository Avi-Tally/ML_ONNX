import re

def refactor():
    with open('mcp_server.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add Decimal Import
    if 'from decimal import Decimal' not in content:
        content = content.replace('import asyncio\n', 'import asyncio\nfrom decimal import Decimal, InvalidOperation\n')

    # 2. Update get_amt for GET_LEDGER_360
    old_get_amt1 = '''            def get_amt(b):
                try:
                    return float(str(b.get('amount', 0)).replace(',', '').lstrip('₹').strip())
                except:
                    return 0.0'''
    new_get_amt1 = '''            def get_amt(b):
                try:
                    return Decimal(str(b.get('amount', 0)).replace(',', '').lstrip('₹').strip() or '0')
                except:
                    return Decimal('0.0')'''
    content = content.replace(old_get_amt1, new_get_amt1)

    # 3. Use fetch_bills_optimized in GET_LEDGER_360
    old_ledger360 = '''            # Fetch outstandings for this ledger
            bills = tally_client.fetch_bills(company_name, port, report_type="All", from_date=f_date, to_date=t_date)
            party_bills = [b for b in bills if b.get('party', '').lower() == resolved.lower() or resolved.lower() in b.get('party', '').lower()]'''
    new_ledger360 = '''            # Fetch outstandings for this ledger
            bills = tally_client.fetch_bills_optimized(company_name, port, report_type="All", from_date=f_date, to_date=t_date, ledger_filter=resolved)
            party_bills = bills'''
    content = content.replace(old_ledger360, new_ledger360)
    
    content = content.replace('bal_val = float(bal_str)', 'bal_val = Decimal(bal_str)')

    # 4. Use fetch_ledger_summary in GET_COMPARATIVE_SUMMARY
    old_comp_sum = '''                rec = tally_client.fetch_bills(c_name, c_port, report_type="Receivables", from_date=f_date, to_date=t_date)
                pay = tally_client.fetch_bills(c_name, c_port, report_type="Payables", from_date=f_date, to_date=t_date)
                tot_rec = sum(get_amt(b) for b in rec)
                tot_pay = sum(get_amt(b) for b in pay)
                comp_results.append({
                    "company": c_name,
                    "port": c_port,
                    "receivables": tot_rec,
                    "payables": tot_pay,
                    "net": tot_rec - tot_pay
                })'''
    new_comp_sum = '''                rec_ledgers = tally_client.fetch_ledger_summary(c_name, c_port, group_name="Sundry Debtors", from_date=f_date, to_date=t_date)
                pay_ledgers = tally_client.fetch_ledger_summary(c_name, c_port, group_name="Sundry Creditors", from_date=f_date, to_date=t_date)
                tot_rec = sum(Decimal(str(r['amount'])) for r in rec_ledgers)
                tot_pay = sum(Decimal(str(r['amount'])) for r in pay_ledgers)
                comp_results.append({
                    "company": c_name,
                    "port": c_port,
                    "receivables": tot_rec,
                    "payables": tot_pay,
                    "net": (tot_rec - tot_pay)
                })'''
    content = content.replace(old_comp_sum, new_comp_sum)

    # 5. GET_BILL_DETAILS
    old_bill_det = '''                bills = tally_client.fetch_bills(company_name, port, "All", from_date=None, to_date=None, exclude_pdc=exclude_pdc, ledger_filter=document_ref)'''
    new_bill_det = '''                bills = tally_client.fetch_bills_optimized(company_name, port, "All", from_date=None, to_date=None, exclude_pdc=exclude_pdc, ledger_filter=document_ref)'''
    content = content.replace(old_bill_det, new_bill_det)
    
    content = content.replace('b["abs_amount"] = abs(float(b.get("amount", "0")))', 'b["abs_amount"] = abs(Decimal(str(b.get("amount", "0")).replace(",", "") or "0"))')

    # 6. Extract GET_TOP_DEBTORS
    old_top_debt = '''        # 7. ANALYTICAL INTENTS
        elif intent in ["GET_RECEIVABLES", "GET_PAYABLES", "GET_AGEING", "GET_TOP_DEBTORS", "GET_TOP_CREDITORS"]:'''
    new_top_debt = '''        # 7. TOP DEBTORS / CREDITORS (Tier 2 Fast Queries)
        elif intent in ["GET_TOP_DEBTORS", "GET_TOP_CREDITORS"]:
            try:
                group_name = "Sundry Debtors" if intent == "GET_TOP_DEBTORS" else "Sundry Creditors"
                limit = parsed.get("parameters", {}).get("limit", 10)
                
                # Fast Ledger Query
                ledgers = tally_client.fetch_ledger_summary(company_name, port, group_name=group_name, sort_desc=True, limit=limit, from_date=f_date, to_date=t_date)
                
                md = [f"### Analytical Report: {intent.replace('GET_', '').replace('_', ' ').title()} - {company_name} (Port {port})"]
                
                if not ledgers:
                    md.append("No accounts found.")
                    return "\\n".join(md)
                    
                if parsed.get("parameters", {}).get("count_only") or parsed.get("parameters", {}).get("sum_only"):
                    total_parties = len(ledgers)
                    total_val = sum(l['amount'] for l in ledgers)
                    md.append(f"**Total Parties (in top {limit}):** {total_parties}  |  **Total Value:** ₹ {total_val:,.2f}\\n")
                    
                md.append("| Rank | Party Name | Total Outstanding |")
                md.append("| :--- | :--- | :--- |")
                for i, l in enumerate(ledgers):
                    md.append(f"| {i+1} | {l['party']} | ₹ {l['amount']:,.2f} |")
                    
                return "\\n".join(md)
            except Exception as e:
                return f"Error retrieving top accounts for {company_name}: {e}"

        # 8. ANALYTICAL INTENTS (Ageing, Receivables, Payables)
        elif intent in ["GET_RECEIVABLES", "GET_PAYABLES", "GET_AGEING"]:'''
    content = content.replace(old_top_debt, new_top_debt)

    # 7. Use fetch_bills_optimized for remaining analytics
    old_ana_bills = '''                bills = tally_client.fetch_bills(
                    company_name, 
                    port, 
                    report_type, 
                    from_date=tdl_f_date, 
                    to_date=tdl_t_date, 
                    status_filter=parsed.get("parameters", {}).get("status_filter"),
                    reference_date=parsed.get("parameters", {}).get("reference_date"),
                    exclude_pdc=exclude_pdc,
                    ledger_filter=resolved_ledger
                )'''
    new_ana_bills = '''                bills = tally_client.fetch_bills_optimized(
                    company_name, 
                    port, 
                    report_type, 
                    from_date=tdl_f_date, 
                    to_date=tdl_t_date, 
                    status_filter="pending",
                    reference_date=parsed.get("parameters", {}).get("reference_date"),
                    exclude_pdc=exclude_pdc,
                    ledger_filter=resolved_ledger
                )'''
    content = content.replace(old_ana_bills, new_ana_bills)

    # Remove the old rendering code for top debtors/creditors
    old_render = '''                # Formatter for different intents
                if intent in ["GET_TOP_DEBTORS", "GET_TOP_CREDITORS"]:
                    if params.get("count_only") or params.get("sum_only"):
                        total_parties = len(final_bills)
                        total_val = sum(b['abs_amount'] for b in final_bills)
                        md.append(f"**Total Parties:** {total_parties}  |  **Total Value:** ₹ {total_val:,.2f}\\n")
                        
                    md.append("| Rank | Party Name | Total Outstanding |")
                    md.append("| :--- | :--- | :--- |")
                    for i, b in enumerate(final_bills):
                        md.append(f"| {i+1} | {b['party']} | ₹ {b['abs_amount']:,.2f} |")

                elif intent == "GET_AGEING":'''
    new_render = '''                # Formatter for different intents
                if intent == "GET_AGEING":'''
    content = content.replace(old_render, new_render)
    
    # 8. Decimals for remaining analytical logic
    content = content.replace('raw_amt = float(b.get("amount", "0"))', 'raw_amt = Decimal(str(b.get("amount", "0")).replace(",", "") or "0")')
    content = content.replace('o_val = abs(float(b.get("opening_amount", 0) or 0.0))', 'o_val = abs(Decimal(str(b.get("opening_amount", 0) or "0").replace(",", "")))')
    content = content.replace('p_val = abs(float(b.get("amount", 0) or 0.0))', 'p_val = abs(Decimal(str(b.get("amount", 0) or "0").replace(",", "")))')

    # Also update GET_COMPARATIVE_SUMMARY get_amt 2nd instance
    content = content.replace(old_get_amt1, new_get_amt1)

    with open('mcp_server.py', 'w', encoding='utf-8') as f:
        f.write(content)
        
refactor()
print("Refactor completed successfully.")
