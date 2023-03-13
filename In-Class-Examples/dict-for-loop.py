employee = {
    "first Name": "Joe",
    "last Name": "Black",
    "employee Id": 1,
    "full Time": True,
    "hourly Pay": 31.5
}

print(employee)

# looping through the keys (default)
#for x in employee:
#    print(x)



# using the keys() method in a loop to return keys of the dictionary
#for x in employee.keys():
#    print(x)
    

#looping through dict by referring to each item’s key to get  its value
#for x in employee:

    #print(x)                #keys
#    print(employee[x])      #values



# the code print(employee[x]) in the loop replaces the lines below:
#print(employee["firstName"])
#print(employee["lastName"])
#print(employee["employeeId"])
#print(employee["fullTime"])
#print(employee["hourlyPay"])

# using the values() method in a loop to return values of the dictionary
#for x in employee.values():
#    print(x)

# using a loop to iterate through both keys and values, by using the items() method
for key, value in employee.items():       
    #print(key, value)                     # key refers to keys, value to values
    print("{0}: \t{1}".format(key, value))