def splitFullName(fullName):

    # first removes any blank spaces and then splits the string by using the specified string separator
    nameParts = fullName.split(" ")         
    firstName = nameParts[0]                # accessing the first item in the list (first name)
    lastName = nameParts[1]                 # accessing the second item in the list (last name)

    # Returning multiple values, both first and last name. 
    # By default, the multiple values are returned as a Tuple
    return firstName, lastName

userName = input("Please enter your full name (first name and the last name):")

# Calling the function and saving its return values
# 1) Into two variables (one variable for each value returned)
fName, lName = splitFullName(userName)

print("First name is:", fName)
print("Last name is:", lName)

#fName, lName = splitFullName("Joe, Black")

# OR:
# 2) Into one variable. The variable references the Tuple object returned by the function
firstAndLastName = splitFullName(userName)
#print(firstAndLastName)

print("First name is:", firstAndLastName[0])
print("Last name is:", firstAndLastName[1])