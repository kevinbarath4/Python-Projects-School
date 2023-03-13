employees = {
    1: {'firstName': 'Joe', 'lastName': 'Black', 'employeeId': 123},
    2: {'firstName': 'Veronica', 'lastName': 'White', 'employeeId': 234},
    3: {'firstName': 'Ali', 'lastName': 'East', 'employeeId': 421},
    4: {'firstName': 'Anna', 'lastName': 'Zeu', 'employeeId': 452, 'fullTime': True}
}

# deletes the item with the key 'firstName' from the child dictionary 4
del employees[4]['firstName']

# deletes the item with the key 'fullTime' from the child dictionary 4
employees[4].pop('fullTime')

# deletes the items with the key 'employeeId' and 'lastName' from the child dictionary 4
del employees[4]['employeeId'], employees[4]['lastName']    
print(employees[4])