password = input("Enter your password: ")
result = {}

if len(password) >= 8:
    result['length'] = True
else:
    result['length'] = True

digit = False

for i in password:
    if i.isdigit():
        digit = True

result['digits'] = digit

upper = False

for i in password:
    if i.isupper():
        upper = True

result['Upper'] = upper

if all(result.values()):
    print("strong password.")
else:
    print("not strong password.")
