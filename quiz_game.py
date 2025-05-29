questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: " ,
             "What is the most abundant gas in Earth's atmosphere?:  ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")
options = (("A. 116","B. 117","C. 118", "D. 119"),
           ("A. Whale","B. Crocodile", "C. Elephant","D. Ostrich"),
           ("A. Nitrogent", "B. Oxygen", "C. Carbon-Dioxide","D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Earth","D. Mars"))
answers = ("C","D","A","A","B")
guesses =[]
score= 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess_input = input("Enter (A,B,C,D): ").upper()
    if guess_input == answers[question_num]:
     print("Correct!")
     score += 1
    else:
     print(f"Wrong! The correct answer is {answers[question_num]}")
    question_num +=1
    guesses.append(guess_input)
print("-------------------------")
print("        RESULTS          ")
print("-------------------------")
print("Guesses: ", end = "")
for guess in guesses:
    print(guess, end = " ")
print() #gia na vgei to epomeno print apo katw
print("Answers: ",end = "")
for answer in answers:
    print(answer, end = " ")
score = int(score / len(questions) * 100)
print() # gia na vgei to epomeno print apo katw
print(f"Your score is {score} %")   