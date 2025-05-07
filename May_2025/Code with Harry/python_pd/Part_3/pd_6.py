lst = [3, 5, 6]
print(lst)
print(type(lst))
print(lst[0])
print(lst[1])
print(lst[2])

lst_1 = [1, 2.5, False, 'Deepto']
print(lst_1)
print(type(lst_1))
print(lst_1[0])
print(lst_1[1])
print(lst_1[2])
print(lst_1[3])

print(lst_1[-3])

colors = ["Red", "Green", "Blue", "Yellow", "Green"]

if "Green" in colors:
    print("IS PRESENT")

COUNT = [1, 2, 3, 4, 5]
print(COUNT[0:])
print(COUNT[0::2])

lst_2 = [i for i in range(4)]
print(lst_2)
lst_3 = [i*i for i in range(5)]
print(lst_3)