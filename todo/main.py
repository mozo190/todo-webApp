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

    elif 'show' in user_action:
        read_todos_txt_file()

        new_todos = []

        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)

        for index, todo in enumerate(new_todos):
            print(f"{index + 1}. {todo}")

    elif 'edit' in user_action:
        number = int(user_action[5:])
        print(number)

        read_todos_txt_file()

        # index = int(input('Enter index:'))
        todo = input('Enter todo:') + '\n'
        todos[number] = todo

        write_into_todos_txt_file()

    elif 'complete' in user_action:
        number = int(user_action[9:])

        read_todos_txt_file()

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