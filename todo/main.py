

while True:
    user_action = input('Enter command "add", "show", "edit", "complete", or "exit":')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter todo:') + '\n'

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, todo in enumerate(todos):
                print(f"{index+1}. {todo}")

        case 'edit':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            index = int(input('Enter index:'))
            todo = input('Enter todo:')
            todos[index-1] = todo

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'complete':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            index = int(input('Enter index:'))
            todos.pop(index-1)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'exit':
            break
