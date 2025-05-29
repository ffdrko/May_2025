length = float(input('Enter length: '))
width = float(input('Enter width: '))

perimeter = (length + width) * 2
area = length * width

print(f"Perimeter is {perimeter}")
print(f"area is {area}")

if 14 > perimeter > 8:
    print("OK")
else:
    print("not ok")