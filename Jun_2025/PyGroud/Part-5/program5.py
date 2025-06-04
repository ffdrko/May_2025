import func
feet_inches =  input("Enter feet and inches: ")

def convert(feet, inches):
    meters = feet * 0.3028 + inches * 0.0254

    # return f"{feet} ft and {inches} inch is equal to {meters} m."
    return meters


feets, inches = func.parse(feet_inches)
result = convert(feets, inches)

if result < 1:
    print("kid is too small.")
else:
    print("Kid can use the slide")