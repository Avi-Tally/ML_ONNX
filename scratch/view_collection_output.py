import requests

company_name = "Modi Chemplast Materials Pvt Ltd"
port = 9000

def test_col(col_id):
    payload = f"""<ENVELOPE>
    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>Export</TALLYREQUEST>
        <TYPE>Collection</TYPE>
        <ID>{col_id}</ID>
    </HEADER>
    <BODY>
        <DESC>
            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
                <SVCURRENTCOMPANY>{company_name}</SVCURRENTCOMPANY>
                <SVCURRENTDATE>20251129</SVCURRENTDATE>
            </STATICVARIABLES>
        </DESC>
    </BODY>
</ENVELOPE>"""

    url = f"http://localhost:{port}"
    try:
        response = requests.post(url, data=payload, headers={'Content-Type': 'text/xml'}, timeout=10)
        # Find <DATA> tag and print it
        start_idx = response.text.find("<DATA>")
        end_idx = response.text.find("</DATA>")
        if start_idx != -1 and end_idx != -1:
            print(f"Col {col_id} <DATA> tag content:")
            print(response.text[start_idx:end_idx+7])
        else:
            print(f"Col {col_id} did not have <DATA> tags, full response:")
            print(response.text)
    except Exception as e:
        print(f"Error for {col_id}: {e}")

test_col("BillsPayable")
test_col("Bills Payable")
