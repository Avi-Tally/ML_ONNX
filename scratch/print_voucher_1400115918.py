with open("scratch/abhay_vouchers.xml", "r", encoding="utf-8") as f:
    lines = f.readlines()

start = 382390
end = 382800
for idx in range(start, min(end, len(lines))):
    print(f"Line {idx+1}: {lines[idx].strip()}")
