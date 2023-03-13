# Looping through the letters in the word "College"
for aLetter in "College":	       

    if aLetter == 'l':
        continue            # stops the iteration when aLetter == 'l'

    elif aLetter == 'g':
        break               # breaks out of the loop when aLetter == 'g'.

    # printing the letter from the current iteration
    print(aLetter)          
else:
    print("All done!")	    # prints the text once the loop finishes iterating through the sequence
                            # does NOT run due to break statement running when aLetter == 'g'