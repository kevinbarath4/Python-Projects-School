# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.
# Run the program again - until the user decides he/she wants to exit. If decides to exit, display "Goodbye!" message.

runAgain = "y"                              #default value, used in the while condition, and later when taking user's response re:
                                            #whether or not wants to continue running the script.

while runAgain.lower() == "y":              # the condition; note: the value in runAgain is converted to lower case so that
                                            # the comparisson works as expected (ie. both 'y' and 'Y' are valid)    
    num = int(input("Enter a number: "))

    if (num % 2) == 0:                      # Using the modulus operator to check whether or not there is a remanider
        result = str(num) + " is an even number."  
    else:
        result = str(num) + " is an odd number."

    print(result)                           # Print the result to the user   

    # in the while loop: display question to user amd receive the response on whether or not he/she wants to run the script again
    # If user provides an answer different than 'y' and 'n', he/she is prompted again, to answer the same question
    answer = ""    
    while answer.lower() != 'y' and answer.lower() != 'n':      # again, the value in answer is converted to lower case so that
                                                                # the comparisson works as expected - as all: 'y', "Y', 'n', 'N' are valid values"

        print("Run the program again? (y/Y = yes, n/N = no) ")
        answer = input()        #ask user whether to continue or not
    else:   
        runAgain = answer       #if valid value, assign it to the variable used in the outer loop

else:
    print ("Goodbye!")          # when the user enters 'n' (or 'N"), for 'No', the script ends.