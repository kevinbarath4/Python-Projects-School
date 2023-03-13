# The program simualates a registration of a user account on a website. 
# After the account is created (ie. user added to an existing list of users), the user can also review
# his/her profile info.
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
      
reviewProfile = input("\nYour account has been created. Would you like to review your profile now? ('y'/'n') - ")

if reviewProfile.strip().lower() == 'y':

    userName = input("Please enter your username: ")
    
    if userName.strip() not in users:
        print("The username you have provided does not exist.")
    else:
        for user, userInfo in users.items():
            if user.lower() == userName.strip().lower():

                print("Thank you! Here is your profile information...\n")
                print("Username: {}".format(user))
                print("First Name: {}".format(userInfo['firstName']))
                print("Last Name: {}".format(userInfo['lastName']))
                print("Member since {}.".format(userInfo['memberSince']))
                print()

                break    

elif reviewProfile.strip().lower() == 'n':

    print("Ok! Thank you for registering. Enjoy the show!")