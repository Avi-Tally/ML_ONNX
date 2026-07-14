from rapidfuzz import fuzz

test_cases = [
    ("chem", "Darshan Chem"),
    ("in chem", "Akshar Plast Chem Investment Pvt Ltd")
]

for q, l in test_cases:
    w = fuzz.WRatio(q, l.lower())
    print(f"WRatio('{q}', '{l}'): {w}")
