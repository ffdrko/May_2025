todo = []

while True:
    user_action = input("Type add, show, edit or exit: ")

    match user_action:
        case 'add':
            user_todo = input("Enter a todo: ")
            todo.append(user_todo)
        case 'show':
            for item in todo:
                print(item)
        case 'edit':
            todo_no = int(input("Enter a todo number: ")) - 1
            todo[todo_no] = input("Enter a new todo: ")
        case 'exit':
            break