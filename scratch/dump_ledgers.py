with open('mismatch_report.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('scratch/ledger_mismatches.txt', 'w', encoding='utf-8') as out:
    for i, line in enumerate(lines):
        if 'Ledger mismatch' in line:
            # The query is usually a few lines up
            query_line = ""
            for j in range(i, max(-1, i-5), -1):
                if lines[j].startswith("### Query:"):
                    query_line = lines[j].strip()
                    break
            out.write(f"{query_line}\n{line.strip()}\n\n")
