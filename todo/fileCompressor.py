import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress")
input_box1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder")
input_box2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[[label1, input_box1, choose_button1],
                                              [label2, input_box2, choose_button2],
                                              [compress_button]])
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    if event == sg.WIN_CLOSED:
        break
    elif event == "Compress":
        print("Compressing...")
        break
print("Goodbye!")
window.close()
