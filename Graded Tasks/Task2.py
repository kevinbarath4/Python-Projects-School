# Name: Task2
# Author: Kevin Barath
# Date Created: January 30th, 2023
# Date Last Modified: February 6th, 2023

# Purpose:
# Calculates the area and perimeter of a triangle, circle or square using functions
#

import sys
import math


#fucntion to calculate the area of the triangle
def trianglearea(uans3, uans4):
    areat = round((uans3 * uans4) * float(0.5), 2)
    return areat

#function to calculate the perimeter of the triangle (isoceles)
def triangleper(uans3, uans4):
    pert1 = uans3
    pert2 = round(math.sqrt(uans3*uans3 + uans4*uans4), 2)
    pert = (2 * pert2) + uans3
    return pert

#fucntion to calculate the area of a rectangle
def rectanglearea(uans3, uans4):
    arear = (uans3 * uans4)
    return arear

#function to calculate the perimeter of a rectangle
def rectangleper(uans3, uans4):
    perr = (uans3 * 2) + (uans4 * 2)
    return perr

#function to calculate the area of a circle
def circlearea(uans2):
    radius = uans2
    areac = float(3.14) * (radius * radius)
    return areac

#function to calculate the perimeter of a circle
def circleper(uans2):
    perc = 2 * 3.14 * uans2
    return perc

#main start function for the menu
def startmenu():
    
    #defining a non-changeable variable for the the loop to always work
    start = True
    
    #start of the loop
    while start == True:
        
        #gets user input of what the "task1.py" has plus the perimeter of all the existing shapes and combines it
        uans1 = input("\nWhat would you like to calculate? \n\n1. Area and Perimeter of a Circle\n2. Area and Perimeter of a Rectangle\n3. Area and Perimeter of a Triangle\n4. Quit\n\nEnter your choice (1-4): ")

        #gets the user input and calls the function for calculating the perimeter AND calculating the 
        if uans1 == "1" :
            uans2 = float(input("Please enter radius of the circle in Centimeters: "))
            areac = circlearea(uans2)
            print("The area of the circle is " + str(areac) +" sqaured centimeters")
            perc = circleper(uans2)
            print("The perimeter of the circle is " + str(perc) + " centimeters")
        
        #same as "task1.py" for this else if statement
        elif uans1 == "2" or uans1 == "3":
            uans3 = float(input("Please Enter Width of the rectangle/triangle: "))
            uans4 = float(input("Please Enter Length/Height of the rectangle/triangle: "))

            #same as "task1.py" except the fact that it is now combining the perimeter with the final answer 
            if uans1 == "2":
                arear = rectanglearea(uans3, uans4)
                print("The area of the rectangle is " + str(arear) + " sqaured centimeters")
                perr = rectangleper(uans3, uans4)
                print("The perimeter of the rectangles is " + str(perr) + " centimeters")

            #same as "task1.py" except the fact that it is now combining the perimeter with the final answer
            if uans1 == "3":
                areat = trianglearea(uans3, uans4)
                print("The area of the triangle is " + str(areat) + " sqaured centimeters")
                pert = triangleper(uans3, uans4)
                print("The perimeter of the triangle is: " + str(pert) + " centimeters")
                
        #exits program using break
        elif uans1 == "4":
            break
        
        #catching user errors to loop program
        else:
            print("Invalid Input")

#calls the startmenu function to run the menu of the program
startmenu()