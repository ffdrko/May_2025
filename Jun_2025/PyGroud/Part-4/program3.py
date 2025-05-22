filenames = ('1.Raw data.txt', '2.Reports.txt', '3.Presentation.txt')
print(type(filenames))
for file in filenames:
    print(file.replace('.','-', 1))