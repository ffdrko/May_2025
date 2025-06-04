def parse(feet_inch):
    parts = feet_inch.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    return feet, inches