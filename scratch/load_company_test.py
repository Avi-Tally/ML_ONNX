import requests
import xml.etree.ElementTree as ET

def test():
    # Let's query Tally for all available companies in the directory
    payload = """<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>AllCompaniesInDir</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="AllCompaniesInDir">
                        <TYPE>Company</TYPE>
                        <FETCH>Name, IsSelected</FETCH>
                    </COLLECTION>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""
    try:
        response = requests.post("http://localhost:9000", data=payload, headers={'Content-Type': 'text/xml'}, timeout=5)
        root = ET.fromstring(response.text)
        companies = root.findall(".//COMPANY")
        print(f"Total companies returned: {len(companies)}")
        for c in companies:
            name = c.findtext("NAME")
            sel = c.findtext("ISSELECTED")
            print(f"  Company: {name} | Loaded: {sel}")
    except Exception as e:
        print(f"Error: {e}")

test()
