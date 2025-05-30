user_input_date = input("Enter today's date: ")
user_input_mode = int(input("How do your mood today from 1 to 10: "))
user_thoughts = input("Let your thoughts flow:\n")

with open(f'files/{user_input_date}.txt', 'w') as file:
    file.write(user_thoughts)