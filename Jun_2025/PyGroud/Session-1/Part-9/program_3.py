while True:
    user_Action = input('Type add, show, edit, complete or exit: ').strip()

    if 'add' in user_Action:
        user_todo = user_Action[4:]

        with open('files/todo_lst1.txt') as file:
            todo_list = file.readlines()

        todo_list.append(user_todo)

        with open('files/todo_lst1.txt', 'w') as file:
            file.writelines(todo_list)

    elif 'show' in user_Action:
        with open('files/todo_lst1.txt') as file:
            todo_list = file.readlines()

        for index, item in enumerate(todo_list):
            print(f'{index + 1}-{item.strip('\n')}')

    elif 'edit' in user_Action:
        todo_no = int(user_Action[5:]) - 1

        with open('files/todo_lst1.txt') as file:
            todo_list = file.readlines()

        todo_list[todo_no] = input("Enter a new todo: ") + "\n"

        with open('files/todo_lst1.txt', 'w') as file:
            file.writelines(todo_list)

    elif 'complete' in user_Action:
        todo_no = int(user_Action[9:]) - 1

        with open('files/todo_lst1.txt') as file:
            todo_list = file.readlines()

        todo_list.pop(todo_no)

        with open('files/todo_lst1.txt', 'w') as file:
            file.writelines(todo_list)
    elif 'exit' in user_Action:
        break
    else:
        print("Invalid comment!!!")