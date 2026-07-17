import requests
import xml.etree.ElementTree as ET

ports = [9000, 9001]
payload = """<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>CompanyList</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="CompanyList">
                        <TYPE>Company</TYPE>
                        <FETCH>Name, IsActive</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

for port in ports:
    url = f"http://localhost:{port}"
    try:
        res = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=5)
        root = ET.fromstring(res.text)
        companies = root.findall(".//COMPANY")
        print(f"Port {port} active companies:")
        for c in companies:
            name = c.findtext("NAME") or c.attrib.get("NAME", "")
            is_active = c.findtext("ISACTIVE") or ""
            print(f"  - {name} (Active: {is_active})")
    except Exception as e:
        print(f"Port {port} failed: {e}")
