def average(a=9, b=1):
    print("The average is ", (a+b)/2)


def average1(*num):
    sums = 0
    for i in num:
        sums += 1

    print("The average is ", sums/ len(num))


def name(**names):
    print("Hello,", names['fname']," your last name is", names['lname'])


# default
average()
# keyword
average(b=10, a=20)
# required - we must give te value
average(10, 10)
average1(1, 2, 3, 4, 5)
name(fname='Fahim', lname='Deepto')