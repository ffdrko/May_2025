import random

def get_num(start_num, last_num):
    return random.randint(start_num, last_num)

user_first_num = int(input("Enter a number: "))
user_last_num = int(input("Enter a number: "))

print(get_num(user_first_num, user_last_num))