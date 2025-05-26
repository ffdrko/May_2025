countries = ["Albania", "Belgium", "Canada", "Ethiopia", "France"]
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

for content, files in zip(countries, filenames):
    file = open(f'../files/{files}', 'w')
    file.write(content)
    file.close()