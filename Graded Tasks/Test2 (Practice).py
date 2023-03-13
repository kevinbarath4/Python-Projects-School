import math


    
def startmenu():
    
    whilegate = True
    
    print("Good day, Welcome to Kevin's Krazy Reviews! I will ask you for FIVE(5) resturant names and their rating!")
    
    resturantStats = {}
    
    i = 1
    
    while i < 6 and i > 0:
        
        resturantName = (input("Please enter a resturant (" + str(i) +") name: "))
        resturantRating = int(input("Please enter the resturant (" + str(i) + ") rating: "))
        
        if resturantRating < 6 and resturantRating > 0:
            resturantStats[i] = {"resturant": resturantName, "rating": resturantRating}
            i = i + 1
        else:
            print("Invalid Input, Please try again!")   
                     
    
    for num, resturant in resturantStats.items():
        print(f"{num}. {resturant['resturant']} (Rating: {resturant['rating']})")
    
    print ('\n')
    print("Not so Good Places to Eat!")
    print("--------------------------")
    for resturant in resturantStats.values():
        if resturant['rating'] == 2:
            print(f"{resturant['resturant']} \t\t\t**")
        elif resturant['rating'] == 1:
            print(f"{resturant['resturant']} \t\t\t*")
        
    print ("\n")
    print("Not so Good Places to Eat!")
    print("--------------------------")
    for resturant in resturantStats.values():
        if resturant['rating'] == 3:
            print(f"{resturant['resturant']} \t\t\t***")
        elif resturant['rating'] == 4:
            print(f"{resturant['resturant']} \t\t\t****")
        elif resturant['rating'] == 5:
            print(f"{resturant['resturant']} \t\t\t*****")

startmenu()
