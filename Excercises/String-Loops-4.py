# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))

if (num % 2) == 0:                        # Using the modulus operator to check whether or not there is a remanider
   result = str(num) + " is an even number."  
else:
   result = str(num) + " is an odd number." 

print(result)