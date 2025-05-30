with open('../files/story.txt') as f:
    content = f.read()

with open('../files/new_story.txt', 'w') as f:
    f.write(content)