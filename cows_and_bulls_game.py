import random

def generate_secret():
    digits = random.sample(range(10),4) # pick 4 unique digits in a list
    return "".join(map(str, digits))  # join them into a "string number"

def calculate_cows_and_bulls(guess,secret):
    bulls = sum([1 for i in range(4) if guess[i]==secret[i]])
    cows =  sum([1 for i in range(4) if guess[i] in secret]) - bulls
    return cows, bulls

def main():
    secret = generate_secret()
    print('I have generated a 4-digit number with unique digits. Trt to guess it!')
    while True:
        try:
            guess = input('Guess: ') # συμφέρει να μη βάλω int() γιατί οι ακέραιοι δεν έχουν len()
            if guess.isdigit() and len(set(guess)) == 4:
                cows,bulls = calculate_cows_and_bulls(guess,secret)   
                print(f"{cows} cows and {bulls} bulls.")  
                if guess == secret:
                    print("Congratulations!You guessed the correct number!")
                    break 
            else:
                print(("Invalid guess.Please enter a 4-digit number with unique digits."))        
        except ValueError:
            print("Invalid guess.Please enter a 4-digit number with unique digits.")

if __name__ == "__main__":
    main()