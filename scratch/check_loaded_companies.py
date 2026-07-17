import requests
import xml.etree.ElementTree as ET

def get_companies(port):
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
        </DESC>
    </BODY>
</ENVELOPE>"""
    try:
        response = requests.post(f"http://localhost:{port}", data=payload, headers={'Content-Type': 'text/xml'}, timeout=5)
        root = ET.fromstring(response.text)
        names = [c.findtext("NAME") for c in root.findall(".//COMPANY")]
        print(f"Port {port} loaded companies: {names}")
    except Exception as e:
        print(f"Port {port} error: {e}")

get_companies(9000)
get_companies(9001)
