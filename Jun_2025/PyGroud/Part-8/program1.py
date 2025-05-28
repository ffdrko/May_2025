todos = []

while True:
    user_Action = input("Type add, show, edit, complete or exit: ")

    match user_Action:
        case 'add':
            user_todos = input("Enter a todo: ") + "\n"

            file = open('files/todo_list.txt', 'r')
            todo_list = file.readlines()
            file.close()

            todo_list.append(user_todos)

            file = open('files/todo_list.txt', 'w')
            file.writelines(todo_list)

        case 'show':
            file = open('files/todo_list.txt', 'r')
            todo_list = file.readlines()
            file.close()

            for index, item in enumerate(todo_list):
                print(f"{index + 1}-{item.strip('\n')}")

        case 'exit':
            break