import requests
import re

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Query Tally for SVDataPath or similar system variables
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>DebugDataPath</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="DebugDataPath">
                        <TYPE>Company</TYPE>
                        <FILTER>IsCurrentCompany</FILTER>
                        <FETCH>Name</FETCH>
                        <COMPUTE>DataPath: $$SysName:Path</COMPUTE>
                        <COMPUTE>CompanyFolder: $..Name</COMPUTE>
                    </COLLECTION>
                    <SYSTEMNAME NAME="IsCurrentCompany">$$IsCurrentCompany:$Name</SYSTEMNAME>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=20)
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
