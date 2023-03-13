import random                           # Importing module random so that we can call its function, random.randint()

total = 0                               # Initalizing the variable (with the value of 0) so that it can be referenced in the loop
                                        # It will be used for calculating the running total, the sum of the multiplication results.

for x in range(10):                         # The loop will run 10 times, therefore 10 random numbers will be generated
    randomNum = random.randint(1,100)       # Generating a random number in the range 1 - 100, and saving it in a variable
    aResult = randomNum * 5
                     
    print (randomNum, "x 5 =", aResult)     # the text that will be printed to the screen, re: the individual multiplications
    total += aResult                        # incrementing the running sum of individual multiplication result by the current result

print ("\nThe sum of the individual multiplication results is:", total)    # Printing out the sum of the multiplication results.