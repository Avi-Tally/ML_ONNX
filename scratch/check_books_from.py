import requests
import xml.etree.ElementTree as ET

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9001

payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>DebugCompany</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="DebugCompany">
                        <TYPE>Company</TYPE>
                        <FETCH>Name, BooksFrom, StartingFrom</FETCH>
                        <FILTERS>TargetFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetFilter">
                        $Name = "{company_name}"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=10)
    root = ET.fromstring(response.text)
    companies = root.findall(".//COMPANY")
    print(f"Total matching companies: {len(companies)}")
    for c in companies:
        name = c.findtext("NAME")
        bf = c.findtext("BOOKSFROM")
        sf = c.findtext("STARTINGFROM")
        print(f"Company: {name} | BooksFrom: {bf} | StartingFrom: {sf}")
except Exception as e:
    print(f"Error: {e}")
