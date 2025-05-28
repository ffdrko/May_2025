todos = []

while True:
    user_Action = input("Type add, show, edit, complete or exit: ")

    match user_Action:
        case 'add':
            user_todos = input("Enter a todo: ") + "\n"
            with open('files/todo_list.txt', 'r') as file:
                todo_list = file.readlines()

            todo_list.append(user_todos)

            with open('files/todo_list.txt', 'w') as file:
                file.writelines(todo_list)

        case 'show':
            with open('files/todo_list.txt', 'r') as file:
                todo_list = file.readlines()

            for index, item in enumerate(todo_list):
                print(f"{index + 1}-{item.strip('\n')}")

        case 'exit':
            break