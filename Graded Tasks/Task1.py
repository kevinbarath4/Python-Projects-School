# Name: Task1
# Author: Kevin Barath
# Date Created: January 30th, 2023
# Date Last Modified: February 6th, 2023

# Purpose:
# Calculates the area of a triangle, circle or square using functions
#

import sys
import math


#function calculate the area of the triangle (isocesles triangle)
def trianglearea(uans3, uans4):
    areat = (uans3 * uans4) * float(0.5)
    return areat

#function to calculate the area of the rectangle
def rectanglearea(uans3, uans4):
    arear = (uans3 * uans4)
    return arear

#function to calculate the area of the circle
def circlearea(uans2):
    radius = uans2
    areac = float(3.14) * (radius * radius)
    return areac

#main body function for user inputs and calling other functions
def startmenu():
    
    #defining a non-changeable variabel for loop
    start = True
    
    #loop starts here
    while start == True:
        
        #asks the user for the input, the program gives the user all the option in a neat order vertically.
        uans1 = input("\nWhat would you like to calculate? \n\n1. Area of a Circle\n2. Area of a Rectangle\n3. Area of a Triangle\n4. Quit\n\nEnter your choice (1-4): ")
    
        #if statement to determine if the user chose a circle
        if uans1 == "1" :
            #gets parameters from the user for the circle
            uans2 = float(input("Please enter radius of the circle in Centimeters: "))
            #calls the circle area function to calculate
            areac = circlearea(uans2)
            #gives back the area of the circle after the function calculated and returned the users results
            print ("The area of the circle is " + str(areac) +" sqaured centimeters")
        
        #else if statement to determine both triangle and rectangle options since I worded the question to work for both input parameters
        elif uans1 == "2" or uans1 == "3":
            
            #asks for width and length of the triangle
            uans3 = float(input("Please Enter Width of the rectangle/triangle: "))
            uans4 = float(input("Please Enter Length of the rectangle/triangle: "))

            #branches into an if statement that will eventually call the rectangle area function
            if uans1 == "2":
                #calls the rectangle area function
                arear = rectanglearea(uans3, uans4)
                #gives back the area of the rectangle
                print("The area of the rectangle is " + str(arear) + " sqaured centimeters")

            #another branch for if the user chose the triangle
            if uans1 == "3":
                #calls the triangle area function (isoceles traingle calculation)
                areat = trianglearea(uans3, uans4)
                print("The area of the triangle is " + str(areat) + " sqaured centimeters")
                
        #whenever the user wants to quit with the program they can do so by entering 4 and therefore breaking the loop    
        elif uans1 == "4":
            break
        
        #any key not specified that is used will output an error and loop the program back to the start
        else:
            print("Invalid Input")

#calls the main branch for the program to work
startmenu()