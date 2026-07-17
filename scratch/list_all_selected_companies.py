import requests
import xml.etree.ElementTree as ET

payload = """<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>SelectedCompanies</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
            </STATICVARIABLES>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = "http://localhost:9000"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=25)
    print("Response text:")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
