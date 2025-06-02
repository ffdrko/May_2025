feet_inches =  input("Enter feet and inches: ")

def convert(feet_inch):
    parts = feet_inch.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3028 + inches * 0.0254

    # return f"{feet} ft and {inches} inch is equal to {meters} m."
    return meters


result = convert(feet_inches)

if result < 1:
    print("kid is too small.")
else:
    print("Kid can use the slide")