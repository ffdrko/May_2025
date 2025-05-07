lst = [i for i in range(1, 11)]
marks = lst.copy()
print(lst)

lst.append(11)
print(lst)
lst.reverse()
print(lst)
print(lst.index(5))
print(lst.count(5))
print(marks)

lst.extend(marks)
print(lst)