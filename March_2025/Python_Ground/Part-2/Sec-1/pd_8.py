num = int(input("Enter a number: "))

if num < 0:
    print("The number is negative.")
elif num >0:
    if num <= 10:
        print("The range of number is between 0 to 10")
    elif num <= 20:
        print("The range of number is between 11 to 20")
    else:
        print("The number is greater then 20")
else:
    print('The number is zero')