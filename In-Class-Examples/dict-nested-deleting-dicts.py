employees = {
    1: {'firstName': 'Joe', 'lastName': 'Black', 'employeeId': 123},
    2: {'firstName': 'Veronica', 'lastName': 'White', 'employeeId': 234},
    3: {'firstName': 'Ali', 'lastName': 'East', 'employeeId': 421},
    4: {'firstName': 'Anna', 'lastName': 'Zeu', 'employeeId': 452, 'fullTime': True}
}

employees.pop(1)                  # deletes the item associated with key 1
del employees[2]                  # deletes the item associated with key 2
del employees[3], employees[4]    # deletes the items associated with keys 3 & 4

print(employees)