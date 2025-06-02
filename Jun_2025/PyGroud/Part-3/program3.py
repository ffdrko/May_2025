def greet(message):
    text = message.capitalize()
    print("hey hey")
    return text

user_message = input("Enter your message: ")

context = greet(user_message)

print(context)