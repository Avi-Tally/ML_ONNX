import requests
import xml.etree.ElementTree as ET

def get_ledger_balance(company_name, port, ledger_name, date_str, exclude_pdc, exclude_opt):
    pdc_val = "Yes" if exclude_pdc else "No"
    opt_val = "Yes" if exclude_opt else "No"
    
    payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>LedgerBal</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
                <SVCURRENTDATE>{date_str}</SVCURRENTDATE>
                <SVEXCLUDEPOSTDATED>{pdc_val}</SVEXCLUDEPOSTDATED>
                <SVEXCLUDEOPTIONAL>{opt_val}</SVEXCLUDEOPTIONAL>
            </STATICVARIABLES>
            <TDL>
                <TDLMESSAGE>
                    <COLLECTION NAME="LedgerBal">
                        <TYPE>Ledger</TYPE>
                        <FETCH>Name, ClosingBalance</FETCH>
                        <FILTERS>TargetLedger</FILTERS>
                    </COLLECTION>
                    <SYSTEM TYPE="Formulae" NAME="TargetLedger">
                        $Name = "{ledger_name}"
                    </SYSTEM>
                </TDLMESSAGE>
            </TDL>
        </DESC>
    </BODY>
</ENVELOPE>"""

    url = f"http://localhost:{port}"
    try:
        response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=10)
        print("Raw Response:")
        print(response.text)
        return "Printed"
    except Exception as e:
        return f"Error: {e}"

company = "Modi Chemplast Materials Pvt Ltd"
port = 9000
ledger = "Thermax Ltd"
date = "20251129"

print(f"Querying Closing Balance for '{ledger}' on {date}:")
print(f"  Exclude PDC: False | Exclude Opt: False -> Bal: {get_ledger_balance(company, port, ledger, date, False, False)}")
print(f"  Exclude PDC: True  | Exclude Opt: False -> Bal: {get_ledger_balance(company, port, ledger, date, True, False)}")
print(f"  Exclude PDC: False | Exclude Opt: True  -> Bal: {get_ledger_balance(company, port, ledger, date, False, True)}")
print(f"  Exclude PDC: True  | Exclude Opt: True  -> Bal: {get_ledger_balance(company, port, ledger, date, True, True)}")
