def read_todo(filepath):
    with open(filepath) as file:
        local_list = file.readlines()
    return local_list

while True:
    users_action = input("Type add, show, edit, complete, exit: ").strip()

    if users_action.startswith("add"):
        user_todo = users_action[4:] + "\n"

        todo_list = read_todo("files/todo_list.txt")

        todo_list.append(user_todo)

        with open("files/todo_list.txt", "w") as files:
            files.writelines(todo_list)

    elif users_action.startswith("show"):
        todo_list = read_todo("files/todo_list.txt")

        for index, item in enumerate(todo_list):
            print(f"{index + 1}-{item.strip("\n")}")

    elif users_action.startswith("edit"):
        try:
            todo_no = int(users_action[5:]) - 1

            todo_list = read_todo("files/todo_list.txt")

            todo_list[todo_no] = input("Enter new todo: ") + "\n"

            with open("files/todo_list.txt", "w") as files:
                files.writelines(todo_list)
        except ValueError:
            print("Please enter number after edit.")
        except IndexError:
            print("The number you entry is not in the list.")

    elif users_action.startswith("complete"):
        try:
            todo_no = int(users_action[9:]) - 1

            todo_list = read_todo("files/todo_list.txt")

            todo_list.pop(todo_no)

            with open("files/todo_list.txt", "w") as files:
                files.writelines(todo_list)
        except IndexError:
            todo_list = read_todo()

            print(f"The size of list is {len(todo_list)}")

    elif users_action.startswith("exit"):
        break

    else:
        print("Wrong input!!! please enter correct input.")