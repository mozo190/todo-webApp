import argparse
import os
from datetime import datetime, timedelta

DOWNLOADS_PATH = os.path.expanduser("~/Downloads")
FILE_AGE_LIMIT_DAYS = 30


def is_file_old(file_path, days):
    file_age_limit = datetime.now() - timedelta(days=days)
    file_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
    return file_modified < file_age_limit


def clean_downloads_folder(folder_path, days):
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist.")
        return

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if is_file_old(file_path, days):
                try:
                    os.remove(file_path)
                    print(f'Removed file: {file_path}')
                except Exception as e:
                    print(f'Error removing file: {file_path} - {e}')


def command_line_input():
    global DOWNLOADS_PATH, FILE_AGE_LIMIT_DAYS
    parser = argparse.ArgumentParser(description='Clean files older than N days in a folder.')
    parser.add_argument('--folder', default=DOWNLOADS_PATH, help='Folder path to clean')
    parser.add_argument('--days', type=int, default=FILE_AGE_LIMIT_DAYS, help='File age limit in days')
    args = parser.parse_args()
    DOWNLOADS_PATH = args.folder
    FILE_AGE_LIMIT_DAYS = args.days


if __name__ == "__main__":
    # Command line arguments
    command_line_input()

    print(f"Cleaning files older than {FILE_AGE_LIMIT_DAYS} days in {DOWNLOADS_PATH} is starting...")
    clean_downloads_folder(DOWNLOADS_PATH, FILE_AGE_LIMIT_DAYS)
    print("Cleaning process is completed.")
