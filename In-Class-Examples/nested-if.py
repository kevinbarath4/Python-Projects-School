aNumber = float(input("Please enter a number: "))

if aNumber > 10:
    print("The number you have entered is greater than 10.")

    # the condition below is checked only if the condition 
    # in the 'parent' if statement evaluates to True
    if aNumber > 20:
        print(" ...and it is also greater than 20!")
    else:
        print(" ...and smaller than 20.")
else:
    print("The number you have entered is lower than or equal to 10.")