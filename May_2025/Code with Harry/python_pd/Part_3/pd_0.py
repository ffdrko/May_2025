num = 5

match num:
    case 0:
        print('The number is Zero')
    case 5 if num % 2 == 1:
        print("The number is 5")
    case _:
        print("The number is ", num)