# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

needed_year = 100 - user_age
current_year = 2025 + needed_year

print("Hey,", user_name, ",you will be 100 years old in", current_year)