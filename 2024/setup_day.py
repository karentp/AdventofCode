import os
import shutil
import sys

def create_day_folder(day):
    folder_name = f"day_{day}"
    if os.path.exists(folder_name):
        print(f"Folder {folder_name} already exists!")
        return

    shutil.copytree("template", folder_name)
    print(f"Created folder {folder_name} with solution and test templates.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python setup_day.py <day_number>")
    else:
        day_number = sys.argv[1]
        create_day_folder(day_number)
