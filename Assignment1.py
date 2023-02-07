import sys
import math


##


def startmenu():
    start = True
    
    while start == True:
        
        print("Welcome to Amazing Eats II! We are a local food service and delivery buisness here in Waterloo!\nWe take orders over the phone and text\n")
        uEmail = input("What is your Email?: ")
        uAdress = input("What is your Delivery Adress?: ")
        uCity = input("What is your City?: ")
        uProvince = input("What is your Province?: ")
        uPostal = input("What is your Postal Code?: ")
        uInstruct = input("Instruction for delivery: ")
        uPhone = input("What is your Phone Number?: ")
        print("\n\nGreat! We currently only have two menu options which are:\n1. Lasagna (Serves 2) - 16.29$\n2. Pizza Pockets (Serves 1) - 4.69$")
        
        while start == True:
            uSelection = input("\nWhich one would you like (1 or 2): ")
            
            if uSelection == "1":
                uAmount1 = int(input("How many would you like?: "))
                uTotal1 = round(float(uAmount1 * 16.29), 2)
                print("The total is: " + str(uTotal1))
                
            elif uSelection == "2":
                uAmount2 = int(input("How many would you like?: "))
                uTotal2 = round(float(uAmount2 * 4.29,), 2)
                print("The total is: " + str(uTotal2))
            
            else:
                print("Invalid Input")
            
        
startmenu()