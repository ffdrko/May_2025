try:
    width = float(input("Enter the width: "))
    length = float(input("Enter the length: "))

    area = width * length
    if width == length:
        print("this is a square.")
        print(area)
    else:
         print(area)
except ValueError:
    print("Please enter a number.")