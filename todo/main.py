def read_todos_txt_file():
    with open('files/todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_into_todos_txt_file():
    with open('files/todos.txt', 'w') as file_local:
        todos_local = file_local.writelines(todos)
    return todos_local


while True:
    user_action = input('Enter command "add", "show", "edit", "complete", or "exit":')
    user_action = user_action.strip()

    # match user_action:
    if 'add' in user_action:
        todo = user_action[4:] + '\n'

        todos = read_todos_txt_file()

        todos.append(todo)

        write_into_todos_txt_file()

    elif 'show' in user_action:
        todos = read_todos_txt_file()

        new_todos = []

        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)

        for index, todo in enumerate(new_todos):
            print(f"{index + 1}. {todo}")

    elif 'edit' in user_action:
        number = int(user_action[5:])
        print(number)

        todos = read_todos_txt_file()

        # index = int(input('Enter index:'))
        todo = input('Enter todo:') + '\n'
        todos[number] = todo

        write_into_todos_txt_file()

    elif 'complete' in user_action:
        number = int(user_action[9:])

        todos = read_todos_txt_file()

        todo_to_remove = todos[number - 1].strip('\n')
        todos.pop(number - 1)

        write_into_todos_txt_file()

        message = f'Todo with index {number}: "{todo_to_remove}" has been completed.'
        print(message)

    elif 'exit' in user_action:
        break

    else:
        print('Invalid command!')

print('Goodbye!')
