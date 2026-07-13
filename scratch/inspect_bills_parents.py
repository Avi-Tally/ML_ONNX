import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET

xml_file = "debug_bills_rec.xml"
if not os.path.exists(xml_file):
    xml_file = "bills_receivable.xml"
    
print(f"Reading from local file: {xml_file}")

# We will use iterparse to be memory efficient since the file is large
context = ET.iterparse(xml_file, events=('end',))
count = 0
for event, elem in context:
    if elem.tag == 'BILL':
        party = elem.findtext("PARENT") or ""
        name = elem.findtext("NAME") or ""
        parent_group = elem.findtext("PARENTGROUP") or ""
        amt = elem.findtext("CLOSINGBALANCE") or "0"
        
        print(f"Bill Name: '{name}' | Party: '{party}' | Parent Group: '{parent_group}' | Amount: {amt}")
        count += 1
        if count >= 10:
            break
        elem.clear()
