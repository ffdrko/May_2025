# List variable for questions
questions = [
    "What is the capital city of France?",
    "Which planet is known as the Red Planet?",
    "What is 2 + 2?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the chemical symbol for water?",
    "Which animal is known as man's best friend?",
    "What is the largest continent by land area?",
    "In which year did the Titanic sink?",
    "What is the primary source of energy for Earth's climate system?",
    "Which programming language is known for its use in web development and has a logo with a blue 'JS'?"
]

# List variable for options
options = [
    ["A) Florida", "B) Paris", "C) Texas", "D) Narnia"],
    ["A) Jupiter", "B) Mars", "C) Venus", "D) Mercury"],
    ["A) 22", "B) 4", "C) 5", "D) 2"],
    ["A) William Shakespeare", "B) Charles Dickens", "C) Jane Austen", "D) Mark Twain"],
    ["A) CO2", "B) H2O", "C) O2", "D) NaCl"],
    ["A) Cat", "B) Dog", "C) Bird", "D) Fish"],
    ["A) Australia", "B) Africa", "C) Asia", "D) Europe"],
    ["A) 1912", "B) 1905", "C) 1920", "D) 1898"],
    ["A) The Moon", "B) The Sun", "C) Geothermal Heat", "D) Wind"],
    ["A) Python", "B) Java", "C) JavaScript", "D) C++"]
]

# List variable for answers
answers = [
    "B) Paris",
    "B) Mars",
    "B) 4",
    "A) William Shakespeare",
    "B) H2O",
    "B) Dog",
    "C) Asia",
    "A) 1912",
    "B) The Sun",
    "C) JavaScript"
]

cash = 10000
action = True

while action:
    for i in range(len(questions)):
        print(questions[i])
        for x in options[i]:
            print(x)
        user_answer = input("Enter your answer: ").upper().strip()
        for y in answers[i][0]:
            if user_answer == y[0]:
                print("You are right, you have earn the cash.")
                cash = cash * 2
            else:
                print("You are wrong buddy!!")
    break


print("You have won total ", cash, " taka.")