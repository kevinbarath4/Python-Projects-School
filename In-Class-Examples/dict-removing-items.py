employee = {
    "firstName":"Joe", "lastName":"Black", "fullTime": True
}
# 
employee.pop("fullTime")

del employee["firstName"], employee['lastName']

employee.clear()

del employee