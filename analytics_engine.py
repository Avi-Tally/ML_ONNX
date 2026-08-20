from datetime import datetime, timedelta
import date_utils

class AnalyticsEngine:
    def __init__(self):
        pass

    def _parse_date(self, date_str):
        parsed = date_utils.parse_date(date_str)
        return parsed if parsed is not None else datetime.min


    def process_bills(self, bills, intent, params=None, today_str=None):
        if params is None:
            params = {}
            
        filtered_bills = []
        
        for b in bills:
            # Clean foreign currency amount details if present
            amt_str = b.get("amount", "0").strip()
            if "=" in amt_str:
                amt_str = amt_str.split("=")[-1].strip()
            cleaned_amt = "".join(c for c in amt_str if c.isdigit() or c in [".", "-"])
            try:
                amt = float(cleaned_amt)
            except ValueError:
                amt = 0.0
                
            abs_amt = abs(amt)
            b["abs_amount"] = abs_amt
            
            b["parsed_date"] = self._parse_date(b.get("date", ""))
            
            due_str = b.get("due_date", "").strip()
            if "day" in due_str.lower():
                try:
                    days_to_add = int(due_str.lower().split("day")[0].strip())
                    if b["parsed_date"] != datetime.min:
                        b["parsed_due_date"] = b["parsed_date"] + timedelta(days=days_to_add)
                    else:
                        b["parsed_due_date"] = datetime.min
                except:
                    b["parsed_due_date"] = self._parse_date(due_str)
            else:
                b["parsed_due_date"] = self._parse_date(due_str)
            
            # Status filter based on query strings (hacky but works if passed in params)
            is_cleared = bool(b.get("cleared_on", "").strip())
            b["is_cleared"] = is_cleared
            
            filtered_bills.append(b)

        if not filtered_bills:
            return []

        if today_str:
            today = self._parse_date(today_str)
            if today == datetime.min:
                today = datetime.now()
        else:
            dates = [b["parsed_date"] for b in filtered_bills if b["parsed_date"] != datetime.min]
            max_date = max(dates) if dates else datetime.now()
            if max_date < datetime(2025, 1, 1):
                today = max_date
            else:
                today = datetime.now()
            
        for b in filtered_bills:
            b_due = b["parsed_due_date"] if b["parsed_due_date"] != datetime.min else b["parsed_date"]
            b["age_days"] = (today - b_due).days if b_due != datetime.min else 0
            
        # Apply explicit parameters
        final_bills = []
        for b in filtered_bills:
            include = True
            
            # Exclude bills that are invoiced in the future relative to the reporting date
            # Only when the user has NOT asked for future-dated or upcoming bills
            if not params.get("date_filter") or params.get("date_filter", {}).get("type") not in ("next_days", "this_week"):
                if b["parsed_date"] != datetime.min and b["parsed_date"] > today:
                    include = False
                
            # Overdue filter (exclude non-overdue bills with negative/zero age)
            # Only exclude future-due bills when user explicitly asks for overdue
            if params.get("overdue_only") and b["age_days"] <= 0:
                include = False
                
            # Amount filter
            if params.get("amount_filter"):
                op = params["amount_filter"]["operator"]
                val = params["amount_filter"]["value"]
                if op == "<" and b["abs_amount"] >= val: include = False
                elif op == ">" and b["abs_amount"] <= val: include = False
                
            # Age filter
            if params.get("age_filter"):
                op = params["age_filter"]["operator"]
                days = params["age_filter"]["days"]
                if op == "<":
                    if b["age_days"] >= days:
                        include = False
                elif op == ">":
                    if b["age_days"] <= days:
                        include = False
                
            # Date filter (last X days, next X days, explicit range, this_week, today)
            if params.get("date_filter"):
                typ = params["date_filter"]["type"]
                date_target = params.get("date_target", "bill_date")
                
                target_date = b["parsed_due_date"] if date_target == "due_date" else b["parsed_date"]
                if target_date == datetime.min:
                    target_date = b["parsed_date"] if date_target == "due_date" else b["parsed_due_date"]
                    
                if target_date != datetime.min:
                    if typ == "last_days":
                        days = params["date_filter"].get("days", 0)
                        min_date = today - timedelta(days=days)
                        if target_date < min_date or target_date > today:
                            include = False
                    elif typ == "next_days":
                        days = params["date_filter"].get("days", 0)
                        max_due = today + timedelta(days=days)
                        if date_target == "due_date":
                            if target_date > max_due:
                                include = False
                        else:
                            if target_date < today or target_date > max_due:
                                include = False
                    elif typ == "month_year":
                        m_int = params["date_filter"]["month"]
                        y_int = params["date_filter"]["year"]
                        if target_date.month != m_int or target_date.year != y_int:
                            include = False
                    elif typ == "this_week":
                        if date_target == "due_date":
                            max_due = today + timedelta(days=6)
                            if target_date > max_due:
                                include = False
                        else:
                            start_dt = today - timedelta(days=today.weekday())
                            end_dt = start_dt + timedelta(days=6)
                            start_dt = datetime(start_dt.year, start_dt.month, start_dt.day)
                            end_dt = datetime(end_dt.year, end_dt.month, end_dt.day, 23, 59, 59)
                            if target_date < start_dt or target_date > end_dt:
                                include = False
                    elif typ == "today":
                        if date_target == "due_date":
                            if target_date > today:
                                include = False
                        else:
                            if target_date.date() != today.date():
                                include = False
                    elif typ == "explicit_range":
                        start_dt = datetime(params["date_filter"]["start_year"], params["date_filter"]["start_month"], params["date_filter"]["start_day"])
                        end_dt = datetime(params["date_filter"]["end_year"], params["date_filter"]["end_month"], params["date_filter"]["end_day"], 23, 59, 59)
                        if target_date < start_dt or target_date > end_dt:
                            include = False
                else:
                    include = False
                        
            # Status filter
            status_filter = params.get("status_filter")
            if status_filter == "cleared" and not b["is_cleared"]:
                include = False
            elif status_filter == "pending" and b["is_cleared"]:
                include = False
                        
            if include:
                final_bills.append(b)
                
        # Grouping for Top Debtors / Creditors
        if intent in ["GET_TOP_DEBTORS", "GET_TOP_CREDITORS"]:
            party_totals = {}
            for b in final_bills:
                party = b.get("party", "Unknown Party")
                if party not in party_totals:
                    party_totals[party] = 0.0
                party_totals[party] += b["abs_amount"]
                
            grouped_bills = [{"party": p, "abs_amount": amt} for p, amt in party_totals.items()]
            final_bills = grouped_bills
            
        # Sorting
        sort_cfg = params.get("sort")
        if sort_cfg:
            field = sort_cfg["field"]
            order = sort_cfg["order"]
            rev = (order == "desc")
            if field == "bill_date":
                final_bills.sort(key=lambda x: x.get("parsed_date", datetime.min), reverse=rev)
            elif field == "amount":
                final_bills.sort(key=lambda x: x.get("abs_amount", 0.0), reverse=rev)
        else:
            final_bills.sort(key=lambda x: x.get("abs_amount", 0.0), reverse=True)
            
        # Limit
        limit = params.get("limit")
        if limit and limit > 0:
            final_bills = final_bills[:limit]
            
        return final_bills

    def compute_trust_scores(
        self,
        party_metrics: dict = None,
        party_bills: list = None,
        party_vouchers: list = None,
        party_outstandings: list = None,
        reference_date: datetime = None
    ) -> list:
        """
        Computes mathematically rigorous, bounded Trust Score T in [0, 100%]:
        T = [ 0.40 * S_settle + 0.25 * S_freq + 0.20 * S_recent + 0.15 * S_volume ] * (1 - P_overdue) * 100%
        """
        if reference_date is None:
            reference_date = datetime.now()

        party_map = {}

        # 0. High-performance fast path: directly use pre-aggregated scalar metrics
        if party_metrics:
            for p_name, m in party_metrics.items():
                p_clean = p_name.strip()
                if not p_clean:
                    continue
                party_map[p_clean] = {
                    "party": p_clean,
                    "total_invoiced": m.get("total_invoiced", 0.0),
                    "total_settled": m.get("total_settled", 0.0),
                    "total_outstanding": m.get("total_outstanding", 0.0),
                    "overdue_amount": m.get("overdue_amount", 0.0),
                    "bill_count": m.get("bill_count", 1),
                    "voucher_count": m.get("bill_count", 1),
                    "last_txn_date": m.get("last_txn_date"),
                    "parent_group": ""
                }

        # 1. Aggregate Bills Data (Settlement Rate & Overdue Penalty) - Fallback
        elif party_bills:
            for b in party_bills:
                party = b.get("party", "").strip()
                if not party:
                    continue
                if party not in party_map:
                    party_map[party] = {
                        "party": party,
                        "total_invoiced": 0.0,
                        "total_settled": 0.0,
                        "total_outstanding": 0.0,
                        "overdue_amount": 0.0,
                        "bill_count": 0,
                        "voucher_count": 0,
                        "last_txn_date": None,
                        "parent_group": b.get("parent_group", "")
                    }
                
                try:
                    amt = abs(float(b.get("amount", 0)))
                except:
                    amt = 0.0
                    
                is_settled = bool(b.get("is_settled") or b.get("is_cleared"))
                age = b.get("age_days", 0)
                
                party_map[party]["total_invoiced"] += amt
                party_map[party]["bill_count"] += 1
                
                if is_settled:
                    party_map[party]["total_settled"] += amt
                else:
                    party_map[party]["total_outstanding"] += amt
                    if age > 0:
                        party_map[party]["overdue_amount"] += amt

        # 2. Aggregate Vouchers Data (Frequency & Recency)
        if party_vouchers:
            for v in party_vouchers:
                party = v.get("party", "").strip()
                if not party:
                    continue
                if party not in party_map:
                    party_map[party] = {
                        "party": party,
                        "total_invoiced": 0.0,
                        "total_settled": 0.0,
                        "total_outstanding": 0.0,
                        "overdue_amount": 0.0,
                        "bill_count": 0,
                        "voucher_count": 0,
                        "last_txn_date": None,
                        "parent_group": ""
                    }
                
                party_map[party]["voucher_count"] += 1
                v_date_str = v.get("date", "")
                v_date = self._parse_date(v_date_str)
                if v_date != datetime.min:
                    if not party_map[party]["last_txn_date"] or v_date > party_map[party]["last_txn_date"]:
                        party_map[party]["last_txn_date"] = v_date

        # 3. Integrate Party Outstandings
        if party_outstandings:
            for p in party_outstandings:
                p_name = p.get("party") or p.get("name", "")
                if not p_name:
                    continue
                if p_name not in party_map:
                    party_map[p_name] = {
                        "party": p_name,
                        "total_invoiced": abs(float(p.get("amount", 0))),
                        "total_settled": 0.0,
                        "total_outstanding": abs(float(p.get("amount", 0))),
                        "overdue_amount": 0.0,
                        "bill_count": 1,
                        "voucher_count": 1,
                        "last_txn_date": None,
                        "parent_group": p.get("parent", "")
                    }

        if not party_map:
            return []

        # Find max volume for relative normalization
        max_volume = max((p["total_invoiced"] for p in party_map.values()), default=1.0)
        if max_volume <= 0:
            max_volume = 1.0

        scores = []
        for p_name, data in party_map.items():
            tot_inv = data["total_invoiced"]
            tot_settled = data["total_settled"]
            tot_out = data["total_outstanding"]
            overdue = data["overdue_amount"]
            txns = max(data["voucher_count"], data["bill_count"])
            
            # S_settle: Settlement Ratio in [0, 1]
            if tot_inv > 0:
                s_settle = min(1.0, max(0.0, tot_settled / tot_inv))
                if s_settle == 0 and tot_out > 0 and overdue == 0:
                    s_settle = 0.70
            else:
                s_settle = 0.50

            # S_freq: Frequency Score in [0, 1] (capped at 10 transactions)
            s_freq = min(1.0, txns / 10.0)

            # S_recent: Recency Score in [0, 1]
            if data["last_txn_date"]:
                days_since = max(0, (reference_date - data["last_txn_date"]).days)
                s_recent = max(0.0, 1.0 - (days_since / 365.0))
            else:
                s_recent = 0.60

            # S_volume: Volume Score in [0, 1]
            s_volume = min(1.0, tot_inv / max_volume) if max_volume > 0 else 0.5

            # P_overdue: Overdue Penalty in [0, 0.50]
            if tot_out > 0:
                p_overdue = min(0.50, overdue / tot_out)
            else:
                p_overdue = 0.0

            # Weighted Trust Score Calculation
            raw_trust = (0.40 * s_settle + 0.25 * s_freq + 0.20 * s_recent + 0.15 * s_volume) * (1.0 - p_overdue)
            trust_pct = round(min(100.0, max(0.0, raw_trust * 100.0)), 1)

            # Assign Rating Badge
            if trust_pct >= 85.0:
                rating = "🟢 AAA (Exceptional)"
            elif trust_pct >= 70.0:
                rating = "🟢 AA (Very High)"
            elif trust_pct >= 55.0:
                rating = "🟡 A (Good)"
            elif trust_pct >= 40.0:
                rating = "🟠 BBB (Moderate)"
            else:
                rating = "🔴 High Risk"

            scores.append({
                "party": p_name,
                "trust_score": trust_pct,
                "rating": rating,
                "settlement_rate": round(s_settle * 100, 1),
                "txn_count": txns,
                "total_volume": tot_inv,
                "overdue_amount": overdue,
                "outstanding": tot_out
            })

        scores.sort(key=lambda x: x["trust_score"], reverse=True)
        return scores

