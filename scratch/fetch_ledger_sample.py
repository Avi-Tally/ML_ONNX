import requests, time
xml='''<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>CustomLedgerCollection</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>Bella Casa Data for User Activity</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="CustomLedgerCollection">
                        <TYPE>Ledger</TYPE>
                        <FETCH>Name, ClosingBalance, BillAllocations.*</FETCH>
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
r=requests.post('http://localhost:9000', data=xml)
with open('scratch/ledger_sample.xml', 'w') as f:
    f.write(r.text[:5000])
