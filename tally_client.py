import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

class TallyClient:
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

    def __init__(self, ports=[9000, 9001]):
        self.ports = ports
        self.routing_table = {}  # maps company_name.lower() -> port
        self.update_routing_table()

    def clean_xml(self, xml_str):
        """Strips out invalid XML control characters and entities (like &#4;)."""
        import re
        
        # Remove decimal entities
        def dec_repl(match):
            val = int(match.group(1))
            if val in [9, 10, 13] or (32 <= val <= 55295) or (57344 <= val <= 65533):
                return match.group(0)
            return ""
        
        # Remove hex entities
        def hex_repl(match):
            val = int(match.group(1), 16)
            if val in [9, 10, 13] or (32 <= val <= 55295) or (57344 <= val <= 65533):
                return match.group(0)
            return ""
            
        xml_str = re.sub(r'&#(\d+);', dec_repl, xml_str)
        xml_str = re.sub(r'&#x([0-9a-fA-F]+);', hex_repl, xml_str)
        
        # Remove raw control chars (except tab, LF, CR)
        cleaned = [c for c in xml_str if ord(c) in [9, 10, 13] or ord(c) >= 32]
        return "".join(cleaned)

    def update_routing_table(self):
        """Probes all configured ports concurrently and caches which companies are loaded on which ports."""
        new_routing = {}
        import concurrent.futures

        def probe_port(port):
            url = f"http://localhost:{port}"
            payload = """<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>List of Companies</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="List of Companies">
                        <TYPE>Company</TYPE>
                        <NATIVEMETHOD>Name</NATIVEMETHOD>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""
            try:
                response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=1)
                if response.status_code == 200:
                    cleaned_xml = self.clean_xml(response.text)
                    root = ET.fromstring(cleaned_xml)
                    found = {}
                    for company_elem in root.findall(".//COMPANY"):
                        name_elem = company_elem.find("NAME")
                        if name_elem is not None and name_elem.text:
                            company_name = name_elem.text.strip()
                            found[company_name.lower()] = {"name": company_name, "port": port}
                        elif company_elem.attrib.get("NAME"):
                            company_name = company_elem.attrib.get("NAME").strip()
                            found[company_name.lower()] = {"name": company_name, "port": port}
                    return found
            except requests.exceptions.RequestException:
                pass
            return {}

        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.ports)) as executor:
            results = list(executor.map(probe_port, self.ports))

        for res in results:
            new_routing.update(res)

        # Fetch context for the active companies (also concurrently to save more time)
        def fetch_ctx(k, v):
            context = self.fetch_company_context(v["name"], v["port"])
            v["context"] = context
            return k, v

        if new_routing:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(new_routing)) as executor:
                futures = [executor.submit(fetch_ctx, k, v) for k, v in new_routing.items()]
                for future in concurrent.futures.as_completed(futures):
                    k, v = future.result()
                    new_routing[k] = v

        self.routing_table = new_routing
        return self.routing_table

    def get_port_for_company(self, company_query=None):
        """
        Determines the correct port and full company name based on a query string.
        If company_query is None, returns the first active port and company.
        """
        if not self.routing_table:
            # Re-probe if empty
            self.update_routing_table()
            if not self.routing_table:
                raise ConnectionError("No running TallyPrime instances detected on configured ports.")

        if company_query:
            query = company_query.lower().strip()
            # 1. Exact match or substring match
            for k, info in self.routing_table.items():
                if query in k or k in query:
                    return info["port"], info["name"], info["context"]

        # Default fallback to first company in the routing table
        first_key = list(self.routing_table.keys())[0]
        first_info = self.routing_table[first_key]
        return first_info["port"], first_info["name"], first_info["context"]

    def execute_xml_request(self, port, payload):
        """Sends an XML request to TallyPrime and returns the response text."""
        url = f"http://localhost:{port}"
        try:
            response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=60)
            if response.status_code != 200:
                raise IOError(f"Tally HTTP server returned status code {response.status_code}")
            return self.clean_xml(response.text)
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to communicate with Tally on port {port}: {e}")

    def get_group_hierarchy_map(self, company, port):
        """Fetches all Groups from Tally on the specified port and builds a map of lowercase parent groups."""
        payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>GroupList</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="GroupList">
                        <TYPE>Group</TYPE>
                        <FETCH>Name, Parent</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""
        try:
            res = self.execute_xml_request(port, payload)
            root = ET.fromstring(res)
            groups = root.findall(".//GROUP")
            group_parents = {}
            for g in groups:
                name = g.findtext("NAME") or g.attrib.get("NAME", "")
                parent = g.findtext("PARENT") or ""
                if name:
                    group_parents[name.strip().lower()] = parent.strip().lower()
            return group_parents
        except Exception as e:
            print(f"Error fetching group hierarchy map from port {port}: {e}")
            return {}

    def is_group_under(self, group_name, target_parent, group_map):
        """Recursively checks if group_name is a subgroup of target_parent using group_map."""
        curr = group_name.strip().lower()
        target = target_parent.strip().lower()
        visited = set()
        while curr and curr not in visited:
            if curr == target:
                return True
            visited.add(curr)
            curr = group_map.get(curr)
        return False

    def fetch_company_context(self, company_name, port):
        """Fetches the current working date and period for the specified company."""
        payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>CompanyPeriodDetails</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="CompanyPeriodDetails">
                        <TYPE>Company</TYPE>
                        <FILTER>IsCurrentCompany</FILTER>
                        <FETCH>Name</FETCH>
                        <COMPUTE>CurrentDate: ##SVCurrentDate</COMPUTE>
                        <COMPUTE>FromDate: ##SVFromDate</COMPUTE>
                        <COMPUTE>ToDate: ##SVToDate</COMPUTE>
                    </COLLECTION>
                    <SYSTEMNAME NAME="IsCurrentCompany">$$IsCurrentCompany:$Name</SYSTEMNAME>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""
        try:
            response_xml = self.execute_xml_request(port, payload)
            root = ET.fromstring(response_xml)
            company_node = root.find(".//COLLECTION/COMPANY")
            if company_node is not None:
                def parse_date(node_name):
                    n = company_node.find(node_name)
                    if n is not None and n.text:
                        ds = n.text.strip()
                        if len(ds) == 8: # YYYYMMDD
                            import datetime
                            try:
                                return datetime.datetime.strptime(ds, "%Y%m%d").strftime("%d-%b-%Y")
                            except:
                                return ds
                        return ds
                    return "Unknown"
                
                return {
                    "current_date": parse_date("CURRENTDATE"),
                    "from_date": parse_date("FROMDATE"),
                    "to_date": parse_date("TODATE")
                }
        except Exception as e:
            print("ERROR IN fetch_company_context:", e)
            try:
                print("RESPONSE XML:", response_xml)
            except:
                pass
            
        # Fallback
        return {
            "current_date": "Unknown",
            "from_date": "Unknown",
            "to_date": "Unknown"
        }

    def fetch_ledgers(self, company_name, port):
        """Fetches all ledgers and their balances for a specific company and port."""
        payload_ledgers = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>LedgerListWithBalance</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="LedgerListWithBalance">
                        <TYPE>Ledger</TYPE>
                        <FETCH>Name, ClosingBalance</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

        payload_groups = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>GroupListWithBalance</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="GroupListWithBalance">
                        <TYPE>Group</TYPE>
                        <FETCH>Name, ClosingBalance</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""
        
        ledgers = {}
        
        # 1. Fetch Ledgers
        res_ledgers = self.execute_xml_request(port, payload_ledgers)
        root_ledgers = ET.fromstring(res_ledgers)
        for ledger_elem in root_ledgers.findall(".//LEDGER"):
            name = ledger_elem.findtext("NAME") or ledger_elem.attrib.get("NAME", "")
            if name:
                bal = ledger_elem.findtext("CLOSINGBALANCE") or "0.00"
                ledgers[name.strip()] = bal.strip()

        # 2. Fetch Groups
        res_groups = self.execute_xml_request(port, payload_groups)
        root_groups = ET.fromstring(res_groups)
        for group_elem in root_groups.findall(".//GROUP"):
            name = group_elem.findtext("NAME") or group_elem.attrib.get("NAME", "")
            if name:
                bal = group_elem.findtext("CLOSINGBALANCE") or "0.00"
                ledgers[name.strip()] = bal.strip()
                
        return ledgers

    def fetch_trial_balance(self, company_name, port):
        """Fetches the Trial Balance report."""
        payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Data</TYPE>
        <ID>Trial Balance</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
        </DESC>
    </BODY>
</ENVELOPE>"""
        response_xml = self.execute_xml_request(port, payload)
        root = ET.fromstring(response_xml)
        
        tb_data = []
        names = root.findall(".//DSPACCNAME")
        infos = root.findall(".//DSPACCINFO")
        for name_node, info_node in zip(names, infos):
            disp_name = name_node.find("DSPDISPNAME")
            if disp_name is not None and disp_name.text:
                name = disp_name.text.strip()
                
                dr_val = ""
                dr_amt_node = info_node.find(".//DSPCLDRAMTA")
                if dr_amt_node is not None and dr_amt_node.text:
                    dr_val = dr_amt_node.text.strip()
                    
                cr_val = ""
                cr_amt_node = info_node.find(".//DSPCLCRAMTA")
                if cr_amt_node is not None and cr_amt_node.text:
                    cr_val = cr_amt_node.text.strip()
                    
                balance = "0.00"
                drcr = ""
                if dr_val and dr_val != "0.00":
                    balance = dr_val
                    drcr = "Dr"
                elif cr_val and cr_val != "0.00":
                    balance = cr_val
                    drcr = "Cr"
                    
                tb_data.append({
                    "name": name,
                    "balance": balance,
                    "type": drcr
                })
        return tb_data

    def fetch_stock_summary(self, company_name, port):
        """Fetches the Stock Summary report."""
        payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Data</TYPE>
        <ID>Stock Summary</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
        </DESC>
    </BODY>
</ENVELOPE>"""
        response_xml = self.execute_xml_request(port, payload)
        root = ET.fromstring(response_xml)
        
        stock_data = []
        names = root.findall(".//DSPACCNAME")
        infos = root.findall(".//DSPSTKINFO")
        for name_node, info_node in zip(names, infos):
            disp_name = name_node.find("DSPDISPNAME")
            if disp_name is not None and disp_name.text:
                item_name = disp_name.text.strip()
                
                qty = ""
                qty_node = info_node.find(".//DSPCLQTY")
                if qty_node is not None and qty_node.text:
                    qty = qty_node.text.strip()
                    
                rate = ""
                rate_node = info_node.find(".//DSPCLRATE")
                if rate_node is not None and rate_node.text:
                    rate = rate_node.text.strip()
                    
                val = ""
                val_node = info_node.find(".//DSPCLAMTA")
                if val_node is not None and val_node.text:
                    val = val_node.text.strip()
                    
                stock_data.append({
                    "item": item_name,
                    "quantity": qty if qty else "0",
                    "rate": rate if rate else "0",
                    "value": val if val else "0"
                })
        return stock_data

    def fetch_recent_vouchers(self, company_name, port, from_date=None, to_date=None):
        """Fetches recent vouchers (transactions) from the Day Book."""
        sv_dates = ""
        if from_date: sv_dates += f"\n                <SVFROMDATE>{from_date}</SVFROMDATE>"
        if to_date: sv_dates += f"\n                <SVTODATE>{to_date}</SVTODATE>"
        
        payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Data</TYPE>
        <ID>Day Book</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>{sv_dates}
            </STATICVARIABLES>
        </DESC>
    </BODY>
</ENVELOPE>"""
        response_xml = self.execute_xml_request(port, payload)
        root = ET.fromstring(response_xml)
        
        vouchers = []
        for v in root.findall(".//VOUCHER"):
            v_type = v.findtext("VOUCHERTYPENAME")
            v_num = v.findtext("VOUCHERNUMBER")
            date_raw = v.findtext("DATE")
            party = v.findtext("PARTYLEDGERNAME")
            narration = v.findtext("NARRATION")
            
            # Format date: 20171008 -> 2017-10-08
            formatted_date = date_raw
            if date_raw and len(date_raw) == 8:
                formatted_date = f"{date_raw[:4]}-{date_raw[4:6]}-{date_raw[6:]}"
                
            # Extract ledger entries
            ledger_entries = []
            entries = v.findall(".//ALLLEDGERENTRIES.LIST") + v.findall(".//LEDGERENTRIES.LIST")
            total_amount = "0.00"
            for entry in entries:
                lname = entry.findtext("LEDGERNAME")
                amount = entry.findtext("AMOUNT")
                if lname or amount:
                    lname_clean = lname.strip() if lname else ""
                    amount_clean = amount.strip() if amount else "0.00"
                    ledger_entries.append({
                        "ledger": lname_clean,
                        "amount": amount_clean
                    })
                    # Use the party's ledger entry to determine the voucher net total
                    if party and lname_clean.lower() == party.lower():
                        total_amount = amount_clean.lstrip("-")
            
            vouchers.append({
                "date": formatted_date,
                "type": v_type if v_type else "Journal",
                "number": v_num if v_num else "N/A",
                "party": party if party else "N/A",
                "amount": total_amount if total_amount != "0.00" else (ledger_entries[0]["amount"].lstrip("-") if ledger_entries else "0.00"),
                "narration": narration if narration else "",
                "entries": ledger_entries
            })
            
        return vouchers

    def fetch_bills(self, company_name, port, report_type="All", from_date=None, to_date=None, status_filter=None, reference_date=None):
        """Fetches bills using a custom TDL collection and a streaming parser."""
        ref_date_formatted = None
        if reference_date:
            parsed_ref = self._parse_date(reference_date)
            if parsed_ref != datetime.min:
                ref_date_formatted = parsed_ref.strftime("%Y%m%d")

        group_map = self.get_group_hierarchy_map(company_name, port)
        filter_names = []
        filter_defs = []
        
        if from_date or to_date:
            f_date = from_date if from_date else "19000101"
            t_date = to_date if to_date else "20991231"
            filter_names.append("DateFilter")
            filter_defs.append(f"""<SYSTEM TYPE="Formulae" NAME="DateFilter">
                        $BillDate &gt;= $$Date:"{f_date}" AND $BillDate &lt;= $$Date:"{t_date}"
                    </SYSTEM>""")
                    
        if status_filter == "pending":
            filter_names.append("OutstandingFilter")
            filter_defs.append("""<SYSTEM TYPE="Formulae" NAME="OutstandingFilter">
                        $ClosingBalance != 0
                    </SYSTEM>""")
                    
        date_filter_tag = ""
        date_filter_def = ""
        if filter_names:
            date_filter_tag = f"<FILTERS>{', '.join(filter_names)}</FILTERS>"
            date_filter_def = "\n                    ".join(filter_defs)
         
        payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>CustomBillCollection</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
                {f'<SVCURRENTDATE>{ref_date_formatted}</SVCURRENTDATE>' if ref_date_formatted else ''}
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="CustomBillCollection">
                        <TYPE>Bill</TYPE>
                        <FETCH>Name, BillDate, BillCreditPeriod, ClosingBalance, OpeningBalance, Parent, ClearedOn</FETCH>
                        <COMPUTE>PartyGSTIN: $Partygstin:Ledger:$Parent</COMPUTE>
                        <COMPUTE>GSTRegType: $GSTRegistrationType:Ledger:$Parent</COMPUTE>
                        <COMPUTE>ParentGroup: $Parent:Ledger:$Parent</COMPUTE>
                        {date_filter_tag}
                    </COLLECTION>
                    {date_filter_def}
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""
        
        url = f"http://localhost:{port}"
        try:
            response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=120, stream=True)
            if response.status_code != 200:
                raise IOError(f"Tally HTTP server returned status code {response.status_code}")
                
            class SanitizedStream:
                def __init__(self, response):
                    self.iterator = response.iter_content(chunk_size=8192, decode_unicode=False)
                    self.byte_buffer = b""
                    import re
                    # Tally sometimes outputs naked & which breaks xml.etree
                    self.naked_amp_regex = re.compile(b'&(?!(amp|lt|gt|quot|apos|#);)')
                    self.entity_regex = re.compile(b'&#(\\d+);|&#x([0-9a-fA-F]+);')

                def read(self, size=-1):
                    while size > 0 and len(self.byte_buffer) < size:
                        try:
                            chunk = next(self.iterator)
                            self.byte_buffer += chunk
                        except StopIteration:
                            break
                            
                    if size > 0:
                        chunk_to_process = self.byte_buffer[:size]
                        self.byte_buffer = self.byte_buffer[size:]
                    else:
                        chunks = []
                        try:
                            while True:
                                chunks.append(next(self.iterator))
                        except StopIteration:
                            pass
                        chunk_to_process = b"".join(chunks)
                        self.byte_buffer = b""

                    if not chunk_to_process:
                        return b""
                        
                    # Sanitize
                    chunk_to_process = self.naked_amp_regex.sub(b'&amp;', chunk_to_process)
                    chunk_to_process = self.entity_regex.sub(b'', chunk_to_process)
                    return chunk_to_process
                        
                    return text.encode('utf-8')
                    
            stream = SanitizedStream(response)
            
            bills = []
            
            context = ET.iterparse(stream, events=('end',))
            for event, elem in context:
                if elem.tag == 'BILL':
                    name = elem.findtext("NAME") or ""
                    party = elem.findtext("PARENT") or ""
                    date = elem.findtext("BILLDATE") or ""
                    
                    due_date_elem = elem.find("BILLCREDITPERIOD")
                    due_date = date
                    if due_date_elem is not None:
                        if due_date_elem.text:
                            due_date = due_date_elem.text
                        elif due_date_elem.attrib.get("JD"):
                            try:
                                jd = int(due_date_elem.attrib.get("JD"))
                                base_date = datetime(1900, 1, 1)
                                dt = base_date + timedelta(days=jd - 1)
                                due_date = dt.strftime("%Y%m%d")
                            except:
                                due_date = date
                                
                    amt_elem = elem.find("CLOSINGBALANCE")
                    amt = amt_elem.text if amt_elem is not None else "0"
                    
                    open_elem = elem.find("OPENINGBALANCE")
                    open_amt = open_elem.text if open_elem is not None else "0"
                    
                    gstin = elem.findtext("PARTYGSTIN") or ""
                    gst_type = elem.findtext("GSTREGTYPE") or ""
                    parent_group = elem.findtext("PARENTGROUP") or ""
                    cleared_on = elem.findtext("CLEAREDON") or ""
                    
                    # Robustly parse and clean foreign currency/multicurrency amount strings (e.g. "? 36511.00 @ Rs 104.10/? = Rs 3800795.10")
                    amt_str = amt.strip()
                    if "=" in amt_str:
                        amt_str = amt_str.split("=")[-1].strip()
                    cleaned_amt = "".join(c for c in amt_str if c.isdigit() or c in [".", "-"])
                    try:
                        amt_float = float(cleaned_amt)
                    except:
                        amt_float = 0.0
                        
                    # Determine nature based on recursive parent group and keywords
                    pg_lower = parent_group.strip().lower()
                    party_lower = party.strip().lower()
                    
                    is_creditor = (
                        self.is_group_under(pg_lower, "sundry creditors", group_map) or
                        self.is_group_under(pg_lower, "trade payables", group_map) or
                        any(w in pg_lower for w in ["creditor", "payable", "supplier", "vendor"]) or
                        any(w in party_lower for w in ["creditor", "supplier", "vendor"])
                    )
                    is_debtor = (
                        self.is_group_under(pg_lower, "sundry debtors", group_map) or
                        self.is_group_under(pg_lower, "trade receivables", group_map) or
                        any(w in pg_lower for w in ["debtor", "receivable", "customer", "client", "sales"]) or
                        any(w in party_lower for w in ["debtor", "customer", "client"])
                    )
                    
                    is_payable = amt_float > 0
                    is_receivable = amt_float < 0
                            
                    # Filter based on report_type
                    if report_type == "Receivable" and not is_receivable:
                        elem.clear()
                        continue
                    elif report_type == "Payable" and not is_payable:
                        elem.clear()
                        continue
                        
                    # Pre-calculate normalized amounts using absolute values for outstanding totals
                    if is_payable:
                        normalized_pay_amt = abs(amt_float)
                        normalized_rec_amt = 0.0
                    else:
                        normalized_pay_amt = 0.0
                        normalized_rec_amt = abs(amt_float)
                        
                    bills.append({
                        "name": name,
                        "party": party,
                        "date": date,
                        "due_date": due_date,
                        "amount": amt.strip(),
                        "normalized_payables_amount": normalized_pay_amt,
                        "normalized_receivables_amount": normalized_rec_amt,
                        "opening_amount": open_amt.strip(),
                        "gstin": gstin.strip(),
                        "gst_type": gst_type.strip(),
                        "parent_group": parent_group.strip(),
                        "cleared_on": cleared_on.strip(),
                        "is_settled": (cleared_on.strip() != "" or amt_float == 0)
                    })
                    elem.clear()
                    
            return bills
        except Exception as e:
            print(f"Error streaming bills from Tally: {e}")
            return []
