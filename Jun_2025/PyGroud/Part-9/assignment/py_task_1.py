user_pass = input("Enter a new password: ")

if len(user_pass) >= 7:
    print("Great password")
else:
    print("Your password is weak")