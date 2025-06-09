import function_1
import time

while True:
    user_action = input("Type add, show, edit, complete, exit: ")

    if user_action.startswith('add'):
        user_todo = user_action[4:] + "\n"

        todo_list = function_1.get_todos()

        todo_list.append(user_todo)

        function_1.write_todos(todo_list)
        print(f"The time is {time.strftime("%d-%m-%Y")}")
    elif user_action.startswith('show'):
        todo_list = function_1.get_todos()

        for index, item in enumerate(todo_list):
            print(f"{index + 1}-{item.strip('\n')}")
    elif user_action.startswith('edit'):
        user_todo_no = int(user_action[5:]) - 1

        todo_list = function_1.get_todos()

        todo_list[user_todo_no] = input("Enter a todo: ") + '\n'
        function_1.write_todos(todo_list)
    elif user_action.startswith('complete'):
        user_todo_no = int(user_action[9:]) - 1

        todo_list = function_1.get_todos()

        todo_list.pop(user_todo_no)

        function_1.write_todos(todo_list)
    elif user_action.startswith('exit'):
        break
    else:
        print("It's a wrong action.")