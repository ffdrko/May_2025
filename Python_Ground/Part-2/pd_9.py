import time

timestamp = int(time.strftime("%H"))

if timestamp < 12:
    print("Good Morning Sir!")
elif timestamp == 12:
    print("Good noon Sir!")
else:
    print("Good After noon Sir!")