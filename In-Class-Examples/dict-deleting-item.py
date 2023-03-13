employee = {
    "firstName": "Joe",
    "lastName": "Black",    
    "fullTime": True,    
    "hourlyPay": 31.5
}

employee.pop("fullTime")
print(employee)

del employee["firstName"], employee["lastName"]
print(employee)

employee.clear()
print(employee)

del employee
print(employee)