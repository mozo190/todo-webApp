import FreeSimpleGUI as sg

import functions

label = sg.Text("My To-do App")
input_box = sg.InputText(tooltip="Enter todo", size=(40, 1), key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.read_todos_txt_file(), size=(40, 10),
                      key="todos", enable_events=True)
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")

window = sg.Window("Todo App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button], [exit_button]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    match event:
        case "Add":
            todos = functions.read_todos_txt_file()
            todos.append(values["todo"] + '\n')
            functions.write_into_todos_txt_file(todos)
            window["todo"].update(value="")
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.read_todos_txt_file()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_into_todos_txt_file(todos)
            window["todos"].update(values=functions.read_todos_txt_file())
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
print("Goodbye!")
window.close()
