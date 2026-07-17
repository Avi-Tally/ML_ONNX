with open("raw_xml_dumps/tally_ui_export_new.xml", "r", encoding="utf-16") as f:
    content = f.read()

import re
# Look for any tags containing company name, or just print lines that contain "company"
matches = re.findall(r'<[^>]*company[^>]*>(.*?)</[^>]*>', content, re.I)
print("Company related tags in XML:", set(matches))
