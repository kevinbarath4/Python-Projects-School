import random
randomNum = random.randint(1,10)

print("The program has randomly generated an integer number between 1 and 10 (included). Try to guess what this number is.")
print("Enter your guess:")

guess = input()     # the user's first attempt is taken in

# The loop will run all the while the condition specified evaluates as True - that is, as long as the user's guess and the 
# number generated are different
# Once the condition stops evaluation to True (that is, once the user guesses correctly), the else construct in the loop will execute
while int(guess) != randomNum:  
    print("Incorrect! Try again:")
    guess = input()                 # after not guessing correctly the first time, 
                                    # the user is prompted to try again, until he gets the correct number.
else:
    print("You got it! The number generated is " + guess + ".")