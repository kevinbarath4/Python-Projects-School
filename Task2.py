import sys
import math





def trianglearea(uans3, uans4):
    areat = round((uans3 * uans4) * float(0.5), 2)
    return areat

def triangleper(uans3, uans4):
    pert1 = uans3
    pert2 = round(math.sqrt(uans3*uans3 + uans4*uans4), 2)
    pert = (2 * pert2) + uans3
    return pert

def rectanglearea(uans3, uans4):
    arear = (uans3 * uans4)
    return arear

def rectangleper(uans3, uans4):
    perr = (uans3 * 2) + (uans4 * 2)
    return perr

def circlearea(uans2):
    radius = uans2
    areac = float(3.14) * (radius * radius)
    return areac

def circleper(uans2):
    perc = 2 * 3.14 * uans2
    return perc

def startmenu():
    
    start = True
    
    while start == True:
        
        uans1 = input("\nWhat would you like to calculate? \n\n1. Area and Perimeter of a Circle\n2. Area and Perimeter of a Rectangle\n3. Area and Perimeter of a Triangle\n4. Quit\n\nEnter your choice (1-4): ")
    
        if uans1 == "1" :
            uans2 = float(input("Please enter radius of the circle in Centimeters: "))
            areac = circlearea(uans2)
            print("The area of the circle is " + str(areac) +" sqaured centimeters")
            perc = circleper(uans2)
            print("The perimeter of the circle is " + str(perc) + " centimeters")
        
        elif uans1 == "2" or uans1 == "3":
            uans3 = float(input("Please Enter Width of the rectangle/triangle: "))
            uans4 = float(input("Please Enter Length/Height of the rectangle/triangle: "))

            if uans1 == "2":
                arear = rectanglearea(uans3, uans4)
                print("The area of the rectangle is " + str(arear) + " sqaured centimeters")
                perr = rectangleper(uans3, uans4)
                print("The perimeter of the rectangles is " + str(perr) + " centimeters")

            if uans1 == "3":
                areat = trianglearea(uans3, uans4)
                print("The area of the triangle is " + str(areat) + " sqaured centimeters")
                pert = triangleper(uans3, uans4)
                print("The perimeter of the triangle is: " + str(pert) + " centimeters")
                
            
        elif uans1 == "4":
            break
        
        else:
            print("Invalid Input")

startmenu()