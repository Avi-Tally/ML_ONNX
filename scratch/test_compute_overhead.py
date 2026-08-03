import requests, time

# Test 1: With COMPUTE tags (current)
xml_with_compute = '''<ENVELOPE>
<HEADER><VERSION>1</VERSION><TALLYREQUEST>Export</TALLYREQUEST><TYPE>Collection</TYPE><ID>CustomBillCollection</ID></HEADER>
<BODY><DESC>
<STATICVARIABLES><SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT><SVCURRENTCOMPANY>Bella Casa Data for User Activity</SVCURRENTCOMPANY></STATICVARIABLES>
<TDL><TDLMESSAGE>
<COLLECTION NAME="CustomBillCollection">
    <TYPE>Bill</TYPE>
    <FETCH>Name, BillDate, BillDueDate, BillCreditPeriod, ClosingBalance, OpeningBalance, Parent, ClearedOn, IsBillWiseOn</FETCH>
    <COMPUTE>PartyGSTIN: $Partygstin:Ledger:$Parent</COMPUTE>
    <COMPUTE>GSTRegType: $GSTRegistrationType:Ledger:$Parent</COMPUTE>
    <COMPUTE>ParentGroup: $Parent:Ledger:$Parent</COMPUTE>
    <COMPUTE>IsBillWiseOn: $IsBillWiseOn:Ledger:$Parent</COMPUTE>
    <FILTERS>ParentFilter</FILTERS>
</COLLECTION>
<SYSTEM TYPE="Formulae" NAME="ParentFilter">$Parent = "EXCEL ENTERPRISES"</SYSTEM>
</TDLMESSAGE></TDL>
</DESC></BODY></ENVELOPE>'''

# Test 2: Without COMPUTE tags (minimal)
xml_no_compute = '''<ENVELOPE>
<HEADER><VERSION>1</VERSION><TALLYREQUEST>Export</TALLYREQUEST><TYPE>Collection</TYPE><ID>CustomBillCollection</ID></HEADER>
<BODY><DESC>
<STATICVARIABLES><SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT><SVCURRENTCOMPANY>Bella Casa Data for User Activity</SVCURRENTCOMPANY></STATICVARIABLES>
<TDL><TDLMESSAGE>
<COLLECTION NAME="CustomBillCollection">
    <TYPE>Bill</TYPE>
    <FETCH>Name, BillDate, BillDueDate, BillCreditPeriod, ClosingBalance, OpeningBalance, Parent, ClearedOn</FETCH>
    <FILTERS>ParentFilter</FILTERS>
</COLLECTION>
<SYSTEM TYPE="Formulae" NAME="ParentFilter">$Parent = "EXCEL ENTERPRISES"</SYSTEM>
</TDLMESSAGE></TDL>
</DESC></BODY></ENVELOPE>'''

t0 = time.time()
r1 = requests.post('http://localhost:9000', data=xml_with_compute)
print(f"WITH COMPUTE: {time.time()-t0:.2f}s, size: {len(r1.text)}")

t0 = time.time()
r2 = requests.post('http://localhost:9000', data=xml_no_compute)
print(f"NO COMPUTE:   {time.time()-t0:.2f}s, size: {len(r2.text)}")
