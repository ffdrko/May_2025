import json

with open("files/question.json") as file:
    content = file.read()

data = json.loads(content)
score = 0

for ques in data:
    print(ques["question_text"])
    for index, option in enumerate(ques["options"]):
        print(f"{index + 1}-{option}")

    user_input = int(input("Enter your answer: "))
    ques["user_choice"] = user_input

for index, ques in enumerate(data):
    if ques["user_choice"] == ques["options"]:
        score = score + 1


print(f"Your score is {score}")
