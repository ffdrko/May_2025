while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith('add'):
        user_todo = user_action[4:]

        with open("files/todo_list.txt") as file:
            todo_list = file.readlines()

        todo_list.append(user_todo + "\n")

        with open("files/todo_list.txt", "w") as file:
            file.writelines(todo_list)

    elif user_action.startswith('show'):
        with open("files/todo_list.txt") as file:
            todo_list = file.readlines()

        for index, item in enumerate(todo_list):
            print(f"{index + 1}-{item.strip('\n')}")

    elif user_action.startswith('edit'):
        try:
            todo_no = int(user_action[5:]) - 1

            with open("files/todo_list.txt") as file:
                todo_list = file.readlines()

            todo_list[todo_no] = input("Enter a new todo: ") + "\n"

            with open("files/todo_list.txt", "w") as file:
                file.writelines(todo_list)
        except ValueError:
            print("Comment statement is not right.")
            continue

    elif user_action.startswith('complete'):
        try:
            todo_no = int(user_action[9:]) - 1

            with open("files/todo_list.txt") as file:
                todo_list = file.readlines()

            todo_list.pop(todo_no)

            with open("files/todo_list.txt", "w") as file:
                file.writelines(todo_list)
        except IndexError:
            print("This not the size of list.")

    elif user_action.startswith('exit'):
        break

    else:
        print("Wrong comment!!!")