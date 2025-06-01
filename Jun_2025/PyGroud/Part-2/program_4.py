def get_avg():
    with open('files/data.txt') as file:
        local_value = file.readlines()

    val = local_value[1:]
    new_val = [float(i.strip('\n')) for i in val]

    avg = sum(new_val) / len(new_val)
    return avg

average = get_avg()
print(average)
print(average)