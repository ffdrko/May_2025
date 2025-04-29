# Takes three different inputs from the user (e.g., a number, a word, and a decimal).
# Uses the type() function to print the data type of each input.
# Example:

# Enter a number: 42
# Enter a word: Python
# Enter a decimal: 3.14
# Type of 42 is <class 'str'>
# Type of Python is <class 'str'>
# Type of 3.14 is <class 'str'>

user_input1 = int(input("Enter a number: "))
user_input2 = input("Enter a word: ")
user_input3 = float(input("Enter a decimal: "))

print("Type of", user_input1, "is", type(user_input1))
print("Type of", user_input2, "is", type(user_input2))
print("Type of", user_input3, "is", type(user_input3))