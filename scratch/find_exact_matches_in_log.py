import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('.'))

log_path = r"C:\Users\avija\.gemini\antigravity\brain\b17f1b4c-0c87-45b9-b9be-fe3b17f6d0d3\.system_generated\tasks\task-8875.log"

if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    print(f"Total lines in log: {len(lines)}")
    found = False
    for line in lines:
        if "4923295" in line or "4923296" in line or "4923294" in line:
            print(line.strip())
            found = True
    if not found:
        print("No exact match line found in the log.")
else:
    print("Log file not found!")
