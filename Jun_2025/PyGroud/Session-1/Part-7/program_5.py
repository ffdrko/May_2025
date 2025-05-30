filenames = ['1.doc', '2.report', '3.presentation']

filenames = [i.replace('.', '-') + '.txt' for i in filenames]
print(filenames)