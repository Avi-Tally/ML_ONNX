import os

data_dir = r"C:\Users\Public\TallyPrime\data"
if os.path.exists(data_dir):
    print(f"Contents of {data_dir}:")
    for item in os.listdir(data_dir):
        path = os.path.join(data_dir, item)
        is_dir = os.path.isdir(path)
        if is_dir:
            # Print files inside
            print(f"  [DIR] {item} | Contents: {os.listdir(path)}")
        else:
            print(f"  [FILE] {item}")
else:
    print(f"Path does not exist: {data_dir}")
