import random

words = ['python','elephant','coding','astronaut','jazz','metal','mathematics']

def display_hint(hint):
    print(" ".join(hint))
         
def check_the_letter(letter,secret_word,hint,wrong_guesses,guessed_letters):
    if letter in secret_word:
        if letter not in guessed_letters:
            for i in range(len(secret_word)):
                if secret_word[i] == letter :
                    hint[i] = letter
                    print("Good guess!")
    else:
        if letter not in guessed_letters:
            wrong_guesses += 1
            print("Wrong guess!")
    return hint,wrong_guesses

def main():
    secret_word = random.choice(words)
    hint = ["_"] * len(secret_word)
    wrong_guesses = 0
    guessed_letters = set()
    while True:
        display_hint(hint)
        letter = input('Enter a letter: ').lower()
        
        #Enter valid letter
        if len(letter) != 1:
            print("❌ Please enter only ONE character.")
        elif not letter.isalpha():
            print("❌ Please enter a LETTER (a-z).")
            
        #Check the letter ,and update the hint,wrong_guesses in the main loop (NOW the letter isn’t in guessed_letters yet)
        hint, wrong_guesses = check_the_letter(letter, secret_word, hint, wrong_guesses, guessed_letters)
        
        #Add letter after checking th letter
        if letter in guessed_letters:
            print(f"{letter} has already been guessed!")
        else:
            guessed_letters.add(letter)
            
        #Check if win or lose
        if "_" not in hint:
            print(secret_word)
            print("You won!") 
            break   
        elif wrong_guesses == 6 :
            print(f"Game over! You lost! The word was: {secret_word}")
            break
        
if __name__ == "__main__":
    main()

