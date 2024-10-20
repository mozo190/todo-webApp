import FreeSimpleGUI as sg
import zip_creator

label1 = sg.Text("Select files to compress")
input_box1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder")
input_box2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="destination")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output")

window = sg.Window("File Compressor", layout=[[label1, input_box1, choose_button1],
                                              [label2, input_box2, choose_button2],
                                              [compress_button, output_label]])
while True:
    event, values = window.read()
    print(1, event, values)
    print(2, values)
    filepaths = values["files"].split(";")
    print(3, filepaths)
    folder = values["destination"]
    if event == sg.WIN_CLOSED:
        break
    elif event == "Compress":
        print("Compressing...")
        zip_creator.make_archive(filepaths, folder)
        window["output"].update("Files compressed successfully")
        print("Files compressed successfully")
print("Goodbye!")
window.close()
