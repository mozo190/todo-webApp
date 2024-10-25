import PySimpleGUI as sg

import fileUnZip_functions as functions

sg.theme("DarkBlue3")

label1 = sg.Text("Select files to compress")
input_box1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder")
input_box2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="destination")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="white")

exit_button = sg.Button("Exit")

window = sg.Window("File Extractor",
                   layout=[[label1, input_box1, choose_button1],
                           [label2, input_box2, choose_button2],
                           [extract_button, exit_button, output_label]])
while True:
    event, values = window.read()
    filepaths = values["files"].split(";")
    folder = values["destination"]

    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Extract":
        if not filepaths or not folder:
            sg.popup("Please select files and destination folder.")
            continue
        print("Extracting...")
        functions.extract_files(filepaths[0], folder)
        window["output"].update("Files extracted successfully")


print("Goodbye!")
window.close()
