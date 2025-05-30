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

        case 'edit':
            todo_num = int(input("Enter the todo number for edit: ")) - 1

            with open('files/todo_list.txt', 'r') as file:
                todo_list = file.readlines()

            todo_list[todo_num] = input("Enter the new todo: ") + "\n"

            with open('files/todo_list.txt', 'w') as file:
                file.writelines(todo_list)

        case 'complete':
            todo_num = int(input("Enter the complete todo number: ")) - 1

            with open('files/todo_list.txt', 'r') as file:
                todo_list = file.readlines()

            remove_todo = todo_list[todo_num]
            todo_list.pop(todo_num)

            with open('files/todo_list.txt', 'w') as file:
                file.writelines(todo_list)

            print(f"Todo = {remove_todo.strip('\n')} is removed successfully.")
        case 'exit':
            break