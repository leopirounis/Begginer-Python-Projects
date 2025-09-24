import random
secret_number = random.randint(1,100)

while True:
   try: #to try thes na einai mesa sto loop gia na ksanastelnei minima enw exei ginei value error
     player_answer = int(input("Guess the number between 1 and 100: "))
     if player_answer < secret_number :
        print("Too low!")
     elif player_answer > secret_number:
        print("Too high!")
     else:
        print("Congratulations you guessed the number.")
        break
   except ValueError:
     print("Invalid Value")