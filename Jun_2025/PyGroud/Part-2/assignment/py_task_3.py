def format_filename():
    filename = "report.txt"
    filename = filename[:-4].capitalize()

    return filename

content = format_filename()
print(content)