countries = ["Albania", "Belgium", "Canada", "Ethiopia", "France"]

for i in countries:
    file = open(f'../files/{i}.txt', 'w')
    file.write(i)
    file.close()