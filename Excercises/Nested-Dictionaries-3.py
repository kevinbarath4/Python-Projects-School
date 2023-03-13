# The program simualates a registration of a user account on a website.
from datetime import datetime

websiteName = "The World Is Yours To Share It"

# The default list of user accounts. In the real world this information is often pulled from a database.
users = {
    'BFraiser': {
        'firstName': 'Bob',
        'lastName': 'Fraiser',
        'password': '12345Ss',
        'memberSince': 2002
    }, 
    'JHaniston': {
        'firstName': 'Joanna',
        'lastName': 'Haniston',
        'password': 'K22755p',
        'memberSince': 1993
    }
 }

# Display a welcome/intro message and ask user to create an account for him/herself by entering the required information
print("\nWelcome to '{}' website! You are on our 'Create Your Account' page.".format(websiteName))

userName = input("\nEnter the username you would like to register for yourself: ")
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
password = input("Enter your password:")

currentYear = datetime.now().year       # Getting the current year
users[userName] = {'firstName': firstName, 'lastName': lastName, 'password': password, 'memberSince': currentYear}
      
print("\nYour account has been created. Thank you for registering!")