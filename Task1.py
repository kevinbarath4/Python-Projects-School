import sys
import math




def trianglearea(uans3, uans4):
    areat = (uans3 * uans4) * float(0.5)
    return areat

def rectanglearea(uans3, uans4):
    arear = (uans3 * uans4)
    return arear

def circlearea(uans2):
    radius = uans2
    areac = float(3.14) * (radius * radius)
    return areac

def startmenu():
    
    start = True
    
    while start == True:
        
        uans1 = input("\nWhat would you like to calculate? \n\n1. Area of a Circle\n2. Area of a Rectangle\n3. Area of a Triangle\n4. Quit\n\nEnter your choice (1-4): ")
    
        if uans1 == "1" :
            uans2 = float(input("Please enter radius of the circle in Centimeters: "))
            areac = circlearea(uans2)
            print ("The area of the circle is " + str(areac) +" sqaured centimeters")
        
        elif uans1 == "2" or uans1 == "3":
            uans3 = float(input("Please Enter Width of the rectangle/triangle: "))
            uans4 = float(input("Please Enter Length of the rectangle/triangle: "))

            if uans1 == "2":
                arear = rectanglearea(uans3, uans4)
                print("The area of the rectangle is " + str(arear) + " sqaured centimeters")

            if uans1 == "3":
                areat = trianglearea(uans3, uans4)
                print("The area of the triangle is " + str(areat) + " sqaured centimeters")
                
            
        elif uans1 == "4":
            break
        
        else:
            print("Invalid Input")

startmenu()