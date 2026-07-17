import requests
import re

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

# Query Tally for license and product info
payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>DebugLicense</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="DebugLicense">
                        <TYPE>Company</TYPE>
                        <FILTER>IsCurrentCompany</FILTER>
                        <FETCH>Name</FETCH>
                        <COMPUTE>IsEducational: $$IsEducationalMode</COMPUTE>
                        <COMPUTE>LicenseSerial: $$LicenseSerial</COMPUTE>
                        <COMPUTE>ProductInfo: $$ProductInfo</COMPUTE>
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
