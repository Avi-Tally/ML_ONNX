import os

keyword = "till_today"
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    for idx, line in enumerate(f, 1):
                        if keyword in line:
                            print(f"{path}:{idx} -> {line.strip()}")
            except:
                pass
