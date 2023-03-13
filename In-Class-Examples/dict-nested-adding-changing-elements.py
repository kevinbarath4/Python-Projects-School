# initial nested dictionary
employees = {
    1: {'firstName': 'Joe', 'lastName': 'Black', 'employeeId': 123},
    2: {'firstName': 'Veronica', 'lastName': 'White', 'employeeId': 234},
    3: {'firstName': 'Ali', 'lastName': 'East', 'employeeId': 421}
}

# adding a new dictionary as an element to the parent dictionary
employees[4] = {}                   

# adding elements one at a time to the new child dictionary
employees[4]['firstName'] = 'Anna'  
employees[4]['lastName'] = 'Zeu'
employees[4]['employeeId'] = 452
employees[4]['fullTime'] = True     # It's ok to add additional elements to a child dictionary

# Adding a whole dictionary
employees[5] = {'firstName': 'Cara', 'lastName': 'Wilson', 'employeeId': 333}

print(employees)                # dictionary employees after adding dictionaries 4 and 5

# Updating a value in a child dictionary
employees[5]['firstName'] = "Caroline"
print(employees[5]['firstName'])