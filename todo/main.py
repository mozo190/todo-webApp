def read_todos_txt_file():
    global file, todos
    with open('files/todos.txt', 'r') as file:
        todos = file.readlines()


def write_into_todos_txt_file():
    global file
    with open('files/todos.txt', 'w') as file:
        file.writelines(todos)


while True:
    user_action = input('Enter command "add", "show", "edit", "complete", or "exit":')
    user_action = user_action.strip()

    # match user_action:
    if 'add' in user_action:
        todo = input('Enter todo:') + '\n'

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        write_into_todos_txt_file()

    if 'show' in user_action:
        read_todos_txt_file()

        new_todos = []

        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)

        for index, todo in enumerate(new_todos):
            print(f"{index + 1}. {todo}")

    if 'edit' in user_action:
        read_todos_txt_file()

        index = int(input('Enter index:'))
        todo = input('Enter todo:') + '\n'
        todos[index - 1] = todo

        write_into_todos_txt_file()

    if 'complete' in user_action:
        read_todos_txt_file()

        index = int(input('Enter index:'))
        todo_to_remove = todos[index - 1].strip('\n')
        todos.pop(index - 1)

        write_into_todos_txt_file()

        message = f'Todo with index {index}: "{todo_to_remove}" has been completed.'
        print(message)

    if 'exit' in user_action:
        break

print('Goodbye!')