import os
import time

import FreeSimpleGUI as sg

import functions

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("LightBrown4")

clock_label = sg.Text("", key="clock")
label = sg.Text("My To-do App")
input_box = sg.InputText(tooltip="Enter todo", size=(40, 1), key="todo")
image_source = "add.PNG"
if os.path.exists(image_source):
    add_button = sg.Button(size=(10, 1), image_source=image_source, tooltip="Add todo", key="Add")
else:
    add_button = sg.Button("Add", tooltip="Add todo", key="Add")
list_box = sg.Listbox(values=functions.read_todos_txt_file(), size=(40, 10),
                      key="todos", enable_events=True)
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")
image_source_complete = "complete.PNG"
if os.path.exists(image_source_complete):
    complete_button = sg.Button(key="Complete", image_source=image_source_complete)
else:
    complete_button = sg.Button("Complete", key="Complete")

window = sg.Window("Todo App",
                   layout=[[clock_label],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.read_todos_txt_file()
            todos.append(values["todo"] + '\n')
            functions.write_into_todos_txt_file(todos)
            window["todo"].update(value="")
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.read_todos_txt_file()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_into_todos_txt_file(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first.")

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.read_todos_txt_file()
                todos.remove(todo_to_complete)
                functions.write_into_todos_txt_file(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first.")
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
print("Goodbye!")
window.close()
