employees = {
    123: {
        'FirstName': 'Joe', 
        'lastName': 'Black'
    },
    234: {
        'firstName': 'Veronica', 
        'lastName': 'White'
    },
    421: {
        'firstName': 'Ali', 
        'lastName': 'East'
    }
}

# The first loop returns all the keys and values in the nested dictionary employees. 
# Each of the keys is an employee id number, one per employee.
# Each of the values is the dictionary containing information of an employee. 
# We use the keys to unpack the information (employeeInfo) of each employee.

# The second loop goes through the information of each employee. 
# It returns all the keys for each of child dictionaries: firstName, lastName.
# we print the key of the person’s information and use each key to get & print value for that key.
for employeeId, employeeInfo in employees.items():
    print("\nEmployee ID: {}".format(employeeId))
    
    for key in employeeInfo:
        print("{0}: {1}".format(key, employeeInfo[key]))