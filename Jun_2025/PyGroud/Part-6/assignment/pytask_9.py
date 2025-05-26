filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for i in filenames:
    file = open(f"task_files/{i}", 'w')
    file.write("Hello")
    file.close()