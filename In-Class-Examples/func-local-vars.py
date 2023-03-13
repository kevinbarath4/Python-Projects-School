def myFunction():
    x = 300
    print("Value of x inside the function:", x)

myFunction()

# this will result in an error, since x is local to the function and as such 
# is not accessible  from outside the function
print("Value of x outside the function:", x)     