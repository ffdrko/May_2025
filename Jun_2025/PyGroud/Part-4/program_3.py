def get_todo(filepath="files/todo_list.txt"):
    """ this function is taking
        the todo from the user.
    """
    with open(filepath) as file:
        local_list = file.readlines()
    return local_list


def write_todo(todos_arg, filepath="files/todo_list.txt"):
    """ this function is saving the
        input from the user.
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

print(help(get_todo))


while True:
    user_Action = input("Type add, show, edit, complete, exit: ").strip()

    if user_Action.startswith("add"):
        user_todo = user_Action[4:] + "\n"

        todo_list = get_todo()

        todo_list.append(user_todo)

        write_todo(todo_list)
    elif user_Action.startswith("show"):
        todo_list = get_todo()

        for index, item in enumerate(todo_list):
            print(f"{index + 1}-{item.strip("\n")}.")
    elif user_Action.startswith("edit"):
        try:
            todo_no = int(user_Action[5:]) - 1
            todo_list = get_todo()
            todo_list[todo_no] = input("Enter a new todo: ") + "\n"

            write_todo(todo_list)
        except ValueError:
            print("The comment is not correct.")
    elif user_Action.startswith("complete"):
        try:
            todo_no = int(user_Action[9:]) - 1
            todo_list = get_todo()
            todo_list.pop(todo_no)

            write_todo(todo_list)
        except IndexError:
            print("This is not the size of the list.")
    elif user_Action.startswith("exit"):
        break