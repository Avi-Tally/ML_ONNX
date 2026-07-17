import xml.etree.ElementTree as ET
import re

file_path = "raw_xml_dumps/tally_ui_export_new.xml"
with open(file_path, "r", encoding="utf-16") as f:
    content = f.read()

dates = re.findall(r'<BILLDATE>(.*?)</BILLDATE>', content)
print(f"Total bill dates in XML: {len(dates)}")
from datetime import datetime
parsed_dates = []
for d in dates:
    try:
        parsed_dates.append(datetime.strptime(d.strip(), "%d-%b-%y"))
    except Exception as e:
        pass
if parsed_dates:
    print(f"Latest bill date in XML: {max(parsed_dates).strftime('%Y-%m-%d')}")
    print(f"Earliest bill date in XML: {min(parsed_dates).strftime('%Y-%m-%d')}")
