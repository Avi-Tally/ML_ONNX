import requests
import xml.etree.ElementTree as ET

payload = """<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>ActiveCompany</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="ActiveCompany">
                        <TYPE>Company</TYPE>
                        <FETCH>Name, IsSelected</FETCH>
                        <FILTERS>ActiveOnly</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="ActiveOnly">
                        $IsSelected = Yes
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = "http://localhost:9000"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=5)
    root = ET.fromstring(response.text)
    companies = root.findall(".//COMPANY")
    print(f"Active companies on Port 9000: {[c.findtext('NAME') for c in companies]}")
except Exception as e:
    print(f"Error: {e}")
