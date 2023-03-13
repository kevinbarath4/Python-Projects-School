# Here, the goal is to print all numbers from 1 to 6, except 3.
# Note that the increment for i logically needs to come before the continue statement, otherwise 
# once i hits 3 the increment won't happen anymore because of the continue statement that
# stops the current iteration. 
# Also, i is now initialized with zero, due to the change of statement order.
i = 0   

while i < 6:  

    i += 1
    if i == 3:
        continue        # if i is 3 do nothing but continue to the next iteration

    print(i)            # will print out 1, 2, 4, 5, 6