import time

from functions import read_todos_txt_file, write_into_todos_txt_file

now = time.strftime('%Y-%m-%d %H:%M:%S')
print(f'Current time: {now}')

while True:
    user_action = input('Enter command "add", "show", "edit", "complete", or "exit":')
    user_action = user_action.strip()

    # match user_action:
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = read_todos_txt_file()

        todos.append(todo + '\n')

        write_into_todos_txt_file(todos)

    elif user_action.startswith('show'):
        todos = read_todos_txt_file()

        new_todos = []

        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)

        for index, todo in enumerate(new_todos):
            print(f"{index + 1}. {todo}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            todos = read_todos_txt_file()

            # index = int(input('Enter index:'))
            todo = input('Enter todo:') + '\n'
            todos[number - 1] = todo

            write_into_todos_txt_file(todos)
        except ValueError:
            print('Invalid index!')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = read_todos_txt_file()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            write_into_todos_txt_file(todos)

            message = f'Todo with index {number}: "{todo_to_remove}" has been completed.'
            print(message)
        except IndexError:
            print('Invalid index!')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Invalid command!')

print('Goodbye!')
