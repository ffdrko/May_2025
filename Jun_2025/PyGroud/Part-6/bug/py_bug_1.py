from parse import parse
import random

user_input = input("Enter a lower bond and an upper bound divided a comma: ")

parsed = parse(user_input)

rand = random.randint(parsed['lower_bond'], parsed['upper_bound'])

print(rand)