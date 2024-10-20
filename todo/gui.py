import FreeSimpleGUI as sg

import functions

label = sg.Text("My To-do App")
input_box = sg.InputText(tooltip="Enter todo", size=(40, 1), key="todo")
add_button = sg.Button("Add")

window = sg.Window("Todo App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.read_todos_txt_file()
            todos.append(values["todo"] + '\n')
            functions.write_into_todos_txt_file(todos)
        case sg.WIN_CLOSED:
            break

window.close()
