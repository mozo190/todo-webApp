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

## Updates:

* I have updates the script to move files to a "Trash" folder within hte Downloads folder instead of deleting them. This allows for easier recovery of files that were accidentally deleted.
* Ask for user input, whether to move the file to trash or not.
* A new Cleaner Stats class has been added to track statistics about the cleaning process. It records the number of files moved and skipped and then prints the statistics at the ond of the program.

## **Run the app With the Windows Task Scheduler**

you can set the script to run automatically with the following steps:

## **1. Create a .bat file**

This .bat file will run the Python script. Create a text file with the following content and save it as, for example, clean_downloads.bat:

`@echo off
pythonw "C:\\az_elérési_út_ide\\a_script_fájl_útvonala\\download_cleaner.py" --folder "C:\\Users\\[Felhasználó_neve]\\Downloads" --days 30
`
**Important:** Change the python path to the valid Python executable if necessary. Change the paths according to your own folder.

## 2. Open the Task Scheduler.

Type "Task Scheduler" in the Windows search box int the Start menu and open the application.

## 3. Create a new task.

Click on "Create Basic Task" in the Actions pane on the right side of the window.
Give the task a name, for example, "CleanUp Downloads". Under "Security Settings", select "Run even if the user is not logged in" if necessary.

## 4. Set the start conditions.

Go to the "Launchers" tab.
Click the "New" button and select when you want to run the script. For example, you can set it to run daily at a specific time.
Enter an exact time when you want the script to run.

## 5. Set the action.

On the "Action" tab, click the "New" button.
Enter the path to your .bat file in the "Program/script" field.

## 6. Save the task.

Click "OK" to save the task.
In the Task Scheduler window, right-click on the task and select "Run" to test if it works.

## 7. Testing

Check that the files in the download folder are properly cleaned according to the specified criteria.
Look at the log file (download_cleaner.log) to see what events happened during the cleaning process.

* The task will now run automatically based on the trigger you set.
* You can also set the task to run with the highest privileges to avoid any permission issues.
* You can also set the task to run only when the user is logged in or not.
* You can also set the task to run only when the computer is idle or not.
* You can also set the task to run only when the computer is on AC power or not.

## License:

This project is licensed under the MIT License. See the LICENSE file for more information.
