import random
while True:
    player_answer = input("Roll the dice? (y/n): ").upper()
    if player_answer == "Y":
         x = random.randint(1,6)
         y = random.randint(1,6)
         cordinates = (x,y)
         print(cordinates)
    elif player_answer == "N":
     print("Thanks for playing!")
     break
    else:
     print("Invalid choice!")
    
     


