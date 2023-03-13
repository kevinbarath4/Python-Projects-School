employee = { 
    "firstName":"Joe",
    "lastName":"Black"
}

# Updating the value for key 'firstName' from 'Joe' to 'Jane'
employee["firstName"] = "Jane"

# By using the update() method
employee.update({"firstName":"Jane", "lastName":"White"})
print(employee)