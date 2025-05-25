for i, j in enumerate("Hello"):
    print(i, j)

a = enumerate(["a", "b", "c"])
print(a)
print(list(a))

for i, j in [(0, 'a'), (1, 'b'), (2, 'c')]:
    print(i,j)