from function import get_todo, write_todo
while True:
    user_action = input("Type add, show, edit, complete and exit:").strip()

    if user_action.startswith("add"):
        user_todo = user_action[4:] + "\n"

        todo_list = get_todo()

        todo_list.append(user_todo)

        write_todo(todo_list)

    elif user_action.startswith("show"):
        todo_list = get_todo()

        for index, item in enumerate(todo_list):
            print(f"{index + 1}-{item.strip("\n")}")

    elif user_action.startswith("edit"):
        try:
            todo_no = int(user_action[5:]) - 1

            todo_list = get_todo()

            todo_list[todo_no] = input("Enter the new todo: ") + "\n"

            write_todo(todo_list)
        except ValueError:
            print("Please enter number.")

    elif user_action.startswith("complete"):
        try:
            todo_no = int(user_action[9:]) - 1

            todo_list = get_todo()

            todo_list.pop(todo_no)

            write_todo(todo_list)
        except IndexError:
            print("The number you entry is not the size of the list.")

    elif user_action.startswith("exit"):
        break
    else:
        print("Wrong comment!!!")