todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action:
        case 'add':
            user_todo = input("Enter a todo: ") + "\n"

            file = open('files/todo_list.txt', 'r')
            todo_list = file.readlines()
            file.close()

            todo_list.append(user_todo)

            file = open('files/todo_list.txt', 'w')
            file.writelines(todo_list)
            file.close()
        case 'show':
            file = open('files/todo_list.txt', 'r')
            todo_list = file.readlines()
            file.close()

            for index, item in enumerate(todo_list):
                print(f"{index + 1}-{item}")
        case 'edit':
            user_todo_no = int(input("Enter the todo number to edit: "))
            todos[user_todo_no - 1] = input("Enter a new todo: ")
        case 'complete':
             user_todo_no = int(input("Enter the todo number to edit: ")) - 1
             todos.pop(user_todo_no)
        case 'exit':
            break