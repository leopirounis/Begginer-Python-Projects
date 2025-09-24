import sys
from termcolor import colored, cprint

#Green and red colors 
print_red_on_red = lambda x: cprint(x, "red", "on_red")
print_green_on_green = lambda x: cprint(x, "green", "on_green")

#Quiz game programm

correct_answers = 0

answer_1 = input(
    "Question 1: What is the capital of France?\n A. Berlin \n B. Madrid \n C. Paris \n D. Rome \n Your answer: "
).upper()

if answer_1 == "C":
    print_green_on_green("Correct!")
    correct_answers += 1
else:
    print_red_on_red("Wrong! The correct answer is C.")

answer_2 = input(
    "Question 2: Which planet is known as the red planet?\n A. Earth \n B. Mars \n C. Jupiter \n D. Saturn \n Your answer: "
).upper()

if answer_2 == "B":
    print_green_on_green("Correct!")
    correct_answers += 1
else:
    print_red_on_red("Wrong! The correct answer is B.")
    
answer_3 = input(
    "Question 3: What is the largest ocean on Earth?\n A. Atlantic \n B. Indian \n C. Arctic  \n D. Pacific \n Your answer: "
).upper()

if answer_3 == "D":
    print_green_on_green("Correct!")
    correct_answers += 1
else:
    print_red_on_red("Wrong! The correct answer is D.")


print(f"\nQuiz over!Your final score is {correct_answers} out of 3.")