# The script will check the numbers between 1300 and 2350 (both included), 
# and find and print those numbers which are exactly divisible both by 7 and by 5.

numberList = []                                     # initiating an empty list that will hold the numbers that match the conditions

for number in range(1300, 2351):

    if (number % 7 == 0) and (number % 5 == 0):     # checking if the number is divisible without remainder by 7 and by 5
        numberList.append(str(number))              # if it is, add it to the list. The variable is casted to string so that join() can 
                                                    # can be used later.

#separator = ", "                                   # Could use a variable to store the string separator value to use with join()
#print (separator.join(numberList))                 # and then use the variable in print();
                                                    # 
print (', '.join(numberList))                       # Or, here: using the separator string directly with the join() method - without 
                                                    # assigning it to a variable first
                                                    # 
                                                    # The join() method concatenates the elements of the list into one 
                                                    # string in which the elements are separated by ", "