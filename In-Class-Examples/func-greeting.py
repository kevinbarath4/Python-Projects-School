# defining a function with 2 parameters
def greeting(firstName, lastName):     

    # the parameters (firstName and lastName) are used by the code inside function
	# - they can be used as any other variables             
    print("Hello, " + firstName + " " + lastName + "!")

# taking input from user
userFirstName = input("Enter your first name: ")   
userLastName = input("Enter your last name: ")

# calling the function and passing to it the values user entered as function arguments
greeting(userFirstName, userLastName)            