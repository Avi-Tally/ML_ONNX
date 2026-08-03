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
                        <FETCH>Name</FETCH>
                        <SORT>@@Default: $BillDate</SORT>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>'''
t0=time.time()
r=requests.post('http://localhost:9000', data=xml, stream=True)
count = 0
for line in r.iter_lines():
    if b"<NAME>" in line:
        count += 1
        if count >= 10:
            break
print(f"Time for top 10: {time.time()-t0:.2f}s")
