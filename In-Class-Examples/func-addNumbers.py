def addNumbers(num1, num2):
    sum = num1 + num2
    
    # the function returns the return value of the built in round function
    # (the result of the addition rounded to 2 decimal places)
    return round(sum, 2)
			
# Getting from user the numbers that are to be added together; the numbers are rounded to 2 decimal places
print("Enter two numbers that you would like to add up")
firstNumber = float(input("1st number: "))
secondNumber = float(input("2nd number: "))

# calling the function and saving its return value to a variable	
result = addNumbers(firstNumber,secondNumber)    

print("The sum of numbers", firstNumber, "and", secondNumber, "is", result)