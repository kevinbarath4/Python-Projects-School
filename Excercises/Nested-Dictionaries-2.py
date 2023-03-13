# The program displays the list of users (accounts) registered on a website

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
print("\nThe list of website users...\n")

for user, userInfo in users.items(): 
    
    print("Username: {}".format(user))
    print("First Name: {}".format(userInfo['firstName']))
    print("Last Name: {}".format(userInfo['lastName']))
    print("Member since {}.".format(userInfo['memberSince']))
    print("{:^20}".format("-----"))