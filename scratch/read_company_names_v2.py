import os
import re

data_dir = r"C:\Users\Public\TallyPrime\data"
folders = ["987651", "999999"]
for f in folders:
    file_path = os.path.join(data_dir, f, "Company.1800")
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            content = file.read()
            # Find all sequences of printable ASCII characters of length >= 10
            ascii_strings = re.findall(b"[ -~]{10,}", content)
            print(f"\n--- Folder {f} ---")
            for s in ascii_strings:
                try:
                    decoded = s.decode('ascii').strip()
                    # Filter out strings that look like garbage
                    if any(c.isalpha() for c in decoded) and len(decoded) > 15:
                        print(f"  {decoded}")
                except:
                    pass
