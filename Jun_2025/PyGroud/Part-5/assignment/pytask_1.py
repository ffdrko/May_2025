def water_state(temperature):
    if temperature <= 0:
        return "solid"
    elif 100 <temperature >= 0:
        return "Liquid"
    else:
        return "Gas"

print(water_state(75))