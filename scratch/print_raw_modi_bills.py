import requests

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9001

payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>DebugBills</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
                <SVCURRENTDATE>20251129</SVCURRENTDATE>
                <SVEXCLUDEPOSTDATED>Yes</SVEXCLUDEPOSTDATED>
                <SVEXCLUDEOPTIONAL>Yes</SVEXCLUDEOPTIONAL>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="DebugBills">
                        <TYPE>Bill</TYPE>
                        <FETCH>Name, ClosingBalance, Parent, IsBillWiseOn</FETCH>
                        <COMPUTE>IsBillWiseOn: $IsBillWiseOn:Ledger:$Parent</COMPUTE>
                        <FILTERS>TargetFilter</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetFilter">
                        $Parent = "Thermax Ltd" OR $Parent = "Abhay Limited"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

url = f"http://localhost:{port}"
try:
    response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=20)
    print("Raw XML response:")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
