# Default arg

def average(a=9, b=1):
    print("The average is ", (a+b)/2)


average()
# keyword
average(b=5, a=25)


def suma(*num):
    sumq = 0
    for i in num:
        sumq += i
    print(sumq)


suma(1, 2, 5)