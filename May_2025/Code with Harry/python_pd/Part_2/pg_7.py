import time

current_time = int(time.strftime("%H"))
# current_time = 18
print(current_time)

if current_time < 12:
    print("Good morning!")
elif current_time == 12:
    print("Good noon!")
else:
    print("Good Afternoon")