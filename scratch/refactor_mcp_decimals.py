import re

with open('mcp_server.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Decimal import if missing
if 'from decimal import Decimal' not in content:
    content = content.replace('import asyncio\n', 'import asyncio\nfrom decimal import Decimal, InvalidOperation\n')

# Replace the specific float usages. We'll use regex for robustness.
content = re.sub(r'return float\(str\(b\.get\(\'amount\', 0\)\)\.replace\(\',\', \'\'\)\.lstrip\(\'₹\'\)\.strip\(\)\)', 
                 r\"return Decimal(str(b.get('amount', 0)).replace(',', '').lstrip('₹').strip() or '0')\", content)

content = re.sub(r'bal_val = float\(bal_str\)', 
                 r'bal_val = Decimal(bal_str)', content)

content = re.sub(r'b\[\'abs_amount\'\] = abs\(float\(b\.get\(\'amount\', \'0\'\)\)\)', 
                 r\"b['abs_amount'] = abs(Decimal(str(b.get('amount', '0')).replace(',', '') or '0'))\", content)

content = re.sub(r'raw_amt = float\(b\.get\(\"amount\", \"0\"\)\)', 
                 r'raw_amt = Decimal(str(b.get(\"amount\", \"0\")).replace(\",\", \"\") or \"0\")', content)

content = re.sub(r'raw_amt = float\(b\.get\(\'amount\', 0\)\)', 
                 r\"raw_amt = Decimal(str(b.get('amount', '0')).replace(',', '') or '0')\", content)

content = re.sub(r'o_val = abs\(float\(b\.get\(\"opening_amount\", 0\) or 0\.0\)\)', 
                 r'o_val = abs(Decimal(str(b.get(\"opening_amount\", 0) or \"0\").replace(\",\", \"\")))', content)

content = re.sub(r'p_val = abs\(float\(b\.get\(\"amount\", 0\) or 0\.0\)\)', 
                 r'p_val = abs(Decimal(str(b.get(\"amount\", 0) or \"0\").replace(\",\", \"\")))', content)

with open('mcp_server.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished!")
