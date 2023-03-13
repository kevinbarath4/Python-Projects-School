# Creating a non-empty nested dictionary having same keys (in child dictionaries)
employees = {
    1: {'firstName': 'Joe', 'lastName': 'Black', 'employeeId': 123},
    2: {'firstName': 'Veronica', 'lastName': 'White', 'employeeId': 234},
    3: {'firstName': 'Ali', 'lastName': 'East', 'employeeId': 421}
}


























# Same code/data, only a different layout where child dicts items are coded one item per line
employees = {
    1: {
        'firstName': 'Joe', 
        'lastName': 'Black', 
        'employeeId': 123
    },
    2: {
        'firstName': 'Veronica', 
        'lastName': 'White', 
        'employeeId': 234
    },
    3: {
        'firstName': 'Ali', 
        'lastName': 'East', 
        'employeeId': 421
    }
} 

print(employees)



# Creting an empty nested dictionary
nestedDict = { 
    'dict1': { }, 
    'dict2': { }
}
