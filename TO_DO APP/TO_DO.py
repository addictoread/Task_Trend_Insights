while True:
    user_action = input("Print add, show, exit,edi, complete")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo") + "\n"

            file = open("todo.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todo.txt", "w")
            file.writelines()
            file.close()
        case 'show':
            file = open("todo.txt", "r")
            todos = file.readlines()
            file.close()

            # another way = new_todo = [item.strip("\n") for item in todos]

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Enter no of todo to edit"))
            number = number -1
            new_todo = input("New todo?")
            todos[number] = new_todo
        case 'complete':
            number = int(input("no of todo to mark complete"))
            todos.pop(number -1)
        case 'exit':
            print("exit")




