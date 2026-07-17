import requests
import xml.etree.ElementTree as ET

def test_billwise():
    company_name = "Bella Casa Data for User Activity"
    port = 9001
    
    payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>LedgerBillWiseTest</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="LedgerBillWiseTest">
                        <TYPE>Ledger</TYPE>
                        <!-- Fetch Name and IsBillWiseOn -->
                        <FETCH>Name, IsBillWiseOn</FETCH>
                        <FILTERS>LimitFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="LimitFilter">
                        $$IsLedger AND ($Name = "Abhay Limited" OR $IsBillWiseOn = Yes OR $IsBillWiseOn = No)
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
        ledgers = root.findall(".//LEDGER")
        print(f"Total ledgers returned: {len(ledgers)}")
        for l in ledgers[:10]:
            name = l.findtext("NAME")
            bw = l.findtext("ISBILLWISEON")
            print(f"  Ledger: {name} | IsBillWiseOn: {bw}")
    except Exception as e:
        print(f"Error: {e}")

test_billwise()
