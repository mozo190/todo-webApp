import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress")
input_box1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select destination folder")
input_box2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

window = sg.Window("File Compressor", layout=[[label1, input_box1, choose_button1],
                                              [label2, input_box2, choose_button2]])

window.read()
window.close()
