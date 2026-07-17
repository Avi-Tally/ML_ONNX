import xml.etree.ElementTree as ET

file_path = "raw_xml_dumps/tally_ui_export_new.xml"
with open(file_path, "r", encoding="utf-16") as f:
    content = f.read()

# Let's search for the raw XML segment of the bill MODI/25-26/231
import re
# We look for <BILLFIXED> followed by everything up to the next </BILLFIXED> or end of XML
matches = re.findall(r'(<BILLFIXED>.*?</BILLFIXED>.*?)(?=<BILLFIXED>|$)', content, re.DOTALL)
print(f"Total XML blocks found: {len(matches)}")
target_refs = ["MODI/25-26/231", "MODI/25-26/440", "MODI/25-26/439", "MODI/25-26/438", "MODI/25-26/426"]
for m in matches:
    for ref in target_refs:
        if ref in m:
            print(f"\n--- Found block for {ref} ---")
            print(m.strip())
