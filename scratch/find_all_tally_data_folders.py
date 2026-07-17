import os

# We search for "Company.900" starting from common directories
search_dirs = [
    r"C:\Users",
    r"C:\Program Files",
    r"C:\TallyPrime",
    r"C:\Tally",
]

found_folders = []
for sd in search_dirs:
    if os.path.exists(sd):
        print(f"Searching in {sd}...")
        for root, dirs, files in os.walk(sd):
            if "Company.900" in files:
                found_folders.append(root)

print(f"\nFound {len(found_folders)} Tally company data folders:")
for f in sorted(found_folders):
    # Get last modified time of files in this folder
    mtimes = [os.path.getmtime(os.path.join(f, name)) for name in os.listdir(f)]
    latest_time = max(mtimes) if mtimes else 0
    import datetime
    dt = datetime.datetime.fromtimestamp(latest_time)
    print(f"  - Path: {f} | Last Modified: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
