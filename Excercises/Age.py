name = input("Enter your name:")
age = int(input("Enter your age:"))

if age >= 0 and age < 10 or  age > 12:
    print("Hello, " + name + "! There are no games available for " + str(age) 
        + " years olds at this time.")

elif age >= 10 and age <= 12:
    print("Welcome, " + name + "! To view the games available for " 
        + str(age) + " year olds, press the 'List the available games' button.") 

else:           # the age entered is less than 0
    print("Hello, " + name + "! You have entered an invalid age value. Re-run the program to try again.")