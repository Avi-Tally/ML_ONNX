import requests

payload = """<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>AllCompanies</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="AllCompanies">
                        <TYPE>Company</TYPE>
                        <FETCH>*</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = "http://localhost:9001"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=5)
    print("Raw XML response:")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
