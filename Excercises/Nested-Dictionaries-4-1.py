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

# -----------------------------------------------------------------------------------------------
# Function: getUserInfo
# Description: will prompt user to enter information needed to register for an account
# Parameters: none
# Return value: 
#   info - a list; the information user provided re: creating an account
# -----------------------------------------------------------------------------------------------
def getUserInfo(): 

    info = {}
    info["userName"] = input("Enter the username you would like to register for yourself: ")
    info["firstName"] = input("Enter your first name: ")
    info["lastName"] = input("Enter your last name: ")
    info["password"] = input("Enter your password:")

    return info
    
# ----------------------------------------------------------------------------------------------
# Function: createAccount
# Description: will use the information user provided to create a new account for the user
# Parameters: 
#       userInfo (list) - information provided by the user re: creating an account
# Return value: 
#       a Boolean value True if account is successfully created
# -----------------------------------------------------------------------------------------------
def createAccount(userInfo):    

    currentYear = datetime.now().year       # Getting the current year

    # adding a new user to the list of users
    users[userInfo['userName']] = {'firstName': userInfo['firstName'], 'lastName': userInfo['lastName'], 
        'password': userInfo['password'], 'memberSince': currentYear}

    return True
    
# ----------------------------------------------------------------------------------------------
# Function: displayProfileInfo
# Description: will use user's username to lookup and display on the console information 
#              from the user's account
# Parameters: 
#       userName (string) - username provided by the user
# Return value: none#       
# -----------------------------------------------------------------------------------------------
def displayProfileInfo(userName):

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

# -----------------------------------------------------------------------------------------------
# Main section of the program. It controls the flow of the program by calling different functions when/as needed, 
# passing the right arguments in function calls, and saving (and using) any return values. It also communicates with the user
# as needed (e.g. displays a welcome message, asks about the next step - ie. if wants to review the profile info, etc)

print("\nWelcome to '{}' website! You are on our 'Create Your Account' page.\n".format(websiteName))

infoFromUser = getUserInfo()                            # getting information that's needed for account registration from user
accountCreated = createAccount(infoFromUser)            # a new account is created for the user

# User can choose to view his/her profile info, or not
if(accountCreated):         
    reviewProfile = input("\nYour account has been created. Would you like to review your profile now? ('y'/'n') - ")

    if reviewProfile.strip().lower() == 'y':

        userName = input("Please enter your username: ")
        displayProfileInfo(userName)                    # outputs user profile info to the console

    elif reviewProfile.strip().lower() == 'n':

        print("Ok! Thank you for registering. Enjoy the show!")