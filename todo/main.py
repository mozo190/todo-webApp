def read_todos_txt_file():
    global file, todos
    with open('files/todos.txt', 'r') as file:
        todos = file.readlines()


while True:
    user_action = input('Enter command "add", "show", "edit", "complete", or "exit":')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter todo:') + '\n'

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            read_todos_txt_file()

            new_todos = []

            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)

            for index, todo in enumerate(new_todos):
                print(f"{index + 1}. {todo}")

        case 'edit':
            read_todos_txt_file()

            index = int(input('Enter index:'))
            todo = input('Enter todo:') + '\n'
            todos[index - 1] = todo

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            read_todos_txt_file()

            index = int(input('Enter index:'))
            todo_to_remove = todos[index - 1].strip('\n')
            todos.pop(index - 1)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f'Todo with index {index}: "{todo_to_remove}" has been completed.'
            print(message)

        case 'exit':
            break
