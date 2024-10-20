import pathlib
import zipfile


def make_archive(filepaths, dest_folder):
    dest_path = pathlib.Path(dest_folder, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as zipf:
        for file in filepaths:
            zipf.write(file, arcname=pathlib.Path(file).name)


if __name__ == '__main__':
    make_archive(['files/todos.txt'], 'files')
