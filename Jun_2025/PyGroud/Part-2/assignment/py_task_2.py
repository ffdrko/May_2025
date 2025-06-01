def get_max():
    grades = [9.6, 9.2, 9.7]
    max_num = max(grades)
    min_num = min(grades)

    return f"Max:{max_num}, Min:{min_num}"

text =  get_max()
print(text)