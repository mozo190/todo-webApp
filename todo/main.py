todos = []

while True:
    user_action = input('Enter command:')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter todo:')
            todos.append(todo)
        case 'show':
            print(todos)
        case 'edit':
            index = int(input('Enter index:'))
            todo = input('Enter todo:')
            todos[index-1] = todo
        case 'exit':
            break
