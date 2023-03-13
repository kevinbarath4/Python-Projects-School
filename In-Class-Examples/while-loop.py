#Printing i as long as i is less than 6; ie. the code in the loop will print 
# out the values 1 through 5

# 'i' is a 'control' variable; used to control execution of the loop
# it is assigned here 1 as its initial value
i = 1               
while i < 6:		# the condition determining/controlling when the loop stops
    
    # code inside the loop - runs once per each loop iteration
    print(i)		
    i += 1  	    # increments the value in i by 1 every time through the loop
                    # otherwise the loop would run forever

# code outside the loop runs once the loop stops
print("This is printed after the loop stops ...")