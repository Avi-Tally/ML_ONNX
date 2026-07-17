with open("scratch/abhay_vouchers.xml", "r", encoding="utf-8") as f:
    lines = f.readlines()

matching_lines = []
for i, line in enumerate(lines):
    if "1400115918" in line:
        matching_lines.append((i+1, line.strip()))

print(f"Total matching lines for bill 1400115918: {len(matching_lines)}")
for ln, text in matching_lines:
    print(f"Line {ln}: {text}")
