languages = ["English", "German", "Bangla"]

for i in languages:
    with open(f'../files/{i}.txt', 'w') as file:
        file.write(i)