# Pig dice game my solution ✅


import random

player_1_points = []
player_2_points = []

while True:
    while True:
        if sum(player_1_points) >= 100:
            print(f'Player 1 wins with {sum(player_1_points)} points.')
            break
        die = random.randint(1,6)
        sum1 = sum(player_1_points)
        sum2 = sum(player_2_points)
        if die == 1:
            print("\nYou scored 0 points this turn.")
            print(f'Current scores are: Player 1: {sum1},Player 2: {sum2}')
            break
        else:
            player_1_points.append(die)
            
        print(f''' 
    Player's 1's turn
    You rolled a {die}.''')
        roll_again = input("Roll again? (y/n): ").lower()
        if roll_again == "y":
            continue
        elif roll_again == "n":
            print(f'You scored {sum1} points this turn.')
            print(f'Current scores are: Player 1: {sum1},Player 2:{sum2} ')
            break
        
    while True:
        if sum(player_1_points) >= 100:
            break
        if sum(player_2_points) >= 100:
            print(f'Player 2 wins with {sum(player_2_points)} points.')   
            break 
        die = random.randint(1,6)
        sum1 = sum(player_1_points)
        sum2 = sum(player_2_points)
        if die == 1:
            print("\nYou scored 0 points this turn.")
            print(f'Current scores are: Player 1: {sum1},Player 2: {sum2}')
            break
        else:
            player_2_points.append(die)
            
        print(f''' 
    Player's 2's turn
    You rolled a {die}.''')
        roll_again = input("Roll again? (y/n): ").lower()
        if roll_again == "y":
            continue
        elif roll_again == "n":
            print(f'You scored {sum2} points this turn.')
            print(f'Current scores are: Player 1: {sum1},Player 2:{sum2} ')
            break
    if sum(player_1_points) >= 100:
        break
    if sum(player_2_points) >= 100:
        break
    