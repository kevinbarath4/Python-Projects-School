employees = {
    1: {'firstName': 'Joe', 'lastName': 'Black', 'employeeId': 123},
    2: {'firstName': 'Veronica', 'lastName': 'White', 'employeeId': 234},
    3: {'firstName': 'Ali', 'lastName': 'East', 'employeeId': 421}
}
# using dict keys to access values of a child dictionary
print(employees[1]['firstName'])        # [1] refers to the parent dict key; ['firstName'] refers to child dict key
print(employees[1]['lastName'])
print(employees[1]['employeeId'])