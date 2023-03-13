def greeting(name):
    print("Hello, " + name.strip().capitalize() + "!")  

# For ex: print function does not return a value:
print("Welcome!")   

# But input function returns a value, which we can then save into a variable:
firstName = input("Enter your first name: ")

# then we can use the return value of the input function (since we've saved it!) in code that follows
greeting(firstName)