import argparse
import logging
import os
import shutil
from datetime import datetime, timedelta

DOWNLOADS_PATH = os.path.expanduser("~/Downloads")
FILE_AGE_LIMIT_DAYS = 30

# Logging configuration
logging.basicConfig(
    filename='download_cleaner.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def is_file_old(file_path, days):
    file_age_limit = datetime.now() - timedelta(days=days)
    file_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
    return file_modified < file_age_limit


def clean_downloads_folder(folder_path, days):
    trash_folder = os.path.join(folder_path, 'Trash')
    os.makedirs(trash_folder, exist_ok=True)

    if not os.path.exists(folder_path):
        logging.error(f'Folder does not exist: {folder_path}')
        return

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = str(os.path.join(root, file))
            if is_file_old(file_path, days):
                try:
                    print(f'Moving to trash: {file_path}? (y/n): ', end='')  # Ask for user input
                    user_input = input().strip().lower()

                    if user_input == 'y':
                        trash_path = os.path.join(trash_folder, file)
                        shutil.move(file_path, trash_path)
                        logging.info(f'Moved to trash: {file_path}')
                        print(f'Moved to trash: {file_path}')
                    else:
                        print(f'Skipped: {file_path}')
                except Exception as e:
                    logging.error(f'Error moving file: {file_path} - {e}')


def command_line_input():
    global DOWNLOADS_PATH, FILE_AGE_LIMIT_DAYS
    parser = argparse.ArgumentParser(description='Clean files older than N days in a folder.')
    parser.add_argument('--folder', default=DOWNLOADS_PATH, help='Folder path to clean')
    parser.add_argument('--days', type=int, default=FILE_AGE_LIMIT_DAYS, help='File age limit in days')
    args = parser.parse_args()

    DOWNLOADS_PATH = str(args.folder)  # Convert to string to avoid Pathlib object
    FILE_AGE_LIMIT_DAYS = args.days


if __name__ == "__main__":
    # Command line arguments
    command_line_input()

    print(f"Cleaning files older than {FILE_AGE_LIMIT_DAYS} days in {DOWNLOADS_PATH} is starting...")
    clean_downloads_folder(DOWNLOADS_PATH, FILE_AGE_LIMIT_DAYS)
    print("Cleaning process is completed.")
