# The script sums the items in the provided list and prints the result

numbers = [4, -7, 34, 12, 86, 35]
sumNumbers = 0                                          # will hold the running total

for num in numbers:
    sumNumbers += num                                   # increasing the running total by the current number

print("The sum of the numbers is:", sumNumbers)         