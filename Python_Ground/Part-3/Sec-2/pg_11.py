def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


num = fact(5)
print(f"The factorial of 10 is {num}")