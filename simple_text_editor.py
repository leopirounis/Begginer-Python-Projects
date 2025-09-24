#Simple Text Editor my solution ✅

import os

#open(filename, "a") → Append mode
    #If the file does not exist, it creates it.
    #If the file already exists, it keeps the old content 
    # and adds new content at the end.
    
while True:
    filename = input("Enter the name of the text file (e.g., notes.txt): ")
    if ".txt" not in filename:
        print(f'{filename} could not be opened')
        break
    # Check if file exists
    if not os.path.exists(filename):
        print(f"{filename} does not exist. Creating a new file...")
        open(filename,'a').close()  # Create empty file
    text = input("Enter text to append: ")
    with open(filename,'a') as file:
        file.write(text + "\n")
        print("Text appended successfully.")
        break
    
          