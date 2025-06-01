def get_maximum():
    celsius = [14, 15.1, 12.3]
    maxi = max(celsius)
    return maxi

cels = get_maximum()
fahrenheit = cels * 1.8 + 32

print(fahrenheit)