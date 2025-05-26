file = open('../files/eassy.txt', 'r')
text = file.read()
file.close()

total_len = len(text)
print(f'This file contains {total_len} characters.')