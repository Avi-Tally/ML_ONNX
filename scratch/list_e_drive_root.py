import os

root_dir = r"E:\\"
try:
    items = os.listdir(root_dir)
    print(f"Items in {root_dir}:")
    for item in items:
        path = os.path.join(root_dir, item)
        is_dir = os.path.isdir(path)
        print(f"  {'[DIR]' if is_dir else '[FILE]'} {item}")
except Exception as e:
    print(f"Error: {e}")
