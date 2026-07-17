with open("scratch/abhay_vouchers.xml", "r", encoding="utf-8") as f:
    lines = f.readlines()

matching_lines = []
for i, line in enumerate(lines):
    if "abhay" in line.lower():
        matching_lines.append((i+1, line.strip()))

print(f"Total matching lines in XML: {len(matching_lines)}")
for ln, text in matching_lines[:20]:
    print(f"Line {ln}: {text}")
