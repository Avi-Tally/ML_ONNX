import os
import datetime

sd = r"E:\TallyPrime"
if not os.path.exists(sd):
    sd = r"E:\\"

found_folders = []
print(f"Searching for Company.900 in {sd}...")
for root, dirs, files in os.walk(sd):
    if "Company.900" in files:
        found_folders.append(root)

print(f"\nFound {len(found_folders)} Tally company data folders on E: drive:")
for f in sorted(found_folders):
    # Get last modified time of files in this folder
    try:
        mtimes = [os.path.getmtime(os.path.join(f, name)) for name in os.listdir(f)]
        latest_time = max(mtimes) if mtimes else 0
        dt = datetime.datetime.fromtimestamp(latest_time)
        print(f"  - Path: {f} | Last Modified: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"  - Path: {f} | Error: {e}")
