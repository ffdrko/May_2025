def get_todos(filepath="files/todo_list.txt"):
    with open(filepath) as file:
        local_list = file.readlines()
    return local_list

def write_todos(todo_args ,filepath="files/todo_list.txt"):
    with open(filepath, "w") as file:
        file.writelines(todo_args)