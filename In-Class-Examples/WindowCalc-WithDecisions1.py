# Name: WindowCalc.py
# Author: Biljana Ivkovic
# Date Created: September 11, 2021
# Last Updated: September 16, 2021

# Description:
# The program will get user input (in meters) for the desired width and length for a window.

# It will then calculate and display to the console the total length of wood required,
# in feet, and surface area of glass needed in square meters, for the production of wither one or two windows, as per user's choice.
# The assumtion is that both windows (if 2 is indicated as the number of windows) are to be same in size.
numOfWindows = int(input("How many windows would you like to calculate the material for - 1 or 2? "))

print("Enter window width (in meters):")
widthInput = input()
width = float(widthInput)

print("Enter window height (in meters):")
heightInput = input()
height = float(heightInput)

woodLength = 2 * (width + height)

# multiply area * 2 to account for double panes of glass when calculating glass area
glassArea = 2 * (width * height)    

# Handling the case when user wants to calculate the materials for 2 rather than 1 window:
if numOfWindows == 2:    
    woodLength = 2 * woodLength
    glassArea = 2 * glassArea

# converting wood to feet, since wood length is expressed in feet usually
woodLength *= 3.25

print("The length of the wood needed for the", numOfWindows, "windows with the specified dimensions is", woodLength, "feet.")   
print("The area of the glass needed is", glassArea, "square metres.")