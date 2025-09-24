import re

def main():
    password = input("Enter password: ")
    strength = 0
    if len(password) < 8 and re.search(r"[\d]", password):
        pass
    else:
        strength += 1  
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if  re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    if strength == 0:
        print("Password strength: Very Weak.")
    elif strength == 1:
        print("Password strength:  Weak.")
    elif strength == 2:
        print("Password strength:  Medium.")
    elif strength == 3:
        print("Password strength:  Strong.")
    elif strength == 4:
        print("Password strength:  Very Strong.")
           
if __name__ == "__main__":
    main()
