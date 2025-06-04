def water_state(temperature):
    if temperature <= FREEZING_POINT:
        return "solid"
    elif BOILING_POINT >temperature > FREEZING_POINT:
        return "Liquid"
    else:
        return "Gas"

FREEZING_POINT = 0
BOILING_POINT = 100

print(water_state(20))