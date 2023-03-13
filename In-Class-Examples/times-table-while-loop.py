number = int(input("Enter a number from 1 to 10: "))
print()

# to build the times table, we need to repeat the calculation and the output
# - so that is what goes inside the loop
i = 1

while i < 11:
    print(i, "*", number, "=", i * number)
    i += 1