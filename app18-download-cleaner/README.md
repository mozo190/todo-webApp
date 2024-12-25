# **Downloads Folder Cleaner**

This Python script implements a simple downloads folder cleaner. The script monitors the Downloads folder and deletes files that are older than a specified duration. The script supports command-line arguments, allowing customization of the downloads folder and the duration at startup.

## Usage:

To run the script, use the following command:

`python download_cleaner.py`

You can also specify a custom folder and duration using command_linea arguments:

python download_cleaner.py -f <folder_path> -d <duration_in_days>

or

`python download_cleaner.py --folder "C:\Users\John\Downloads"`

`python download_cleaner.py --duration 30`

## **Command-Line Arguments:**

* _--folder_: Specifies the folder path to clean. Default is the Downloads folder.
* _--days_: Specifies the file age limit in days. Files older than this limit will be deleted. Default is 30 days.

## **Example:**

`python download_cleaner.py --folder "C:\Users\John\Downloads" --days 30`

## **Requirements:**

Python 3.x

Updates:

I have updates the script to move files to a "Trash" folder within hte Downloads folder instead of deleting them. 
This allows for easier recovery of files that were accidentally deleted.

## License:

This project is licensed under the MIT License. See the LICENSE file for more information.
