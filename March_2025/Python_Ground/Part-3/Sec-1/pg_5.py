lst =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(lst)
lst.append(110)

print(lst)
lst.reverse()
print(lst)
print(lst.index(36))
print(lst.count(25))

ma = [1250, 2564, 1648]
lst.extend(ma)
print(lst)