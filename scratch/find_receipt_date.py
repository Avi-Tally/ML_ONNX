with open("raw_xml_dumps/tally_ui_export_new.xml", "r", encoding="utf-16") as f:
    content = f.read()

# Let's search for 368 in the XML content
import re
matches = [m.start() for m in re.finditer("368", content)]
print(f"Found {len(matches)} occurrences of 368:")
for idx, pos in enumerate(matches):
    start = max(0, pos - 100)
    end = min(len(content), pos + 100)
    snippet = content[start:end].replace("\n", " ")
    print(f"Match {idx+1}: ... {snippet} ...")
