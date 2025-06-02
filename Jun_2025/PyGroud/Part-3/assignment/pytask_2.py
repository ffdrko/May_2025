def strength(password):
    result = {}

    if len(password) >= 8:
        result['length'] = True
    else:
        result['length'] = False

    digit = False
    uppercase = False

    for i in password:
        if i.isdigit():
            digit = True
        if i.isupper():
            uppercase = True

    result['digit'] = digit
    result['upper'] = uppercase

    if all(result.values()):
        return  "Strong password"
    else:
        return "Weak password"


strength("wolverin_Xmen12")