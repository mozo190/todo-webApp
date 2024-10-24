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

window = sg.Window("File Extractor",
                   layout=[[label1, input_box1, choose_button1],
                           [label2, input_box2, choose_button2],
                           [extract_button, output_label]])
while True:
    event, values = window.read()
    print(1, event, values)
    print(2, values)
    filepaths = values["files"].split(";")
    print(3, filepaths)
    folder = values["destination"]
    if event == sg.WIN_CLOSED:
        break
    elif event == "Extract":
        print("Extracting...")
        functions.extract_files(filepaths[0], folder)
        window["output"].update("Files extracted successfully")
        print("Files extracted successfully")

print("Goodbye!")
window.close()
