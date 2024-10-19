PATH = 'files/todos.txt'


def read_todos_txt_file(file_path=PATH):
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_into_todos_txt_file(todos, path=PATH):
    with open(path, 'w') as file_local:
        file_local.writelines(todos)
