
#initializes a dictionary for the numbers and the cubed numbers
cubes = {}

#for loop that ranges from 1-11 but doesn not include 11, so it will calculate 10 and stop after that.
for num in range(1, 11):
    
    #arithmetic to cube the number
    cube = (num ** 3)
    #places the non-cubed number into a key with the "cube" variable being the variable for that key
    cubes[num] = cube

#prints all the arithmetic operations using a dictionairy for calculated numbers from 1-10 (not inclduing 11)
print(cubes)