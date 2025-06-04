def temp_check(temp):
    if temp > 25:
        return "Hot"
    elif 15 <= temp <= 25:
        return "Warm"
    else:
        return "Cold"

print(temp_check(15))