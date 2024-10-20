import FreeSimpleGUI
import FreeSimpleGUI as sg

import functions

label = sg.Text("My To-do App")
input_box = sg.InputText(tooltip="Enter todo", size=(40, 1))
add_button = sg.Button("Add")

window = FreeSimpleGUI.Window("Todo App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
