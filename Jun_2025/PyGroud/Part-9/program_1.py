while True:
    user_Action = input('Type add, show, edit, complete or exit: ')

    match user_Action:
        case 'add':
            user_todo = input('Enter a todo: ') + '\n'

            with open('files/todo_lst.txt') as file:
                todo_list = file.readlines()

            todo_list.append(user_todo)

            with open('files/todo_lst.txt', 'w') as file:
                file.writelines(todo_list)
        case 'show':
            with open('files/todo_lst.txt') as file:
                todo_list = file.readlines()

            for index, item in enumerate(todo_list):
                print(f'{index + 1}-{item.strip('\n')}')
        case 'edit':
            todo_no = int(input("Enter the todo number for edit: ")) - 1

            with open('files/todo_lst.txt') as file:
                todo_list = file.readlines()

            todo_list[todo_no] = input("Enter a new todo: ") + "\n"

            with open('files/todo_lst.txt', 'w') as file:
                file.writelines(todo_list)
        case 'complete':
            todo_no = int(input("Enter the todo number for edit: ")) - 1

            with open('files/todo_lst.txt') as file:
                todo_list = file.readlines()

            todo_list.pop(todo_no)
        case 'exit':
            break