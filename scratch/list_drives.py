import string
import os

drives = []
for letter in string.ascii_uppercase:
    drive = f"{letter}:\\"
    if os.path.exists(drive):
        drives.append(drive)
print("Available drives on the system:", drives)
