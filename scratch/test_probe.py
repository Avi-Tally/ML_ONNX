import requests
import xml.etree.ElementTree as ET

url = "http://localhost:9000"
payload = """<ENVELOPE>
    <HEADER><TALLYREQUEST>Export Data</TALLYREQUEST></HEADER>
    <BODY>
        <EXPORTDATA>
            <REQUESTDESC>
                <REPORTNAME>List of Accounts</REPORTNAME>
                <STATICVARIABLES>
                    <SVEXPLICITSTATIONARY>No</SVEXPLICITSTATIONARY>
                    <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                    <ACCOUNTTYPE>Companies</ACCOUNTTYPE>
                </STATICVARIABLES>
            </REQUESTDESC>
        </EXPORTDATA>
    </BODY>
</ENVELOPE>"""

res = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=3.0)
print("Status code:", res.status_code)
print("Response preview:")
print(res.text[:500])
