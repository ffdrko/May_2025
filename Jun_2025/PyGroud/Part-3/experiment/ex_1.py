todo_last = []

while True:
    user_action = input("Type add, show or exit: ").strip()

    match user_action:
        case 'add':
            user_todo = input("Enter a todo: ")
            todo_last.append(user_todo)
        case 'show':
            for item in todo_last:
                print(item)
        case 'exit':
            break
        case _:
            print("Wrong message")

print("End of operation.")