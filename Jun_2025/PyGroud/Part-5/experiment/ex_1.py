todo_lst = []

while True:
    user_action = input("Type add, show, edit,complete or exit: ").strip()

    match user_action:
        case 'add':
            user_action = input("Enter a todo: ")
            todo_lst.append(user_action)
        case 'show':
            for item_no, item in enumerate(todo_lst):
                print(f"{item_no + 1}-{item}")
            print("Hello", item_no, item)
        case 'edit':
            user_todo_no = int(input("Number of the todo to edit: ")) - 1
            todo_lst[user_todo_no] = input("Enter a new todo: ")
        case 'complete':
            user_todo_no = int(input("Number of the todo is complete: ")) - 1
            todo_lst.pop(user_todo_no)
        case 'exit':
            break