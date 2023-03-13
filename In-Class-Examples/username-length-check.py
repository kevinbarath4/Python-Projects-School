userName = input("Please enter your username: ")

while len(userName) <= 3:
    userName = input("Your username is too short - it needs to be at least 4 characters long." 
        + "\n\nPlease enter a valid username: ")
else:
    print("Your username is", len(userName), "characters long. Thank you!")