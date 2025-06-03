def get_nr_items(user_input):
    item = user_input.split(",")
    return len(item)

print(get_nr_items("john,lisa,teresa"))