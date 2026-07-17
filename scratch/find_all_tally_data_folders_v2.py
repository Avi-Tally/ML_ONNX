import os
import datetime

drives = [r"C:\\", r"D:\\", r"E:\\"]
found_folders = []

print("Searching for Company.1800 on C: and E: drives...")
for drive in drives:
    if os.path.exists(drive):
        # We walk, but limit depth or skip heavy system folders to avoid infinite hanging
        for root, dirs, files in os.walk(drive):
            # Skip heavy windows/system folders
            if any(p in root.lower() for p in ["\\windows", "\\syswow64", "\\system32", "\\$recycle.bin", "\\microsoft"]):
                # Clear dirs to prevent descending
                dirs[:] = []
                continue
            if "Company.1800" in files:
                found_folders.append(root)

print(f"\nFound {len(found_folders)} Tally company data folders:")
for f in sorted(found_folders):
    try:
        mtimes = [os.path.getmtime(os.path.join(f, name)) for name in os.listdir(f)]
        latest_time = max(mtimes) if mtimes else 0
        dt = datetime.datetime.fromtimestamp(latest_time)
        print(f"  - Path: {f} | Last Modified: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"  - Path: {f} | Error: {e}")
