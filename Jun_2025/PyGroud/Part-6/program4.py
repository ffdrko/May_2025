todo_lst = []

while True:
    user_action = input("TYpe add, show, edit, complete or exit: ").strip()

    match user_action:
        case 'add':
            user_todo = input("Enter a todo: ") + "\n"
            file = open('files/todo_lst.txt', 'r')
            todo_list = file.readlines()
            file.close()

            todo_lst.append(user_todo)

            file = open('files/todo_lst.txt', 'w')
            file.writelines(todo_lst)
            file.close()
        case 'show':
            file = open('files/todo_lst.txt', 'r')
            todo_list = file.readlines()
            file.close()

            for index, item in enumerate(todo_list):
                print(f"{index + 1}-{item}")
        case 'edit':
            user_todo_no = int(input("Enter the todo number to edit: "))
            todo_lst[user_todo_no - 1] = input("Enter new todo: ")
        case 'complete':
            user_todo_no = int(input("Complete todo number: "))
            todo_lst.pop(user_todo_no)
        case 'exit':
            break
