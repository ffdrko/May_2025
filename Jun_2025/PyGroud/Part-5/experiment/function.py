def get_todo(filename="../files/todo_list.txt"):
    with open(filename) as file:
        local_todo_list = file.readlines()
    return local_todo_list

def write_todo(todo_args,filename="../files/todo_list.txt"):
    with open(filename, "w") as file:
        file.writelines(todo_args)

# print(x)
print("I am outside.")
print(__name__)
print(type(__name__))
if __name__ == "__main__":
    print(get_todo())
