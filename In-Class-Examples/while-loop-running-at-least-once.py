# Here, a loop is used to ask user to enter their age - and to do that repeatedly
# until the user enters a valid value (a number greater than 0)


# the condition: True will always be True, and so the loop runs at least once, and until we stop it 
# using break statement. Break statement runs conditionally - only if user's value is greater than 1
while True:		    
    age  = int(input("Please enter your age: "))
    if age >= 1:        # user's entry here is valid, so no need to keep asking for the information again
        break           # which is why we are breaking (exiting) the loop
    
    print("The program expects a number greater than 0.")

print("Got it! Thank you for providing your information.")