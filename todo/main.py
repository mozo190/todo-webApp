todos = []

while True:
    user_action = input('Enter command "add", "show", "edit", or "exit":')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter todo:')

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, todo in enumerate(todos):
                print(f"{index+1}. {todo}")
        case 'edit':
            index = int(input('Enter index:'))
            todo = input('Enter todo:')
            todos[index-1] = todo
        case 'exit':
            break
