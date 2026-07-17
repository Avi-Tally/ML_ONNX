import os
import re

data_dir = r"C:\Users\Public\TallyPrime\data"
folders = ["987651", "999999"]
for f in folders:
    file_path = os.path.join(data_dir, f, "Company.1800")
    if os.path.exists(file_path):
        try:
            with open(file_path, "rb") as file:
                data = file.read()
            # Try to decode as utf-16-le ignoring errors
            decoded = data.decode("utf-16-le", errors="ignore")
            # Replace non-printable characters
            clean = "".join(c if (c.isalnum() or c in " .,&()-") else " " for c in decoded)
            words = [w.strip() for w in clean.split() if len(w.strip()) > 3]
            
            clean_words = []
            for w in words:
                cleaned = re.sub(r'[^a-zA-Z0-9\-\.\,\&\(\)\_]', '', w)
                if len(cleaned) > 3:
                    clean_words.append(cleaned)
            
            matches = [w for w in clean_words if any(x in w.lower() for x in ["modi", "chemplast", "bella", "casa"])]
            print(f"\n--- Folder {f} ---")
            print("Matches:", set(matches))
            print("Sample text:", " ".join(clean_words[:30]))
        except Exception as e:
            print(f"Error reading folder {f}: {e}")
