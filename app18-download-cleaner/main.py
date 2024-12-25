import os
from datetime import datetime, timedelta

DOWNLOADS_PATH = os.path.expanduser("~/Downloads")
FILE_AGE_LIMIT_DAYS = 30


def is_file_old(file_path, days):
    file_age_limit = datetime.now() - timedelta(days=days)
    file_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
    return file_modified < file_age_limit
