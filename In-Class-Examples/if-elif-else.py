aNumber = float(input("Enter a number greater than zero: "))

if aNumber < 0:
    print("The number you have entered is not greater than zero.")
elif aNumber > 100:
    print("The number you have entered is greater than 100.")
elif aNumber < 100:
    print("The number you have entered is smaller than 100.")
else:                                                   # runs if none of the conditions above evaluate to True...
    print("The number you have entered is 100.")