# cleanup.py

import os
import shutil

# Directories to clear
CLEAN_DIRS = [
    "merged_output",
    "final_videos",
    "shorts"
]


def clean_dirs():
    for dir_path in CLEAN_DIRS:
        if os.path.exists(dir_path):
            for file in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"❌ Failed to delete {file_path}: {e}")
        else:
            print(f"Skipping missing directory: {dir_path}")


if __name__ == "__main__":
    print("🧹 Cleaning up project outputs...")
    clean_dirs()
    print("✅ Clean-up complete.")
