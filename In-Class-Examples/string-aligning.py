# formatting (aligning) output

theText = "Programming is fun!"
moreText = "More of the same"

# Printing the center aligned string with plus sign
# print ("Centered string with star: ")
print (theText.center(40, '+'))
print()

# Printing the left aligned string with "-" padding
# print ("Left-aligned string: ")
print (theText.ljust(40, '-'))
print (moreText.ljust(40, '-'))
print()

# Printing the right aligned stringwith "-" padding
# print ("Right-aligned string: ")
print (theText.rjust(40, '-'))
print (moreText.rjust(40, '-'))
print()