import sys

while True:
    username = input("Enter a username between 2 and 20 characters with at least 1 number from 0 to 9: ")
    if len(username) >= 2 and len(username) <= 20 and any(char.isdigit() for char in username):
        print("Valid username")
        break
    else:
        print("Invalid username, try again.")