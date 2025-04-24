dic = {
    345: "Fahim",
    350: "Faisal",
    400: "Deepto"
}

print(dic)
print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(key)

for index, key in dic.items():
    print(f"{index}-{key}")