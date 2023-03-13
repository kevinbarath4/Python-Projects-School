total = 0                  # Here total is a global variable

def addNumbers(num1, num2):
    total = num1 + num2     # Here total is a local variable. 
    
    print("Local (inside the function) total variable:", total)

addNumbers(10, 20)
print("Global (outside the function) total variable:", total)