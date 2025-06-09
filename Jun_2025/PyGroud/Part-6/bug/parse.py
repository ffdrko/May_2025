def parse(user_input):
    parts = user_input.split(",")

    lower_bond = int(parts[0])
    upper_bond = int(parts[1])

    return {"lower_bond": lower_bond, "upper_bound": upper_bond}

