files_name = ['a.txt', 'b.txt', 'c.txt']

for i in files_name:
    file = open(f'task_files/{i}', 'r')
    print(file.read())
    file.close()