import requests
import time

PAYLOAD = """<ENVELOPE>
<HEADER><VERSION>1</VERSION><TALLYREQUEST>Export</TALLYREQUEST>
<TYPE>Collection</TYPE><ID>CompanyList</ID></HEADER>
<BODY><DESC>
<STATICVARIABLES><SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT></STATICVARIABLES>
<TDL><TDLMESSAGE>
<COLLECTION NAME="CompanyList"><TYPE>Company</TYPE><FETCH>Name</FETCH></COLLECTION>
</TDLMESSAGE></TDL>
</DESC></BODY></ENVELOPE>"""

t0 = time.perf_counter()
try:
    print("Pinging localhost:9000 with 35s timeout...")
    r = requests.post('http://localhost:9000', data=PAYLOAD,
                      headers={'Content-Type': 'text/xml'}, timeout=35.0)
    ms = (time.perf_counter() - t0) * 1000
    print(f'Port 9000: HTTP {r.status_code} | {ms:.0f}ms | {len(r.text)} bytes')
except Exception as e:
    ms = (time.perf_counter() - t0) * 1000
    print(f'Port 9000: FAILED ({ms:.0f}ms) - {e}')
