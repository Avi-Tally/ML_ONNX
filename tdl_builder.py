"""
Data-driven TDL (Tally Definition Language) XML Envelope Builder.
Constructs strictly compliant XML request envelopes for TallyPrime HTTP socket transport.
Conforms to the TDL Knowledge Graph and TallyPrime XML socket protocol specification.
"""

import html
from typing import List, Dict, Optional, Tuple, Any, Union
import constants
import date_utils


class TDLEnvelopeBuilder:
    """
    Fluent builder for TallyPrime XML request envelopes.
    
    Supports:
      1. Collection Requests: Dynamic TDL collections with custom TYPE, FETCH, FILTER,
         COMPUTE, CHILDOF, and SYSTEM formulae.
      2. Data Requests: Native Tally C++ internal reports (e.g. 'Group Summary',
         'Trial Balance', 'Cost Centre Breakup', 'Godown Summary', 'Company').
    """

    def __init__(self):
        self._request_type: str = "Collection"  # "Collection", "Data", or "Object"
        self._report_id: Optional[str] = None   # Target report ID when _request_type == "Data"
        self._object_name: Optional[str] = None # Target object ID when _request_type == "Object"
        self._company: Optional[str] = None     # Company name
        self._collection_name: str = "DynamicCollection"
        self._collection_type: Optional[str] = None # "Ledger", "Bill", "Voucher", "StockItem", etc.
        self._fetch_fields: List[str] = []
        self._filters: Dict[str, str] = {}     # {FilterName: FormulaExpression}
        self._computes: Dict[str, str] = {}    # {FieldName: ComputeExpression}
        self._child_of: Optional[str] = None
        self._belongs_to: bool = False
        self._sort_field: Optional[str] = None
        self._max_limit: Optional[int] = None
        self._is_initialise: bool = True       # Enforce ISINITIALISE="Yes" for memory pop
        self._static_vars: Dict[str, str] = {
            "SVEXPORTFORMAT": constants.TDL_EXPORT_FORMAT
        }

    # =========================================================================
    # Request & Target Configuration
    # =========================================================================

    def set_is_initialise(self, is_init: bool = True) -> 'TDLEnvelopeBuilder':
        """Set whether ISINITIALISE='Yes' attribute should be added to the collection."""
        self._is_initialise = is_init
        return self

    def set_max_limit(self, limit: Optional[int]) -> 'TDLEnvelopeBuilder':
        """Set collection MAX result limit (e.g. 200)."""
        self._max_limit = limit
        return self



    def set_request_type(self, req_type: str) -> 'TDLEnvelopeBuilder':
        """Set request type: 'Collection', 'Data', or 'Object'."""
        r = req_type.lower()
        if r == "data":
            self._request_type = "Data"
        elif r == "object":
            self._request_type = "Object"
        else:
            self._request_type = "Collection"
        return self

    def set_object(self, object_name: str) -> 'TDLEnvelopeBuilder':
        """Configure single TDL Object request (e.g. 'AlterIDObj')."""
        self._object_name = object_name
        self._request_type = "Object"
        return self


    def set_report_id(self, report_id: str) -> 'TDLEnvelopeBuilder':
        """Set report ID for native Data requests (e.g. 'Group Summary', 'Trial Balance')."""
        self._report_id = report_id
        self._request_type = "Data"
        return self

    def set_company(self, company: Optional[str]) -> 'TDLEnvelopeBuilder':
        """Set target company name context."""
        self._company = company
        if company:
            self.set_static_var("SVCURRENTCOMPANY", company)
            if self._request_type == "Collection":
                self.set_static_var("SVCOMPANY", company)
        return self

    def set_collection(self, coll_type: str, coll_name: Optional[str] = None) -> 'TDLEnvelopeBuilder':
        """Configure TDL Collection type and identifier."""
        self._collection_type = coll_type
        if coll_name:
            self._collection_name = coll_name
        self._request_type = "Collection"
        return self

    # =========================================================================
    # Collection Projection, Filtration & Computations
    # =========================================================================

    def set_fetch(self, fields: Union[List[str], str]) -> 'TDLEnvelopeBuilder':
        """Set attributes/fields to fetch in the TDL collection."""
        if isinstance(fields, str):
            self._fetch_fields = [f.strip() for f in fields.split(",") if f.strip()]
        else:
            self._fetch_fields = [f.strip() for f in fields if f.strip()]
        return self

    def add_fetch(self, field: str) -> 'TDLEnvelopeBuilder':
        """Append a single field to the fetch projection."""
        if field and field not in self._fetch_fields:
            self._fetch_fields.append(field)
        return self

    def add_filter(self, name: str, formula: str) -> 'TDLEnvelopeBuilder':
        """Add a SYSTEM Formulae filter definition."""
        if name and formula:
            self._filters[name.strip()] = formula.strip()
        return self

    def add_compute(self, field_name: str, expression: str) -> 'TDLEnvelopeBuilder':
        """Add a dynamic computed method calculation."""
        if field_name and expression:
            self._computes[field_name.strip()] = expression.strip()
        return self

    def set_child_of(self, parent: str, belongs_to: bool = False) -> 'TDLEnvelopeBuilder':
        """Set CHILDOF parent scope and optional BELONGSTO flag."""
        self._child_of = parent
        self._belongs_to = belongs_to
        return self

    def set_sort(self, sort_expr: str) -> 'TDLEnvelopeBuilder':
        """Set sorting expression on collection (e.g. 'Default : -$Date')."""
        self._sort_field = sort_expr
        return self

    # =========================================================================
    # Static Variables & Parameter Scoping
    # =========================================================================

    def set_static_var(self, key: str, value: Any) -> 'TDLEnvelopeBuilder':
        """Inject or override an explicit STATICVARIABLE key."""
        if key and value is not None:
            self._static_vars[str(key).strip()] = str(value).strip()
        return self

    def set_date_range(self, from_date: Optional[str], to_date: Optional[str]) -> 'TDLEnvelopeBuilder':
        """
        Set SVFROMDATE and SVTODATE static variables.
        Accepts any date format (automatically normalized to YYYYMMDD).
        """
        if from_date:
            parsed_from = date_utils.parse_date(from_date)
            f_str = date_utils.to_tally_date(parsed_from) if parsed_from else from_date
            self.set_static_var("SVFROMDATE", f_str)
        if to_date:
            parsed_to = date_utils.parse_date(to_date)
            t_str = date_utils.to_tally_date(parsed_to) if parsed_to else to_date
            self.set_static_var("SVTODATE", t_str)
        return self

    def set_current_date(self, current_date: Optional[str]) -> 'TDLEnvelopeBuilder':
        """Set SVCURRENTDATE point-in-time reference date anchor."""
        if current_date:
            parsed_curr = date_utils.parse_date(current_date)
            c_str = date_utils.to_tally_date(parsed_curr) if parsed_curr else current_date
            self.set_static_var("SVCURRENTDATE", c_str)
        return self

    def set_group_name(self, group: str) -> 'TDLEnvelopeBuilder':
        """Set GROUPNAME static variable for Group Summary and outstandings reports."""
        return self.set_static_var("GROUPNAME", group)

    def set_godown_name(self, godown: str) -> 'TDLEnvelopeBuilder':
        """Set GODOWNNAME static variable for warehouse inventory drill-downs."""
        return self.set_static_var("GODOWNNAME", godown)

    def set_cost_centre_name(self, cc: str) -> 'TDLEnvelopeBuilder':
        """Set COSTCENTRENAME static variable for departmental expense drill-downs."""
        return self.set_static_var("COSTCENTRENAME", cc)

    def set_stock_group_name(self, sg: str) -> 'TDLEnvelopeBuilder':
        """Set STOCKGROUPNAME static variable for Stock Summary reports."""
        return self.set_static_var("STOCKGROUPNAME", sg)

    def set_ledger_name(self, ledger: str) -> 'TDLEnvelopeBuilder':
        """Set LEDGERNAME static variable for Ledger Monthly Summary reports."""
        return self.set_static_var("LEDGERNAME", ledger)

    def set_explode_flag(self, explode: bool = True) -> 'TDLEnvelopeBuilder':
        """Set EXPLODEFLAG='Yes' to expand hierarchical child groups."""
        return self.set_static_var("EXPLODEFLAG", "Yes" if explode else "No")

    def set_itemwise(self, itemwise: bool = True) -> 'TDLEnvelopeBuilder':
        """Set ISITEMWISE='Yes' to expand individual master ledgers or stock items."""
        return self.set_static_var("ISITEMWISE", "Yes" if itemwise else "No")

    def set_exclude_postdated(self, exclude: bool = True) -> 'TDLEnvelopeBuilder':
        """Set SVEXCLUDEPOSTDATED='Yes'."""
        return self.set_static_var("SVEXCLUDEPOSTDATED", "Yes" if exclude else "No")

    def set_exclude_optional(self, exclude: bool = True) -> 'TDLEnvelopeBuilder':
        """Set SVEXCLUDEOPTIONAL='Yes'."""
        return self.set_static_var("SVEXCLUDEOPTIONAL", "Yes" if exclude else "No")

    # =========================================================================
    # Core Assembly & XML Serialization
    # =========================================================================

    @staticmethod
    def escape_xml(text: str) -> str:
        """Escape XML entities (&, <, >, ", ')."""
        if not text:
            return ""
        return html.escape(str(text), quote=True)

    def build(self) -> str:
        """
        Assemble and serialize the complete XML envelope string.
        """
        if self._request_type == "Data":
            return self._build_data_envelope()
        elif self._request_type == "Object":
            return self._build_object_envelope()
        return self._build_collection_envelope()

    def _build_static_variables_xml(self, indent: str = "                ") -> str:
        """Format the <STATICVARIABLES> block."""
        lines = []
        for k, v in self._static_vars.items():
            escaped_val = self.escape_xml(v)
            # Retain system formula references without double-escaping $$SysName
            if v.startswith("$$SysName:"):
                escaped_val = v
            lines.append(f"{indent}<{k}>{escaped_val}</{k}>")
        return "\n".join(lines)

    def _build_object_envelope(self) -> str:
        """Construct single TDL Object XML request."""
        obj_name = self._object_name or "AlterIDObj"
        static_vars_xml = self._build_static_variables_xml("            ")
        computes = []
        for c_name, c_expr in self._computes.items():
            computes.append(f"                    <COMPUTE>{c_name}: {c_expr}</COMPUTE>")
        computes_xml = "\n".join(computes)

        return f"""<ENVELOPE>
    <HEADER><TALLYREQUEST>Export</TALLYREQUEST><TYPE>Data</TYPE><ID>AlterIDCheck</ID></HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
{static_vars_xml}
            </STATICVARIABLES>
            <TDL><TDLMESSAGE>
                <OBJECT NAME="{obj_name}">
{computes_xml}
                </OBJECT>
            </TDLMESSAGE></TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

    def _build_data_envelope(self) -> str:

        """Construct native C++ report XML request (<TYPE>Data</TYPE>)."""
        report_id = self._report_id or "Trial Balance"
        static_vars_xml = self._build_static_variables_xml("                ")
        
        return f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Data</TYPE>
        <ID>{report_id}</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
{static_vars_xml}
            </STATICVARIABLES>
        </DESC>
    </BODY>
</ENVELOPE>"""

    def _build_collection_envelope(self) -> str:
        """Construct dynamic TDL Collection XML request (<TYPE>Collection</TYPE>)."""
        coll_name = self._collection_name
        coll_type = self._collection_type or "Ledger"
        static_vars_xml = self._build_static_variables_xml("                ")

        # 1. Collection Attributes
        coll_tags = [f"                        <TYPE>{coll_type}</TYPE>"]
        
        if self._child_of:
            # Check if child_of is a TDL macro like $$VchTypeSales
            if self._child_of.startswith("$$"):
                coll_tags.append(f"                        <CHILDOF>{self._child_of}</CHILDOF>")
            else:
                escaped_child = self.escape_xml(self._child_of)
                coll_tags.append(f'                        <CHILDOF>"{escaped_child}"</CHILDOF>')
                
        if self._belongs_to:
            coll_tags.append("                        <BELONGSTO>Yes</BELONGSTO>")
            
        if self._fetch_fields:
            fetch_csv = ", ".join(self._fetch_fields)
            coll_tags.append(f"                        <FETCH>{fetch_csv}</FETCH>")
            
        if self._filters:
            filter_csv = ", ".join(self._filters.keys())
            coll_tags.append(f"                        <FILTER>{filter_csv}</FILTER>")
            
        for comp_name, comp_expr in self._computes.items():
            coll_tags.append(f"                        <COMPUTE>{comp_name}: {comp_expr}</COMPUTE>")
            
        if self._sort_field:
            coll_tags.append(f"                        <SORT>{self._sort_field}</SORT>")
            
        if self._max_limit:
            coll_tags.append(f"                        <MAX>{self._max_limit}</MAX>")

        coll_inner_xml = "\n".join(coll_tags)


        # 2. System Formulae Definitions
        formulae_tags = []
        for f_name, f_expr in self._filters.items():
            # Escape raw < and > in formula expressions if not already escaped
            if "&lt;" not in f_expr and "&gt;" not in f_expr:
                escaped_expr = f_expr.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            else:
                escaped_expr = f_expr
            formulae_tags.append(f"""                    <SYSTEM TYPE="Formulae" NAME="{f_name}">{escaped_expr}</SYSTEM>""")

        formulae_xml = ("\n" + "\n".join(formulae_tags)) if formulae_tags else ""

        init_attr = ' ISINITIALISE="Yes"' if self._is_initialise else ''

        return f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>{coll_name}</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
{static_vars_xml}
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="{coll_name}"{init_attr}>
{coll_inner_xml}
                    </COLLECTION>{formulae_xml}
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

    # =========================================================================
    # Factory Constructor from 28-Parameter NLP Envelope
    # =========================================================================

    @classmethod
    def from_params(cls, params: Dict[str, Any], company: str, intent: str) -> 'TDLEnvelopeBuilder':
        """
        Translates NLP parameters into a configured TDLEnvelopeBuilder instance.
        """
        builder = cls()
        builder.set_company(company)

        # 1. Date Scoping
        ref_date = params.get("reference_date")
        if ref_date:
            builder.set_current_date(ref_date)
            
        date_filter = params.get("date_filter")
        if date_filter:
            from_d, to_d = date_utils.resolve_date_range(params, {"current_date": ref_date})
            if from_d or to_d:
                builder.set_date_range(from_d, to_d)

        # 2. Intent-Specific Defaults
        if intent == "GET_TRIAL_BALANCE":
            builder.set_request_type("Data").set_report_id("Trial Balance")

        elif intent == "GET_STOCK_SUMMARY":
            builder.set_collection("StockItem", "CustomStockSummary")
            builder.set_fetch([
                "Name", "Parent", "Category", "BaseUnits", "ClosingBalance",
                "ClosingRate", "ClosingValue", "OpeningBalance", "OpeningRate",
                "OpeningValue", "StandardCost", "StandardPrice", "HSNCode"
            ])
            builder.add_filter("NonZeroBalance", "$ClosingBalance != 0")
            if params.get("stock_group"):
                builder.set_child_of(params["stock_group"], belongs_to=True)

        elif intent == "GET_RECENT_VOUCHERS":
            builder.set_collection("Vouchers:VoucherType", "VchCollection")
            builder.set_fetch([
                "Date", "VoucherTypeName", "VoucherNumber", "Reference",
                "PartyLedgerName", "Amount", "Narration"
            ])
            vt = params.get("voucher_type")
            if vt and vt.lower() in constants.VOUCHER_TYPE_MACROS:
                builder.set_child_of(constants.VOUCHER_TYPE_MACROS[vt.lower()], belongs_to=True)
            else:
                builder.set_child_of("$$VchTypeSales", belongs_to=True)

        elif intent in ["GET_RECEIVABLES", "GET_PAYABLES", "GET_BILL_DETAILS", "GET_AGEING"]:
            builder.set_collection("Bill", "CustomBillCollection")
            builder.set_fetch(["Name", "BillDate", "BillCreditPeriod", "ClosingBalance", "OpeningBalance", "Parent"])
            builder.add_compute("PartyGSTIN", "$Partygstin:Ledger:$Parent")
            builder.add_compute("ParentGroup", "$Parent:Ledger:$Parent")
            builder.set_exclude_postdated(True)
            builder.set_exclude_optional(True)

        return builder
