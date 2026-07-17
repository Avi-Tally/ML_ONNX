file_path = "raw_xml_dumps/tally_ui_export_new.xml"
with open(file_path, "r", encoding="utf-16") as f:
    # Read first 1000 characters
    content = f.read(1000)
print("Header of tally_ui_export_new.xml:")
print(content)
