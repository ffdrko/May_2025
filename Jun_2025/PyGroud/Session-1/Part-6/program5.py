contents = ["ALl carrots are to sliced longitudinally", "The carrost were reportedly sliced", "carrots test nice"]

files = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, files):
    file = open(f'files/{filename}', 'w')
    file.write(content)
    file.close()