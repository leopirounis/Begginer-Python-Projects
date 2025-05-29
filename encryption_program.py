import random
import string

chars = " " + string.punctuation +string.digits + string.ascii_letters #oi xaraktires pou tha doulepsoume
chars = list(chars) # kanoume list tous xaraktires tis proigoumenis grammis
key = chars.copy()

random.shuffle(key)

# Encrypt part

plain_text = input("Enter text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Your original text : {plain_text}")
print(f"Your cypher text : {cipher_text}")



# Decrypt part

cipher_text = input("Enter text to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Your cypher text : {cipher_text}")
print(f"Your original text : {plain_text}")


