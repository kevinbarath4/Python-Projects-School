numbers = {'data1':100, 'data2':-514,'data3':2437, 'data4':-232}

total = 0       # the running total
count = 0       # number of positive numbers from the list

# looping through the values in the dictionary and adding up positive numbers only
for key in numbers:           # value refers to the key of the current dict item

    if numbers[key] > 0:

        total += numbers[key]
        count += 1  

# Another approach, using the dictionary values() method
# for value in numbers.values():
#   if value > 0:
#       total = total + value
#        total += value
#        count += 1 

print("The sum of the {} positive numbers found in the list is {}.". format(count, total))