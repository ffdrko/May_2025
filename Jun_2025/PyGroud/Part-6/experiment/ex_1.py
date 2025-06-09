import glob

myfiles = glob.glob("../files/*.txt")

for filepath in myfiles:
    with open(f'../files/{filepath}') as file:
        content = file.read()
    print(content)