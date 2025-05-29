email = input("Enter your email: ")

index_of_papaki = email.index("@")
username = email[:index_of_papaki]
domain = email[index_of_papaki + 1 : ]

print(f"You username is {username} and your domain is {domain}.")