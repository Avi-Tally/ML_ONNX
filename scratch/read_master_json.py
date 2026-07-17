import json
import codecs

file_path = r"C:\Users\Public\TallyPrime\data\Master.json"
try:
    with open(file_path, "r", encoding="utf-16") as f:
        content = f.read()
        print("File length:", len(content))
        # Search for any patterns matching company names or folder numbers
        import re
        company_names = re.findall(r'"(?:name|companyName|company_name)"\s*:\s*"(.*?)"', content, re.I)
        print("Found company names:", set(company_names))
        # Let's print first 1000 characters of the file
        print("First 1000 chars:", content[:1000])
except Exception as e:
    print(f"Error: {e}")
