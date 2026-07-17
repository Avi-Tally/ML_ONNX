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
        print(f"Col {col_id} status: {response.status_code}")
        print("Response text start:")
        print(response.text[:500])
    except Exception as e:
        print(f"Error for {col_id}: {e}")

test_col("BillsPayable")
test_col("Bills Payable")
test_col("BillsPayableReport")
