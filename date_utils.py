"""
==============================================================================
MODULE: TEMPORAL RESOLUTION & DATE UTILITIES (date_utils.py)

PURPOSE:
  Provides unified, zero-ambiguity date parsing, fiscal year alignment, 
  and temporal boundary resolution for natural language accounting queries.

CORE ACCOUNTING MECHANICS:
  1. Indian Fiscal Year Alignment (Standard Tally Books):
     - Financial Year runs from April 1 of Year Y to March 31 of Year Y+1 (e.g., FY 17-18).
     - Q1: Apr 1 - Jun 30 | Q2: Jul 1 - Sep 30 | Q3: Oct 1 - Dec 31 | Q4: Jan 1 - Mar 31.
  2. Temporal Anchor Resolution (SVCURRENTDATE / Point-in-Time):
     - Normalizes relative tokens ('this month', 'last 30 days', 'past quarter', 'last week')
       against the active company's historical current_date (or real-world datetime.now()).
  3. Strict String Serialization:
     - Tally Internal / TDL Date: YYYYMMDD (e.g., 20170815)
     - Standard Presentation Format: DD-MMM-YYYY (e.g., 15-Aug-2017)
==============================================================================
"""

import re
import calendar
from datetime import datetime, timedelta
from typing import Optional, Tuple, Dict, Any

MONTH_NAMES = {
    'january': 1, 'jan': 1,
    'february': 2, 'feb': 2,
    'march': 3, 'mar': 3,
    'april': 4, 'apr': 4,
    'may': 5,
    'june': 6, 'jun': 6,
    'july': 7, 'jul': 7,
    'august': 8, 'aug': 8,
    'september': 9, 'sep': 9, 'sept': 9,
    'october': 10, 'oct': 10,
    'november': 11, 'nov': 11,
    'december': 12, 'dec': 12
}

NUM_TO_MONTH = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
}


def parse_date(date_str: Optional[str]) -> Optional[datetime]:
    """
    Canonical multi-format date parser for Tally string inputs.
    Supports compact numeric (YYYYMMDD), formatted strings (DD-MMM-YYYY, DD/MM/YYYY, ISO), etc.
    Returns None if date_str cannot be parsed.
    """
    if not date_str or not isinstance(date_str, str):
        return None
    
    cleaned = date_str.strip()
    if not cleaned:
        return None

    # 1. 8-digit compact numeric YYYYMMDD (standard Tally internal format)
    if len(cleaned) == 8 and cleaned.isdigit():
        try:
            return datetime.strptime(cleaned, "%Y%m%d")
        except ValueError:
            pass

    # 2. Standard Tally display formats
    formats_to_try = (
        "%d-%b-%Y",  # 15-Aug-2017
        "%d-%b-%y",  # 15-Aug-17
        "%d %b %Y",  # 15 Aug 2017
        "%d %b %y",  # 15 Aug 17
        "%Y-%m-%d",  # 2017-08-15
        "%d-%m-%Y",  # 15-08-2017
        "%d/%m/%Y",  # 15/08/2017
        "%d/%m/%y",  # 15/08/17
        "%d.%m.%Y",  # 15.08.2017
        "%d.%m.%y",  # 15.08.17
        "%B %d, %Y", # August 15, 2017
        "%b %d, %Y", # Aug 15, 2017
        "%d %B %Y",  # 15 August 2017
        "%d %B %y",  # 15 August 17
        "%b-%y",     # Aug-17
        "%b-%Y",     # Aug-2017
        "%b %Y",     # Aug 2017
        "%b %y",     # Aug 17
    )

    for fmt in formats_to_try:
        try:
            return datetime.strptime(cleaned, fmt)
        except ValueError:
            continue

    return None


def to_tally_date(dt: Optional[datetime]) -> str:
    """
    Serialize datetime to TDL XML static variable format: YYYYMMDD.
    """
    if dt is None:
        return ""
    return dt.strftime("%Y%m%d")


def to_display_date(dt: Optional[datetime]) -> str:
    """
    Serialize datetime to user-facing Markdown display format: DD-MMM-YYYY.
    """
    if dt is None:
        return ""
    return dt.strftime("%d-%b-%Y")


def get_last_day_of_month(year: int, month: int) -> int:
    """Returns the last day number of a given month and year."""
    return calendar.monthrange(year, month)[1]


def infer_year_for_month(month: int, ref_dt: datetime) -> int:
    """
    Infers the correct calendar year for a given month relative to an Indian Fiscal Year.
    If ref_dt is in FY 2017-18 (Apr 2017 - Mar 2018):
      - Months 4..12 (Apr..Dec) belong to 2017
      - Months 1..3 (Jan..Mar) belong to 2018
    """
    fy_start_year = ref_dt.year if ref_dt.month >= 4 else ref_dt.year - 1
    return fy_start_year if month >= 4 else fy_start_year + 1


def compute_fiscal_year(reference_date: datetime) -> Tuple[datetime, datetime]:
    """
    Compute Indian Fiscal Year bounds (01-Apr to 31-Mar) for a given reference date.
    """
    year = reference_date.year
    if reference_date.month < 4:
        # e.g., Jan 2025 -> FY is 01-Apr-2024 to 31-Mar-2025
        fy_start = datetime(year - 1, 4, 1)
        fy_end = datetime(year, 3, 31)
    else:
        # e.g., Aug 2025 -> FY is 01-Apr-2025 to 31-Mar-2026
        fy_start = datetime(year, 4, 1)
        fy_end = datetime(year + 1, 3, 31)
    return fy_start, fy_end


def extract_dates_from_query(query: str, ref_date_str: Optional[str] = None, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Comprehensive NLP Date & Temporal Extractor.
    Extracts date filters, point-in-time reference dates, and explicit date ranges
    from natural language query strings with support for informal accounting syntax.
    """
    q = query.lower()
    
    # Establish base reference date
    ref_dt = parse_date(ref_date_str) if ref_date_str else None
    if not ref_dt and context:
        ref_dt = parse_date(context.get("current_date"))
    if not ref_dt:
        ref_dt = datetime.now()

    month_regex_str = r'(?:january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)'

    # 0A. Explicit Named Date Ranges (e.g., 'from 1 apr 17 to 8oct17', '1 apr to 8 oct 17', 'between 1 april 2017 and 8 october 2017')
    m_named_range = re.search(
        r'\b(?:from\s+|between\s+)?'
        r'(\d{1,2})(?:st|nd|rd|th)?[\s\-\/\.]*(' + month_regex_str + r')(?:[\s\-\/\.]*(\d{2,4}))?'
        r'\s*(?:to|-|and)\s*'
        r'(\d{1,2})(?:st|nd|rd|th)?[\s\-\/\.]*(' + month_regex_str + r')(?:[\s\-\/\.]*(\d{2,4}))?\b',
        q
    )
    if m_named_range:
        d1_raw, m1_raw, y1_raw, d2_raw, m2_raw, y2_raw = m_named_range.groups()
        if y2_raw and not y1_raw:
            y1_raw = y2_raw
        elif y1_raw and not y2_raw:
            y2_raw = y1_raw
            
        d1 = int(d1_raw)
        m1 = MONTH_NAMES[m1_raw.lower()]
        y1 = (int("20" + y1_raw) if len(y1_raw) == 2 else int(y1_raw)) if y1_raw else infer_year_for_month(m1, ref_dt)
        
        d2 = int(d2_raw)
        m2 = MONTH_NAMES[m2_raw.lower()]
        y2 = (int("20" + y2_raw) if len(y2_raw) == 2 else int(y2_raw)) if y2_raw else infer_year_for_month(m2, ref_dt)
        
        from_date = f"{d1:02d}-{NUM_TO_MONTH[m1]}-{y1}"
        to_date = f"{d2:02d}-{NUM_TO_MONTH[m2]}-{y2}"
        date_filter = {"type": "explicit_range", "start_day": d1, "start_month": m1, "start_year": y1, "end_day": d2, "end_month": m2, "end_year": y2}
        return {"from_date": from_date, "to_date": to_date, "date_filter": date_filter, "reference_date": None}

    # 0B. Explicit Numeric Date Ranges (e.g., 'from 01-04-2017 to 08-10-2017', '01/04/17 to 08/10/17')
    m_num_range = re.search(
        r'\b(?:from\s+|between\s+)?'
        r'(\d{1,2})[\-\/\.](\d{1,2})[\-\/\.](\d{2,4})'
        r'\s*(?:to|-|and)\s*'
        r'(\d{1,2})[\-\/\.](\d{1,2})[\-\/\.](\d{2,4})\b',
        q
    )
    if m_num_range:
        d1, m1, y1, d2, m2, y2 = [int(x) for x in m_num_range.groups()]
        if 1 <= m1 <= 12 and 1 <= d1 <= 31 and 1 <= m2 <= 12 and 1 <= d2 <= 31:
            if y1 < 100: y1 += 2000
            if y2 < 100: y2 += 2000
            from_date = f"{d1:02d}-{NUM_TO_MONTH[m1]}-{y1}"
            to_date = f"{d2:02d}-{NUM_TO_MONTH[m2]}-{y2}"
            date_filter = {"type": "explicit_range", "start_day": d1, "start_month": m1, "start_year": y1, "end_day": d2, "end_month": m2, "end_year": y2}
            return {"from_date": from_date, "to_date": to_date, "date_filter": date_filter, "reference_date": None}

    # 1. Point-in-time exact dates (DD-MMM-YYYY, DD/MM/YYYY, DD-MM-YYYY, YYYY-MM-DD, 8oct17, 08oct2017, 31mar18, on 15 june 17, dated 02-03-2025)
    # 1A. Dates with named months (e.g., '8oct17', 'on 8oct17', '15-aug-2017', 'as of 31mar18', 'dated 15 june 17')
    m_named_date = re.search(r'\b(?:(as\s+on|as\s+of|till|up\s+to|on|dated|date|balance\s+as\s+at)\s+)?(\d{1,2})(?:st|nd|rd|th)?[\s\-\/\.]*(' + month_regex_str + r')[\s\-\/\.]*(\d{2,4})\b', q)
    if m_named_date:
        prefix = (m_named_date.group(1) or "").strip().lower()
        d = int(m_named_date.group(2))
        m_raw = m_named_date.group(3).lower()
        y = int(m_named_date.group(4))
        if y < 100: y += 2000
        m = MONTH_NAMES[m_raw]
        ref_str = f"{d:02d}-{NUM_TO_MONTH[m]}-{y}"
        if prefix in ["as on", "as of", "till", "up to", "balance as at"]:
            return {"from_date": None, "to_date": ref_str, "date_filter": None, "reference_date": ref_str}
        elif prefix in ["on", "dated", "date"]:
            date_filter = {"type": "single_date", "day": d, "month": m, "year": y}
            return {"from_date": ref_str, "to_date": ref_str, "date_filter": date_filter, "reference_date": ref_str}
        else:
            # Standalone point-in-time date (e.g. '8oct17', '15-aug-2017')
            return {"from_date": None, "to_date": ref_str, "date_filter": None, "reference_date": ref_str}

    # 1B. Numeric dates with standard separators (e.g., '08-10-2017', '8/10/17', 'on 15/06/2017')
    m_num_date = re.search(r'\b(?:(as\s+on|as\s+of|till|up\s+to|on|dated|date|balance\s+as\s+at)\s+)?(\d{1,2})[\-\/\.](\d{1,2})[\-\/\.](\d{2,4})\b', q)
    if m_num_date:
        prefix = (m_num_date.group(1) or "").strip().lower()
        d = int(m_num_date.group(2))
        m = int(m_num_date.group(3))
        y = int(m_num_date.group(4))
        if 1 <= m <= 12 and 1 <= d <= 31:
            if y < 100: y += 2000
            ref_str = f"{d:02d}-{NUM_TO_MONTH[m]}-{y}"
            if prefix in ["as on", "as of", "till", "up to", "balance as at"]:
                return {"from_date": None, "to_date": ref_str, "date_filter": None, "reference_date": ref_str}
            elif prefix in ["on", "dated", "date"]:
                date_filter = {"type": "single_date", "day": d, "month": m, "year": y}
                return {"from_date": ref_str, "to_date": ref_str, "date_filter": date_filter, "reference_date": ref_str}
            else:
                return {"from_date": None, "to_date": ref_str, "date_filter": None, "reference_date": ref_str}

    # 2. Explicit FY: "fy 17-18", "fy 2017-18", "fy 2017-2018", "fy17-18", "fy17"
    m_fy = re.search(r'\bfy\s*(?:20)?(\d{2})(?:\s*-\s*(?:20)?(\d{2}))?\b', q)
    if m_fy:
        sy = int("20" + m_fy.group(1))
        ey = int("20" + m_fy.group(2)) if m_fy.group(2) else sy + 1
        from_date = f"01-Apr-{sy}"
        to_date = f"31-Mar-{ey}"
        date_filter = {"type": "explicit_range", "start_day": 1, "start_month": 4, "start_year": sy, "end_day": 31, "end_month": 3, "end_year": ey}
        return {"from_date": from_date, "to_date": to_date, "date_filter": date_filter, "reference_date": None}

    # 3. Month Ranges: "may to june", "may to june 17", "may 2017 to june 2017", "from apr to sep", "between may and june", "may-june 17"
    m_mrange = re.search(r'(?:from\s+|between\s+)?(' + month_regex_str + r')(?:\s*[\'-]?\s*(\d{2,4}))?\s*(?:to|-|and)\s*(' + month_regex_str + r')(?:\s*[\'-]?\s*(\d{2,4}))?\b', q)
    if m_mrange:
        m1_str = m_mrange.group(1)
        y1_str = m_mrange.group(2)
        m2_str = m_mrange.group(3)
        y2_str = m_mrange.group(4)
        
        m1 = MONTH_NAMES[m1_str]
        m2 = MONTH_NAMES[m2_str]
        
        if y2_str:
            y2 = int("20" + y2_str) if len(y2_str) == 2 else int(y2_str)
        elif y1_str:
            y2 = int("20" + y1_str) if len(y1_str) == 2 else int(y1_str)
        else:
            y2 = infer_year_for_month(m2, ref_dt)
            
        if y1_str:
            y1 = int("20" + y1_str) if len(y1_str) == 2 else int(y1_str)
        elif y2_str:
            y1 = y2
        else:
            y1 = infer_year_for_month(m1, ref_dt)
            if m1 > m2 and not y1_str and not y2_str:
                y2 = y1 + 1
                
        last_d = get_last_day_of_month(y2, m2)
        from_date = f"01-{NUM_TO_MONTH[m1]}-{y1}"
        to_date = f"{last_d:02d}-{NUM_TO_MONTH[m2]}-{y2}"
        date_filter = {"type": "explicit_range", "start_day": 1, "start_month": m1, "start_year": y1, "end_day": last_d, "end_month": m2, "end_year": y2}
        return {"from_date": from_date, "to_date": to_date, "date_filter": date_filter, "reference_date": None}

    # 4. Compact Month+Year: "apr17", "apr-17", "apr 17", "apr'17", "april17", "april 2017", "apr 2017"
    m_my = re.search(r'\b(' + month_regex_str + r')\s*[\'-]?\s*(\d{2,4})\b', q)
    if m_my:
        m_str = m_my.group(1)
        y_str = m_my.group(2)
        m = MONTH_NAMES[m_str]
        y = int("20" + y_str) if len(y_str) == 2 else int(y_str)
        last_d = get_last_day_of_month(y, m)
        from_date = f"01-{NUM_TO_MONTH[m]}-{y}"
        to_date = f"{last_d:02d}-{NUM_TO_MONTH[m]}-{y}"
        date_filter = {"type": "month_year", "month": m, "year": y}
        return {"from_date": from_date, "to_date": to_date, "date_filter": date_filter, "reference_date": None}

    # 5. Standalone Month: "in april", "for may", "during august" (no explicit year)
    m_month_only = re.search(r'\b(?:in|for|of|during|month\s+of)?\s*(' + month_regex_str + r')\b', q)
    if m_month_only:
        m_str = m_month_only.group(1)
        is_modal_may = (m_str == "may" and not any(k in q for k in ["in may", "for may", "of may", "month", "sales", "purchase", "voucher", "bill", "balance", "dated", "2017", "17"]))
        if not is_modal_may:
            m = MONTH_NAMES[m_str]
            y = infer_year_for_month(m, ref_dt)
            last_d = get_last_day_of_month(y, m)
            from_date = f"01-{NUM_TO_MONTH[m]}-{y}"
            to_date = f"{last_d:02d}-{NUM_TO_MONTH[m]}-{y}"
            date_filter = {"type": "month_year", "month": m, "year": y}
            return {"from_date": from_date, "to_date": to_date, "date_filter": date_filter, "reference_date": None}

    # 6. Relative Months: "this month", "last month", "next month"
    if "this month" in q or "current month" in q:
        m = ref_dt.month
        y = ref_dt.year
        last_d = get_last_day_of_month(y, m)
        from_date = f"01-{NUM_TO_MONTH[m]}-{y}"
        to_date = f"{last_d:02d}-{NUM_TO_MONTH[m]}-{y}"
        date_filter = {"type": "this_month"}
        return {"from_date": from_date, "to_date": to_date, "date_filter": date_filter, "reference_date": None}
        
    if "last month" in q or "previous month" in q or "past month" in q:
        first_this = datetime(ref_dt.year, ref_dt.month, 1)
        prev_month_dt = first_this - timedelta(days=1)
        m = prev_month_dt.month
        y = prev_month_dt.year
        last_d = get_last_day_of_month(y, m)
        from_date = f"01-{NUM_TO_MONTH[m]}-{y}"
        to_date = f"{last_d:02d}-{NUM_TO_MONTH[m]}-{y}"
        date_filter = {"type": "last_month"}
        return {"from_date": from_date, "to_date": to_date, "date_filter": date_filter, "reference_date": None}

    if "next month" in q:
        first_this = datetime(ref_dt.year, ref_dt.month, 1)
        next_month_dt = first_this + timedelta(days=32)
        m = next_month_dt.month
        y = next_month_dt.year
        last_d = get_last_day_of_month(y, m)
        from_date = f"01-{NUM_TO_MONTH[m]}-{y}"
        to_date = f"{last_d:02d}-{NUM_TO_MONTH[m]}-{y}"
        date_filter = {"type": "next_month"}
        return {"from_date": from_date, "to_date": to_date, "date_filter": date_filter, "reference_date": None}

    # 7. Weeks: "this week", "last week", "next week"
    if "this week" in q:
        start_dt = ref_dt - timedelta(days=ref_dt.weekday())
        end_dt = start_dt + timedelta(days=6)
        from_date = to_display_date(start_dt)
        to_date = to_display_date(end_dt)
        date_filter = {"type": "this_week"}
        return {"from_date": from_date, "to_date": to_date, "date_filter": date_filter, "reference_date": None}

    if "last week" in q or "past week" in q:
        start_this = ref_dt - timedelta(days=ref_dt.weekday())
        start_last = start_this - timedelta(days=7)
        end_last = start_last + timedelta(days=6)
        from_date = to_display_date(start_last)
        to_date = to_display_date(end_last)
        date_filter = {"type": "last_week"}
        return {"from_date": from_date, "to_date": to_date, "date_filter": date_filter, "reference_date": None}

    if "next week" in q:
        start_this = ref_dt - timedelta(days=ref_dt.weekday())
        start_next = start_this + timedelta(days=7)
        end_next = start_next + timedelta(days=6)
        from_date = to_display_date(start_next)
        to_date = to_display_date(end_next)
        date_filter = {"type": "next_week"}
        return {"from_date": from_date, "to_date": to_date, "date_filter": date_filter, "reference_date": None}

    # 8. Quarters: Q1, Q2, Q3, Q4, this quarter, last quarter
    m_q = re.search(r'\b(?:in\s+|for\s+)?q([1-4])(?:\s*(?:fy)?\s*(?:20)?(\d{2}))?\b', q)
    if m_q:
        q_num = int(m_q.group(1))
        q_yr_str = m_q.group(2)
        base_yr = int("20" + q_yr_str) if q_yr_str else (ref_dt.year if ref_dt.month >= 4 else ref_dt.year - 1)
        if q_num == 1:
            from_date, to_date = f"01-Apr-{base_yr}", f"30-Jun-{base_yr}"
        elif q_num == 2:
            from_date, to_date = f"01-Jul-{base_yr}", f"30-Sep-{base_yr}"
        elif q_num == 3:
            from_date, to_date = f"01-Oct-{base_yr}", f"31-Dec-{base_yr}"
        elif q_num == 4:
            from_date, to_date = f"01-Jan-{base_yr+1}", f"31-Mar-{base_yr+1}"
        date_filter = {"type": "quarter", "quarter": q_num, "year": base_yr}
        return {"from_date": from_date, "to_date": to_date, "date_filter": date_filter, "reference_date": None}

    # 9. Relative Days: "next 10 days", "last 30 days", "past 7 days"
    m_days = re.search(r'\b(next|last|past)\s+(\d+)\s+days\b', q)
    if m_days:
        dir_str = m_days.group(1)
        days = int(m_days.group(2))
        if dir_str == "next":
            end_dt = ref_dt + timedelta(days=days)
            from_date = to_display_date(ref_dt)
            to_date = to_display_date(end_dt)
            date_filter = {"type": "next_days", "days": days}
        else:
            start_dt = ref_dt - timedelta(days=days)
            from_date = to_display_date(start_dt)
            to_date = to_display_date(ref_dt)
            date_filter = {"type": "last_days", "days": days}
        return {"from_date": from_date, "to_date": to_date, "date_filter": date_filter, "reference_date": None}

    # 10. General Relative Point-in-Time: "today", "till date", "till today"
    if "today" in q or "till date" in q or "till today" in q:
        to_date = to_display_date(ref_dt)
        date_filter = {"type": "till_today"}
        return {"from_date": None, "to_date": to_date, "date_filter": date_filter, "reference_date": to_date}

    # Default: No explicit date filter in query
    return {
        "from_date": None,
        "to_date": None,
        "date_filter": None,
        "reference_date": None
    }


def resolve_date_range(params: Dict[str, Any], context: Dict[str, Any]) -> Tuple[Optional[str], Optional[str]]:
    """
    Resolves (from_date, to_date) strings in %d-%b-%Y format based on
    the parameter envelope and company context.
    Single source of truth for all intent handlers and TDL XML generators.
    """
    ref_date = params.get("reference_date")
    ref_today = ref_date if ref_date else (context.get("current_date") or datetime.now().strftime("%d-%b-%Y"))
    ref_dt = parse_date(ref_today) or datetime.now()
    
    from_date = context.get("from_date")
    to_date = context.get("to_date")
    
    date_filter = params.get("date_filter")
    
    if date_filter and isinstance(date_filter, dict):
        filter_type = date_filter.get("type")
        
        if filter_type == "this_month":
            m = ref_dt.month
            y = ref_dt.year
            last_d = get_last_day_of_month(y, m)
            from_date = f"01-{NUM_TO_MONTH[m]}-{y}"
            to_date = f"{last_d:02d}-{NUM_TO_MONTH[m]}-{y}"

        elif filter_type == "last_month":
            first_this = datetime(ref_dt.year, ref_dt.month, 1)
            prev_month_dt = first_this - timedelta(days=1)
            m = prev_month_dt.month
            y = prev_month_dt.year
            last_d = get_last_day_of_month(y, m)
            from_date = f"01-{NUM_TO_MONTH[m]}-{y}"
            to_date = f"{last_d:02d}-{NUM_TO_MONTH[m]}-{y}"

        elif filter_type == "next_month":
            first_this = datetime(ref_dt.year, ref_dt.month, 1)
            next_month_dt = first_this + timedelta(days=32)
            m = next_month_dt.month
            y = next_month_dt.year
            last_d = get_last_day_of_month(y, m)
            from_date = f"01-{NUM_TO_MONTH[m]}-{y}"
            to_date = f"{last_d:02d}-{NUM_TO_MONTH[m]}-{y}"

        elif filter_type == "this_week":
            start_dt = ref_dt - timedelta(days=ref_dt.weekday())
            end_dt = start_dt + timedelta(days=6)
            from_date = to_display_date(start_dt)
            to_date = to_display_date(end_dt)

        elif filter_type == "last_week":
            start_this = ref_dt - timedelta(days=ref_dt.weekday())
            start_last = start_this - timedelta(days=7)
            end_last = start_last + timedelta(days=6)
            from_date = to_display_date(start_last)
            to_date = to_display_date(end_last)

        elif filter_type == "next_week":
            start_this = ref_dt - timedelta(days=ref_dt.weekday())
            start_next = start_this + timedelta(days=7)
            end_next = start_next + timedelta(days=6)
            from_date = to_display_date(start_next)
            to_date = to_display_date(end_next)

        elif filter_type == "quarter":
            q_num = date_filter.get("quarter", 1)
            base_yr = date_filter.get("year", ref_dt.year if ref_dt.month >= 4 else ref_dt.year - 1)
            if q_num == 1:
                from_date, to_date = f"01-Apr-{base_yr}", f"30-Jun-{base_yr}"
            elif q_num == 2:
                from_date, to_date = f"01-Jul-{base_yr}", f"30-Sep-{base_yr}"
            elif q_num == 3:
                from_date, to_date = f"01-Oct-{base_yr}", f"31-Dec-{base_yr}"
            elif q_num == 4:
                from_date, to_date = f"01-Jan-{base_yr+1}", f"31-Mar-{base_yr+1}"

        elif filter_type == "last_days":
            days = date_filter.get("days", 0)
            start_dt = ref_dt - timedelta(days=days)
            from_date = to_display_date(start_dt)
            to_date = to_display_date(ref_dt)

        elif filter_type == "next_days":
            days = date_filter.get("days", 0)
            end_dt = ref_dt + timedelta(days=days)
            from_date = to_display_date(ref_dt)
            to_date = to_display_date(end_dt)

        elif filter_type == "month_year":
            try:
                m = date_filter["month"]
                y = date_filter["year"]
                last_d = get_last_day_of_month(y, m)
                from_date = f"01-{NUM_TO_MONTH[m]}-{y}"
                to_date = f"{last_d:02d}-{NUM_TO_MONTH[m]}-{y}"
            except (KeyError, ValueError):
                pass

        elif filter_type == "explicit_range":
            try:
                start_dt = datetime(date_filter["start_year"], date_filter["start_month"], date_filter["start_day"])
                end_dt = datetime(date_filter["end_year"], date_filter["end_month"], date_filter["end_day"])
                from_date = to_display_date(start_dt)
                to_date = to_display_date(end_dt)
            except (KeyError, ValueError):
                pass

        elif filter_type == "single_date":
            try:
                d = date_filter["day"]
                m = date_filter["month"]
                y = date_filter["year"]
                d_str = f"{d:02d}-{NUM_TO_MONTH[m]}-{y}"
                from_date = d_str
                to_date = d_str
            except (KeyError, ValueError):
                pass

        elif filter_type == "today":
            from_date = to_display_date(ref_dt)
            to_date = to_display_date(ref_dt)

        elif filter_type == "till_today":
            from_date = None
            to_date = to_display_date(ref_dt)
            
        elif filter_type == "fy":
            fy_start, fy_end = compute_fiscal_year(ref_dt)
            from_date = to_display_date(fy_start)
            to_date = to_display_date(fy_end)

    elif ref_date:
        # ref_date is an anchor point (upper bound), NOT a single-day window.
        from_date = None
        to_date = ref_date

    return from_date, to_date
