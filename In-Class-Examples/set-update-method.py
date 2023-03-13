nonTropical = {'apple', 'banana', 'cherry'}
tropical = {"pinaapple", "papaya"}

#tropical.update(nonTropical)       # this updates the set tropical

fruit = tropical.union(nonTropical) # this does not update tropical set, but returns a new set, which is saved to fruit

#print(nonTropical)
#print(tropical)
print(fruit)