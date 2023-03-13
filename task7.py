
#creates a dictionary for the users info
uInfo = {}
#asking the user for their first name and assigning it to key "uName"
uInfo['uName'] = input("Please enter your first name: ")
#same thing as before but for last name
uInfo['uNameLast'] = input("Please enter your last name: ")
#same thing before but for their conestoga student ID/Number
uInfo['uStudentNumber'] = input("Please enter your Conestoga Student number: ")
#dictionary contating all of the given courses
courses = {'PROG1783': 'IT Programming Fundamentals', 'INFO1385': 'Network Infrastructure',
           'PROG2267': 'Advanced IT Programming ', 'INFO1250': 'Computer System Fundamentals'}

#This is the starting print statement for the eligible course. It will then run down to the "for" statement and look like it merged
print("\nThe courses you are eligible for are: ")
#goes through ALL of the keys in the "courses" dictionary and prints them out
for code, name in courses.items():
    print(f'{code}: {name}')

#asks the user for the course CODES separated by commas
uCourses = input("\nEnter the course codes for each course you want to register for, separated by commas: ")
uCoursesList = uCourses.split(",")

#creates a list for the selected courses by the user
uCoursesInfo = []

#adds every course the user wanted into the "uCoursesInfo"
for code in uCoursesList:
    uCoursesInfo.append((code, courses[code]))

#prints the "uInfo" list thats at the start of the program with all the user information
print(f'\nStudent information: {uInfo["uName"]} {uInfo["uNameLast"]}, Student Number: {uInfo["uStudentNumber"]}')
print("You selected these courses: ")

#prints all the selected courses the user chose
for code, name in uCoursesInfo:
    print(f'{name}: {code}')