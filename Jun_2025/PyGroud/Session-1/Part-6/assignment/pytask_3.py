file = open('../files/eassy.txt', 'r')
text = file.read()
file.close()

total_len = len(text)
print(total_len)