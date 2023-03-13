def printMe(name, age):
    print("My name is", name, "and I am", age, "old.")

userFirstName = input("Please enter your first name: ")
userAge = int(input("Please enter your age: "))

printMe(age=userAge, name=userFirstName)