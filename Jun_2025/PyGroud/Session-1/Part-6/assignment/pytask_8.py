user_input = input("Add a new member: ") + "\n"

file = open('../files/members.txt', 'r')
member = file.readlines()
file.close()

member.append(user_input)

file = open('../files/members.txt', 'w')
file.writelines(member)
file.close()