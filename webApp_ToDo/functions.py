import streamlit

PATH = 'todos.txt'


def read_todos_txt_file(file_path=PATH):
    try:  # Try to read the file
        """ Read the todos.txt file and return the content as a list of strings. """
        with open(file_path, 'r') as file_local:
            todos_local = file_local.readlines()
        return todos_local
    except FileNotFoundError:
        return []


def write_into_todos_txt_file(todos, path=PATH):
    """ Write the todos list into the todos.txt file. """
    with open(path, 'w') as file_local:
        file_local.writelines(todos)


def add_todo():
    """ Add a new to do to the todos list. """
    todo1 = streamlit.session_state["new_todo"] + '\n'
    todos = read_todos_txt_file()
    todos.append(todo1)
    write_into_todos_txt_file(todos)
    streamlit.session_state["new_todo"] = ""


if __name__ == '__main__':
    print("This is a module with functions for the todo app.")
    print(read_todos_txt_file())
