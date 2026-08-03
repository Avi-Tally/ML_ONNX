import requests, time

xml='''<ENVELOPE>
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
                <SVCURRENTCOMPANY>Bella Casa Data for User Activity</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="CustomBillCollection">
                        <TYPE>Bill</TYPE>
                        <FETCH>Name, BillDate, BillDueDate, BillCreditPeriod, ClosingBalance, OpeningBalance, Parent, ClearedOn</FETCH>
                        <FILTERS>OutstandingFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="OutstandingFilter">
                        $ClosingBalance != 0
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>'''

t0 = time.time()
r = requests.post('http://localhost:9000', data=xml, headers={'Content-Type': 'text/xml'})
print(f"Without COMPUTE: {time.time()-t0:.2f}s, size: {len(r.text)}")
