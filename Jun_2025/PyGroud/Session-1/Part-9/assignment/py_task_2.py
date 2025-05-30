user_pass = input("Enter a new password: ")

if len(user_pass) > 7:
    print("Great password")
elif len(user_pass) == 7:
    print("password is okay but not too strong.")
else:
    print("Your password is weak")