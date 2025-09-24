import random
import string

def ps_generator(length,upp_answer,numbers_answer,sp_ch_answer):
    if length < (upp_answer + numbers_answer + sp_ch_answer):
        raise ValueError("Password length is too short for the specified criteria.")
    
    password = ''
    
    #It will create a string in the order we add our characters (they are not shuffled!) 
    if upp_answer:
        password += random.choice(string.ascii_uppercase)
    if numbers_answer:
        password += random.choice(string.digits)
    if sp_ch_answer:
        password += random.choice(string.punctuation)
    
    # Fill the remaining length with any allowed characters
    remaining_characters = string.ascii_lowercase
    if upp_answer:
        remaining_characters += string.ascii_uppercase #without random.choice() because we want all the characters                                                  
    if numbers_answer:                                 #to be in the remaining_charcters and then shuffle 
        remaining_characters += string.digits         # (otherwise it choose-save only 1 char)
    if sp_ch_answer:
        remaining_characters += string.punctuation
        
    for _ in range(length - len(password)):
        password += random.choice(remaining_characters)
        
    #We make a list,shuffle it and return a shuffled string without spaces
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

def main():
    try:
        length = int(input("Enter a password length: "))
        upp_answer = input("Include uppercase? (y/n): ").upper() == "Y"
        numbers_answer = input("Include numbers? (y/n): ").upper() == "Y"
        sp_ch_answer = input("Include special charecters? (y/n): ").upper() == "Y"
        
        password = ps_generator(length,upp_answer,numbers_answer,sp_ch_answer)
        print(password)
        
    except ValueError : #you write that way to enable the print of the raise otherwise it wont be printed
        print("Invalid length")

if __name__ == "__main__":
    main()
