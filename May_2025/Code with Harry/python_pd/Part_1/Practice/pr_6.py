"""
Take a number n as input.
Print its square, cube, and square root (rounded to 2 decimal places).
"""
num = int(input("Enter a num: "))

print("Square", num ** 2)
print("cube", num ** 3)
print("Square root", round(num ** 0.5, 2))