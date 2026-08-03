import requests, time
xml = """<ENVELOPE><HEADER><VERSION>1</VERSION><TALLYREQUEST>Export</TALLYREQUEST><TYPE>Collection</TYPE><ID>C</ID></HEADER><BODY><DESC><STATICVARIABLES><SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT></STATICVARIABLES><TDL><TDLMESSAGE><COLLECTION NAME="C"><TYPE>Company</TYPE><FETCH>Name</FETCH></COLLECTION></TDLMESSAGE></TDL></DESC></BODY></ENVELOPE>"""
t0 = time.time()
try:
    r = requests.post('http://localhost:9000', data=xml, timeout=3)
    print(f"OK in {time.time()-t0:.2f}s: {r.text[:300]}")
except Exception as e:
    print(f"FAILED in {time.time()-t0:.2f}s: {e}")
