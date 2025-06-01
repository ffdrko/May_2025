while True:
    user_Action = input("Type add, show, edit, complete or exit: ").strip()

    if user_Action.startswith('add'):
        user_todo = user_Action[4:] + "\n"
        with open("files/todo_list.txt") as file:
            todo_list = file.readlines()

        todo_list.append(user_todo)

        with open("files/todo_list.txt", "w") as file:
            file.writelines(todo_list)

    elif user_Action.startswith('show'):
        with open("files/todo_list.txt") as file:
            todo_list = file.readlines()

        for index, item in enumerate(todo_list):
            print(f"{index + 1}-{item.strip("\n")}")

    elif user_Action.startswith('edit'):
        try:
            todo_no = int(user_Action[4:]) + 1

            with open("files/todo_list.txt") as file:
                todo_list = file.readlines()

            todo_list[todo_no] = input("Enter the new todo: ") + "\n"

            with open("files/todo_list.txt", "w") as file:
                file.writelines(todo_list)
        except ValueError:
            print("You have enter number after edit.")
    elif user_Action.startswith('complete'):
        try:
            todo_no = int(user_Action[4:]) + 1

            with open("files/todo_list.txt") as file:
                todo_list = file.readlines()

            todo_list.pop(todo_no)

            with open("files/todo_list.txt", "w") as file:
                file.writelines(todo_list)
        except IndexError:
            with open("files/todo_list.txt") as file:
                todo_list = file.readlines()

            print(f"The size of the list is {len(todo_list)}")
    elif user_Action.startswith('exit'):
        break
    else:
        print("Wrong action, try again?")