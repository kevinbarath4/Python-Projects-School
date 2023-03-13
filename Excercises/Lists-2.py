# The script removes from the intial list the colour values found at the positions 0, 4, and 5.

colours = ['Red', 'Green', 'White', 'Black', 'Yellow', 'Pink']  # initial list of colours
colours2 = []                                                   # creating an empty list that will at the end  
                                                                # hold the values from the initial list that are to be kept

i = 0 
while i < len(colours):
    
    #if i in [0,4,5]:
        #colours.remove(colours[i])              # neither of these 2 methods here will not do what we need, as once the item at 0th position ('Red') is removed from the list, 
        #colours.pop(i)                          # next time through the loop 'Yellow' will not be found at 4th but 3rd position, and
                                                 # 'Pink' will not be in the 5th but in 4th position.
     
    
    #so, instead of removing elements from the initial list, we will use the empty list by adding to it only the items that are to be kept
    if i not in [0,4,5]:                         # checking if the item - based on its position - is NOT one of those that need to be deleted, 
        colours2.append(colours[i])              # ie. the item is to be kept - so it's added to the second list
       
    i+=1                                        # incrementing the loop counter

print(colours2)                                 # printing the new list that has only the items that initially were not located in the 
                                                # positions 0, 4, 5. 