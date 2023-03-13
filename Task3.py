# Name: Task3
# Author: Kevin Barath
# Date Created: January 30th, 2023
# Date Last Modified: February 6th, 2023

# Purpose:
# asks user for username given the specific parameters of between 2-20 characters with atleast one digit present in the name.
#

import sys


# main function for program
def startmenu():
    #defining a non-changable variable so that the loop always runs
    start = True
    
    #loop starts
    while start == True:
        
        #asks user for a username giving them specific parameters
        unam1 = input("Please enter a username between 2-20 characters that contains at least one number from 0-9\n:")
        
        #if the user unput is greater than 20, it will give the (too long) error in the console and loop back
        if len(unam1) > 20 :
            print("Sorry this username is invalid!! (too long)")
        
        #if the user unput is greater than 20, it will give the (too short) error in the console and loop back
        elif len(unam1) < 2:
            print("Sorry this usernmae is invalid!! (too short)")
        
        #if the length of the user's string is withing the given parameters of 2 and 20 it will continue to the next nested if statements
        elif len(unam1) < 20 and len(unam1) > 2:

                #using any(...) describes for ANYTHING in the string and the char.isdigit states if a character is a digit. if all is true, than a valid username has been entered
              if any(char.isdigit() for char in unam1):
                  print("Great username!")
                #if the username doesn't have atleast one digit from 0-9, than it will be an invlaid username then looping back
              else:
                  print("Sorry this username is invalid!! (needs numbers)")
        
 #calls main function for the program           
startmenu()