file = open('../files/eassy.txt', 'r')
text = file.read()
file.close()

print(text.title())