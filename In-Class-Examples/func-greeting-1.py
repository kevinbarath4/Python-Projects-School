# function definition; the function accepts one parameter, name
def greeting(name):
    # the parameter is used by the code inside the function in the same way as any other variable 
    print("Hello, " + name.strip().capitalize() + "!")   

# taking input from user
userName = input("Enter your name: ")

# calling the function and passing to it as the argument the value user provided 
greeting(userName)            