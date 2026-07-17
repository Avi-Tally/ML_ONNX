import os
import datetime

file_path = "raw_xml_dumps/tally_ui_export_new.xml"
if os.path.exists(file_path):
    mtime = os.path.getmtime(file_path)
    dt = datetime.datetime.fromtimestamp(mtime)
    print(f"File: {file_path}")
    print(f"Size: {os.path.getsize(file_path)} bytes")
    print(f"Last Modified: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
else:
    print(f"File not found: {file_path}")
