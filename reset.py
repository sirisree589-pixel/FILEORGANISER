import os
import shutil

folders = ["Images", "Documents", "Music", "Videos", "Others"]

for folder in folders:
    if os.path.exists(folder):
        for f in os.listdir(folder):
            shutil.move(os.path.join(folder, f), f)

print("DONE Reset*All files restored.")