user_prompt = "Enter a todo: "
todo_lst = []

while True:
    todo = input(user_prompt).capitalize()
    todo_lst.append(todo)
    print(todo_lst)