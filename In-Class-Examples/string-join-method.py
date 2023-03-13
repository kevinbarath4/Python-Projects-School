numList = ['1', '2', '3', '4']  # the list with the values that we want to join into one string, 
                                # and also by using a string separator we specify

separator = " "			        # A blank space that will be used as the string separator when joining list elements
                                # It could be something other than a space - for ex: \n  \t  -  , - etc.

print(numList)			        # Output: ['1', '2', '3', '4’]
print(separator.join(numList))	# Output is: 1 2 3 4      - as one string
print(" ".join(numList))	    # Output is: 1 2 3 4      - as one string