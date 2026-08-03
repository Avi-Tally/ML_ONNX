import sys
sys.path.append('.')
from tally_client import TallyClient
client = TallyClient()
xml = """<ENVELOPE>
<HEADER><VERSION>1</VERSION><TALLYREQUEST>Export</TALLYREQUEST>
<TYPE>Collection</TYPE><ID>LedgersList</ID></HEADER>
<BODY><DESC>
<STATICVARIABLES><SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT></STATICVARIABLES>
<TDL><TDLMESSAGE>
<COLLECTION NAME="LedgersList"><TYPE>Ledger</TYPE><FETCH>Name</FETCH></COLLECTION>
</TDLMESSAGE></TDL>
</DESC></BODY></ENVELOPE>"""
res = client.execute_xml_request(9000, xml)
print(res[:1500])
