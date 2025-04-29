s1 = {1, 2, 3}
s2 = {3, 6, 7}

print(s1)

print(s1.union(s2))

s1.update(s2)
print(s1)

print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))

s1.add(10)
print(s1)

# s1.remove(55)
# print(s1)

s1.discard(55)
print(s1)

s1.pop()
print(s1)
#
# del s2
# print(s2)

s2.clear()
print(s2)