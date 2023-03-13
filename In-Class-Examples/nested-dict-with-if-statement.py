# the program allows user to update job position for one of the employees for which information is loaded when the code runs (in a dict)

# employees info on 'file'
employees = {
    123: {'First Name': 'Joe', 'Last Name': 'Black','Job position': 'Production Worker'},
    234: {'First Name': 'Veronica', 'Last Name': 'White','Job position': 'Production Worker'},
    421: {'First Name': 'Ali', 'Last Name': 'East','Job position': 'Manager'}
}

print("Hi! Use this program to update job position of an employee.")

# asking the user to enter information needed for the update
employeeToPromote = int(input("\nPlease enter the employee id of the employee whose job position you would like to update: "))
newPosition = input("Please enter the new job position for the employee: ")

for employeeId, employeeInfo in employees.items():
    
    # Using the employeee id user entered to look up the employee whose job position is to be updated
    # This is done by finding a match for the employee id value that user entered, among the existing employee IDs (in the dictionary) 
    if employeeToPromote == employeeId:
        
        # we now know who is the employee to update (based on their id) - and we use the id to make the update happen 
        employees[employeeToPromote]['Job position'] = newPosition

        print("\nJob position of the employee with employee id {} has been changed to '{}'."
            "\nHere is the employees's current info on file: \n".format(employeeId, newPosition))
        
        # The next few lines display full info for the selected employee, including the new job position info.
        print("Employee Id: \t{0} ".format(employeeId))
    
        for key in employeeInfo:
            print("{0}: \t{1}".format(key, employeeInfo[key]))

        # we can break out of the loop, since the match has been found
        break