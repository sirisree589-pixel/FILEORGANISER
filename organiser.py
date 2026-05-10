import os
import shutil
import sys
source_folder = "."
skip_files = ["organiser.py", "reset.py"]
dry_run = "--dry-run" in sys.argv

if dry_run:
    print("DRY RUN MODE*no files to be moved\n")


folder_map = {
    "Images"    : [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents" : [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music"     : [".mp3", ".wav", ".aac"],
    "Videos"    : [".mp4", ".mov", ".avi", ".mkv"],
    "Others"    : []
}


print("Scanning folder..")
files = os.listdir(source_folder)
print(f"Found {len(files)} files:\n")


moved   = 0
skipped = 0

for file in files:

    if file in skip_files or os.path.isdir(file):
        continue

    
    parts = file.split(".")
    if len(parts) >= 3:
        ext = "." + parts[-2]
    else:
        ext = "." + parts[-1]
    ext = ext.lower()
    destination = "Others"
    for folder, extensions in folder_map.items():
        if ext in extensions:
            destination = folder
            break
    destination_path = os.path.join(destination, file)
    if os.path.exists(destination_path):
        print(f"DUPLICATE SKIPPED: {file} already exists in {destination}/")
        skipped += 1
        continue

    
    if dry_run:
        print(f"Would move: {file} → {destination}/")
    else:
        os.makedirs(destination, exist_ok=True)
        shutil.move(file, destination_path)
        print(f"Moved: {file} → {destination}/")
        moved += 1

print("\nSUMMARY")
if dry_run:
    print("Dry run complete — no files were moved.")
else:
    print(f"Files moved:   {moved}")
    print(f"Files skipped: {skipped}")
    print("Done! Files organised successfully!")