# Let the breath lead the way!

a = "let the BREath,lead the,way     "

a = a.capitalize()      # Have the first letter of the sentence capitalized and the 
                        # rest of the letters in lower case. The new value is re-assigned to 
                        # the same variable

a = a.rstrip()                  # removes th white spaces at the end of the string.
a = a.replace(","," ")          # the commas are repplaced each with a white space
a = a.replace("way", "way!")    # adding an exclamation mark by using replace() method

print (len(a))          # printing the length of the new string
print(a)                # printing the string itself
