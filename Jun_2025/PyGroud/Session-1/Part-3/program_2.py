todo_lst = []
while True:
    user_action = input("Type add, show or exit: ")

    match user_action:
        case 'add':
            user_todo = input("Enter a todo: ")
            todo_lst.append(user_todo)
        case 'show':
            print(todo_lst)
        case 'exit':
            break
print("End of operation.")