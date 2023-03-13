# within the function definition both base and scope are in the scope, and therefore reachable by the function
def square(base):
    result = base ** 2          
    print("The square of {0} is {1}".format(base, result))

square(5)
print(base)             # 'base' is out of scope and not reachable
print(result)           # 'result' is out of scope and not reachable