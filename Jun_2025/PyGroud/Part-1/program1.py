while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if 'add' in user_action:
        user_todo = user_action[4:] + "\n"

        with open("files/todo_list.txt") as file:
            todo_list = file.readlines()

        todo_list.append(user_todo)

        with open("files/todo_list.txt", "w") as file:
            file.writelines(todo_list)

    elif 'show' in user_action:
        with open("files/todo_list.txt") as file:
            todo_list = file.readlines()

        for index, item in enumerate(todo_list):
            print(f"{index + 1}-{item.strip('\n')}")

    elif 'edit' in user_action:
        todo_no = int(user_action[5:]) - 1

        with open("files/todo_list.txt")as file:
            todo_list = file.readlines()

        todo_list[todo_no] = input("Enter a new todo: ") + "\n"

        with open("files/todo_list.txt", "w") as file:
            file.writelines(todo_list)

    elif 'complete' in user_action:
        todo_no = int(user_action[9:]) - 1

        with open("files/todo_list.txt") as file:
            todo_list = file.readlines()

        todo_list.pop(todo_no)

        with open("files/todo_list.txt", "w") as file:
            file.writelines(todo_list)

    elif 'exit' in user_action:
        break

    else:
        print("Wrong comment!!!")