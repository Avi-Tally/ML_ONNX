from datetime import datetime, timedelta

class AnalyticsEngine:
    def __init__(self):
        pass

    def _parse_date(self, date_str):
        if not date_str:
            return datetime.min
        date_str = date_str.strip()
        if len(date_str) == 8 and date_str.isdigit():
            try:
                return datetime.strptime(date_str, "%Y%m%d")
            except:
                pass
        
        try:
            return datetime.strptime(date_str, "%d-%b-%Y")
        except:
            pass
            
        try:
            return datetime.strptime(date_str, "%d-%b-%y")
        except:
            pass
            
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except:
            pass
            
        return datetime.min

    def process_bills(self, bills, intent, params=None, today_str=None):
        if params is None:
            params = {}
            
        filtered_bills = []
        
        for b in bills:
            try:
                amt = float(b.get("amount", "0"))
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
            
            # Exclude bills that are invoiced in the future relative to the reporting date (today)
            if b["parsed_date"] != datetime.min and b["parsed_date"] > today:
                include = False
                
            # Exclude bills with a future due date (negative age relative to today)
            if b["age_days"] < 0:
                include = False
                
            # Overdue filter (exclude non-overdue bills with negative/zero age)
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
