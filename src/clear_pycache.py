import os
import shutil

for root, dirs, files in os.walk('.'):
    for dir_name in dirs:
        if dir_name == '__pycache__':
            dir_path = os.path.join(root, dir_name)
            shutil.rmtree(dir_path)
            print(f"Removed: {dir_path}")