userName = input("Please enter your username (it needs to be at least 3 characters long): ")
print ("Your username is", len(userName), "characters long.")

if len(userName) <= 3:
    print("Your username is too short!")
else:
    print("Thank you!")