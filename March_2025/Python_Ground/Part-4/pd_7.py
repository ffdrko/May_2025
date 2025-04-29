def func1():
    try:
        lst = [1, 5, 6, 7]
        inp = int(input("Enter the index: "))
        print(lst[inp])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am always here.")


x = func1()
print(x)