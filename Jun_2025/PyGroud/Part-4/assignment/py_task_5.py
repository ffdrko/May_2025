def pass_len(password):
    if len(password) < 8:
        return False
    else:
        return True

print(pass_len("deepto12do"))