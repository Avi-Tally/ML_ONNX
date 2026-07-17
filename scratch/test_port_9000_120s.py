import requests

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

url = "http://localhost:9000"
try:
    print("Pinging Port 9000 with 120s timeout...")
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=120)
    print("Port 9000 Status Code:", response.status_code)
    print("Response text:")
    print(response.text)
except Exception as e:
    print(f"Port 9000 error: {e}")
