#x = 8
#y = "My favourite number is "
#print(y + x)                      # this will result in an error

x = 8
y = "My favourite number is "
z = "!"

# this will work fine as both values are now strings
print(y + str(x))               # Output:  My favourite number is 8   
print()          

x = 8
y = "My favourite number is"    # notice that the blank space at the end is not needed

# this will work fine without casting x to str
print(y, x, z)                    # Output:  My favourite number is 8