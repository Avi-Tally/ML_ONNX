import os

data_dir = r"C:\Users\Public\TallyPrime\data"
folders = ["987651", "999999"]
for f in folders:
    file_path = os.path.join(data_dir, f, "Company.1800")
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            content = file.read(500)
            # Find any ascii strings in the content
            import re
            strings = re.findall(b"[A-Za-z0-9\s\-\.\,\&\(\)\_]{4,}", content)
            print(f"Folder {f} strings:")
            for s in strings:
                try:
                    decoded = s.decode('ascii').strip()
                    if len(decoded) > 5:
                        print(f"  - {decoded}")
                except:
                    pass
