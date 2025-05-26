file = open('files/whatever.txt', 'w')
file.write("Hello my name is fahim faisal deepto.")
file.close()

file = open('files/whatever.txt', 'r')
message =  file.read()
file.close()

print(message)