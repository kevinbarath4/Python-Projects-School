employee = {
    "firstName": "Joe",
    "lastName": "Black"
}

print(employee)

# this adds a new item, with the key 'employee' and a value of 1 for employee id.
employee["employeeId"] = 1

# this also adds a new item, since 'fullTime' key did not previously exist
employee.update({'fullTime': True, "email":"jwhite@conestogac.on.ca"})

print(employee)