# Name: WindowCalc.py
# Author: Biljana Ivkovic
# Date Created: September 11, 2021
# Last Updated: September 16, 2021

# Description:
# The program will get user input (in meters) for the desired width and length for a window. The valid values are 1 and 2.

# It will then calculate and display to the console the total length of wood required,
# in feet, and surface area of glass needed in square meters, for the production of either one or two windows, as per user's choice.
# The assumtion is that both windows (if 2 is indicated as the number of windows) are to be same in size.
#
# If user enters an invalid value (0, or > 2), it is handled by the program displaying an informational message to the user explaining 
# what went wrong.
numOfWindows = int(input("How many windows would you like to calculate the material for - 1 or 2? "))

if numOfWindows == 1 or numOfWindows == 2:

    # take the measurements from the user
    print("Enter window width (in meters):")
    widthInput = input()
    width = float(widthInput)

    print("Enter window height (in meters):")
    heightInput = input()
    height = float(heightInput)

    # do the calculation for 1 window or for 2 windows - depending on user's choice
    woodLength = 2 * (width + height)
    # multiply area * 2 to account for double panes of glass when calculating glass area
    glassArea = 2 * (width * height) 

    if numOfWindows == 2:    
        woodLength = 2 * woodLength
        glassArea = 2 * glassArea

    # converting wood to feet, since wood length is expressed in feet usually
    woodLength *= 3.25    
   
    print("The length of the wood needed for the", numOfWindows, "windows with the specified dimensions is", woodLength, "feet.")   
    print("The area of the glass needed is", glassArea, "square metres.")

elif numOfWindows == 0:   
    print("You have provided an invalid entry. Make sure the value you are providing is a number greater than zero.")

elif numOfWindows > 2:
    print("The system currently supports calculation for maximum 2 windows. Please come back later once the system is approved",
        "or start the program again and use it for calculating the material for 1 or 2 windows only.")