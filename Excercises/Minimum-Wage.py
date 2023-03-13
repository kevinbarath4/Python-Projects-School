minWage = 22.5
hourlyWage = input("Enter your hourly wage: ")
		
# checking if user’s hourly wage is higher than the minimum wage

if not(float(hourlyWage) < minWage):		# need to convert user’s input from string to float	
	print('Your hourly pay is higher than the minimum wage, which is $' + str(minWage))
else:
	print('Your hourly pay is lower than or equal to the minimum wage, which is $' + str(minWage))



# To reduce repetition in the code, we could use the print() function once only, and make use of a variable in it:
'''
comparison = ""

if not (float(hourlyWage) <= minWage):		# need to convert user’s input from string to float	
	comparison = "higher then"
else:
    comparison = "lower than or equal to"

print('Your hourly pay is ' + comparison + ' the minimum wage, which is $' + str(minWage))
'''