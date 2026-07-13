import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

import xml.etree.ElementTree as ET

xml_file = "debug_bills_rec.xml"
if not os.path.exists(xml_file):
    xml_file = "bills_receivable.xml"
    
print(f"Reading from local file: {xml_file}")

context = ET.iterparse(xml_file, events=('end',))
parties = set()
for event, elem in context:
    if elem.tag == 'BILLFIXED':
        party = elem.findtext("BILLPARTY") or ""
        if party:
            parties.add(party)
        if len(parties) >= 20:
            break
        elem.clear()

print("Parties in XML:")
for p in sorted(list(parties)):
    print(f"  {p}")
