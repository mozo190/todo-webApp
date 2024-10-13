todos = []

while True:
    user_action = input('Enter command:')

    match user_action:
        case 'add':
            todo = input('Enter todo:')
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
