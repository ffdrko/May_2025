todo_lst = []

while True:
    user_action = input("Type add, show, edit or exit: ").strip()

    match user_action:
        case 'add':
            user_action = input("Enter a todo: ")
            todo_lst.append(user_action)
        case 'show':
            for item_no, item in enumerate(todo_lst):
                print(item_no,"-",item)
        case 'edit':
            user_todo_no = int(input("Number of the todo to edit: ")) - 1
            todo_lst[user_todo_no] = input("Enter a new todo: ")
        case 'exit':
            break