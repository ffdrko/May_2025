#  Exercise 3

question_1 = ("Which country recently tested a hydrogen-based explosive device?\n"
              "A.United States\n"
              "B.China\n"
              "C.Russia\n"
              "D.India\n")
question_2 = ("Who won the top honors at the Laureus World Sports Awards 2025?\n"
              "A.Lionel Messi & Serena Williams\n"
              "B.Simone Biles & Mondo Duplantis\n"
              "C.Rafael Nadal & Katie Ledecky\n"
              "D.Novak Djokovic & Naomi Osaka\n")

question_3 = ("Which Indian minister inaugurated the country’s largest cruise terminal in Mumbai?\n"
              "A.Nitin Gadkari\n"
              "B.Sarbananda Sonowal\n"
              "C.Piyush Goyal\n"
              "D.Hardeep Singh Puri\n")

question_4 = ("What is the name of the newly discovered methane-producing archaea?\n"
              "A.Methanobrevibacter intestini\n"
              "B.Methanosarcina barkeri\n"
              "C.Methanococcus jannaschii\n"
              "D.Methanopyrus kandleri\n")

question_5 = ("Which country is advancing towards a bilateral trade agreement with India?\n"
              "A.United Kingdom\n"
              "B.United States\n"
              "C.Germany\n"
              "D.Japan\n")

question_6 = ("What major policy has the Reserve Bank of India (RBI) recently introduced?\n"
              "A.Allowing minors above 10 years to operate accounts independently\n"
              "B.Increasing repo rates by 2%\n"
              "C.Banning cryptocurrency transactions\n"
              "D.Introducing digital rupee for retail transactions\n")

question_7 = ("Which initiative aims to develop the world’s smallest semiconductors in India?\n"
              "A.NanoTech India\n"
              "B.Angstrom-Scale Semiconductor Development\n"
              "C.Bharat Chip Initiative\n"
              "D.Quantum Computing Mission\n")

question_8 = ("Which country has increased its wildlife conservation efforts by 6.6%?\n"
              "A.India\n"
              "B.United States\n"
              "C.GCC countries\n"
              "D.Australia\n")

question_9 = ("What is the name of India’s mission to provide tap water connections to rural households?\n"
              "A.Swachh Bharat Abhiyan\n"
              "B.Jal Jeevan Mission\n"
              "C.Namami Gange\n"
              "D.Har Ghar Jal Yojana\n")

question_10 = ("Which cricketers were named in Wisden’s Five Cricketers of the Year 2025?\n"
               "A.Virat Kohli & Steve Smith\n"
               "B.Gus Atkinson, Jamie Smith & Sophie Ecclestone\n"
               "C.Rohit Sharma & Pat Cummins\n"
               "D.Babar Azam & Joe Root\n")

prize = 0
question_list = [question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10]
answers = ["B", "B", "B", "A",  "B",  "A",  "B",  "C", "B",  "B"]

index = 0
while index < len(question_list):
    print(question_list[index])
    user_ans = input("Enter your option (A/B/C/D): ").strip().upper()

    if user_ans == answers[index]:
        print("Correct Answer!\n")
        prize += 100000
    else:
        print("Sorry, wrong answer.\n")

    index += 1  # Increment index manually



print("Your total prize money is", prize)