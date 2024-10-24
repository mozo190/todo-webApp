import zipfile


def extract_files(archive_path, destination_folder):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(destination_folder)


if __name__ == '__main__':
    extract_files('files/compressed.zip', 'files')
