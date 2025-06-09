from function_1 import get_todos, write_todos

while True:
    user_action = input("Type add, show, edit, complete, exit: ")

    if user_action.startswith('add'):
        user_todo = user_action[4:] + "\n"

        todo_list = get_todos()

        todo_list.append(user_todo)

        write_todos(todo_list)
    elif user_action.startswith('show'):
        todo_list = get_todos()

        for index, item in enumerate(todo_list):
            print(f"{index + 1}-{item.strip('\n')}")
    elif user_action.startswith('edit'):
        user_todo_no = int(user_action[5:]) - 1

        todo_list = get_todos()

        todo_list[user_todo_no] = input("Enter a todo: ") + '\n'
        write_todos(todo_list)
    elif user_action.startswith('complete'):
        user_todo_no = int(user_action[9:]) - 1

        todo_list = get_todos()

        todo_list.pop(user_todo_no)

        write_todos(todo_list)
    elif user_action.startswith('exit'):
        break
    else:
        print("It's a wrong action.")