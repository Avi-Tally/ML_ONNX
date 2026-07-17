import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("raw_xml_dumps/tally_ui_export.xml", "r", encoding="utf-16") as f:
    for i in range(100):
        line = f.readline()
        if not line:
            break
        print(f"{i+1}: {line.strip()}")
