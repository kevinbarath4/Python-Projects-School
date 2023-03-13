# Program to sort integers into prime or non-prime lists

# Define a function to check if a number is prime
def prime(uInput):
    if uInput < 2:
        return False
    for i in range(2, int(uInput**(0.5))+1):
        if uInput % i == 0:
            return False
    return True

# Ask user to input a list of integers
uInput = input("Please enter a comma-separated list of whole numbers: ")

# Convert input string to a list of integers
uInputList = [int(x) for x in uInput.split(",")]

# Initialize empty lists for prime and non-prime numbers
primeNumbers = []
primeNumbersNot = []

# loops through the users list to check if they are prime or not prime numbers using the "prime" fucntion
for num in uInputList:
    if prime(uInput):
        primeNumbers.append(uInput)
    else:
        primeNumbersNot.append(uInput)

# Print the sorted lists of prime and non-prime numbers
print("The Prime numbers are:", ", ".join(str(x) for x in primeNumbersNot))
print("The Non-prime numbers are:", ", ".join(str(x) for x in primeNumbersNot))