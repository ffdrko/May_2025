while True:
    user_Action = input('Type add, show, edit, complete or exit: ').strip()

    if 'add' in user_Action:
        user_todo = user_Action[4:]

        with open('files/todo_lst.txt') as file:
            todo_list = file.readlines()

        todo_list.append(user_todo)

        with open('files/todo_lst.txt', 'w') as file:
            file.writelines(todo_list)

    if 'show' in user_Action:
        with open('files/todo_lst.txt') as file:
            todo_list = file.readlines()

        for index, item in enumerate(todo_list):
            print(f'{index + 1}-{item.strip('\n')}')

    if 'edit' in user_Action:
        todo_no = int(input("Enter the todo number for edit: ")) - 1

        with open('files/todo_lst.txt') as file:
            todo_list = file.readlines()

        todo_list[todo_no] = input("Enter a new todo: ") + "\n"

        with open('files/todo_lst.txt', 'w') as file:
            file.writelines(todo_list)

    if 'complete' in user_Action:
        todo_no = int(input("Enter the todo number for edit: ")) - 1

        with open('files/todo_lst.txt') as file:
            todo_list = file.readlines()

        todo_list.pop(todo_no)

        with open('files/todo_lst.txt', 'w') as file:
            file.writelines(todo_list)
    if 'exit' in user_Action:
        break