"""
Centralized Configuration and Constant Definitions for ML_ONNX Tally Integration Pipeline.
Strictly single source of truth for group names, date bounds, timeouts, limits, and TDL macros.
"""

# =====================================================================
# Tally Standard Chart of Accounts Group Hierarchies
# =====================================================================
GROUP_SUNDRY_DEBTORS = "Sundry Debtors"
GROUP_SUNDRY_CREDITORS = "Sundry Creditors"
GROUP_TRADE_RECEIVABLES = "Trade Receivables"
GROUP_TRADE_PAYABLES = "Trade Payables"
GROUP_BANK_ACCOUNTS = "Bank Accounts"
GROUP_CASH_IN_HAND = "Cash-in-Hand"
GROUP_BANK_OD = "Bank OD A/c"

RECEIVABLE_GROUPS = {
    GROUP_SUNDRY_DEBTORS,
    GROUP_TRADE_RECEIVABLES,
}

PAYABLE_GROUPS = {
    GROUP_SUNDRY_CREDITORS,
    GROUP_TRADE_PAYABLES,
}

CASH_BANK_GROUPS = {
    GROUP_BANK_ACCOUNTS,
    GROUP_CASH_IN_HAND,
    GROUP_BANK_OD,
}

# Standard Queryable Root Groups for Native Group Summary Reports
QUERYABLE_ROOT_GROUPS = (
    RECEIVABLE_GROUPS
    | PAYABLE_GROUPS
    | CASH_BANK_GROUPS
    | {
        "Direct Expenses",
        "Indirect Expenses",
        "Direct Incomes",
        "Indirect Incomes",
        "Fixed Assets",
        "Investments",
        "Loans & Advances (Asset)",
        "Current Assets",
        "Current Liabilities",
        "Secured Loans",
        "Unsecured Loans",
        "Capital Account",
        "Duties & Taxes",
        "Provisions",
        "Misc. Expenses (ASSET)",
        "Branch / Divisions",
        "Suspense A/c",
    }
)

# =====================================================================
# TDL Date Boundaries (Point-in-Time Epochs)
# =====================================================================
DATE_EPOCH = "19000101"       # Tally historical beginning-of-time (01-Jan-1900)
DATE_FAR_FUTURE = "20991231"  # Tally far future upper bound (31-Dec-2099)

# =====================================================================
# Network & Streaming Sockets Configuration
# =====================================================================
DEFAULT_HTTP_TIMEOUT = 12.0
FAST_PROBE_TIMEOUT = 0.6
DEFAULT_STREAM_TIMEOUT = 30.0
CHUNK_SOCKET_TIMEOUT = 8.0

# =====================================================================
# Reporting & Display Constraints
# =====================================================================
DEFAULT_DISPLAY_LIMIT = 25
MAX_FETCH_LIMIT = 200
VOUCHER_DISPLAY_LIMIT = 20
DEFAULT_AGEING_INTERVALS = [30, 60, 90]

# =====================================================================
# TDL Native Macros & Enums
# =====================================================================
TDL_EXPORT_FORMAT = "$$SysName:XML"

VOUCHER_TYPE_MACROS = {
    "sales": "$$VchTypeSales",
    "purchase": "$$VchTypePurchase",
    "receipt": "$$VchTypeReceipt",
    "payment": "$$VchTypePayment",
    "journal": "$$VchTypeJournal",
    "contra": "$$VchTypeContra",
    "credit_note": "$$VchTypeCreditNote",
    "debit_note": "$$VchTypeDebitNote",
}

# =====================================================================
# Company Default Active Reference Dates
# =====================================================================
COMPANY_DEFAULT_DATES = {
    "bella casa": "20-Sep-2017",
    "bella casa data for user activity": "20-Sep-2017",
    "modi chem": "29-Oct-2025",
    "modi chemplast materials pvt ltd": "29-Oct-2025",
}

