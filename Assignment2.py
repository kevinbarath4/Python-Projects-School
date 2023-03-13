# Name:                 Assignment2.py
# Author:               Kevin Barath
# Date Created:         Thursday, March 2, 2023
# Date Last Modified:   Tuesday, March 7, 2023

# Purpose of program:
#
# The purpose of this program is to have a user run thorugh an "online" ordering site
# The customer info, menu, student discount, delivery fee and delivery tip is something the user will have to chose from
# 
#
#

#calculates price of the order before any discounts or extra fees
def calculatePrice(price, quantity):
    return price * quantity

#function to calculate discount depending on how much the total order costs.
def calculateDiscount(total):
    
    # if order is less than 100 it is a 15% discount, if it is less than 500 but more than 100 it is a 20% discount, and then if its more than 500 it will be a 25% discount
    if total < 100:
        return 0.15
    elif total < 500 and total > 100:
        return 0.2
    else:
        return 0.25

#function for controlling the reciept and printing it based off of whatever is passed through "customer", "address", "order" and "student"
def receipt(customer, address, order, student):
    
    # For all of the error checking loops
    whilegate = True
    total = 0
    # Checks if the delivery will be true
    delivery = address['streetName'] != ""
    # Gives a value for how much delivery will be if it is true
    deliveryCharge = 5 if delivery else 0
    # Prints the menu using f strings from the "customer" dictionary found in the "startmenu" function
    print("\n\n==== Arnold's Amazing Eats ====")
    print("Delivery Address:")
    print(f"{address['streetNumber']} {address['streetName']} {address['unit']}")
    print(f"{address['city']}, {address['province']}, {address['postalCode']}")
    print(f"Delivery Instructions: {address['deliveryInstructions']}")
    print("Customer Information:")
    print(f"{customer['firstName']} {customer['lastName']}\n")
    print("Order:")
    print("Item\t\tAmt\tPrice\tTotal")
    print("-----\t\t---\t-----\t-----")
    
    # Calculates the total price for the order using the item, its price and quantity. it will then call the "calculatePrice" function 
    for item, price, quantity in order:
        itemTotal = calculatePrice(price, quantity)
        total += itemTotal
        #prints the item, quantity and price in the proper format of only 2 decimal points and spaces
        print(f"{item}\t\t{quantity}\t${price:.2f}\t${itemTotal:.2f}")
    
    # Checks if the user is a student
    if student:
        discount = total * 0.1
        total -= discount
        print(f"\n10% Student Savings\t\t\t\t-${discount:.2f}")
    discountRate = calculateDiscount(total)
    
    # Adds the discount rate to the total of the order indefinetly because the order will never not have an active discount
    if discountRate > 0:
        discount = total * discountRate
        total -= discount
        print(f"\nDiscount ({discountRate * 100}%)\t\t\t\t-${discount:.2f}")
        
    subtotal = total
    
    # if and elif statements to determine whether the delivery charge is waived or not (over 30 = yes)(under 30 = no)
    if delivery and total < 30:
        total += deliveryCharge
        print(f"\nDelivery Charge\t\t\t\t\t${deliveryCharge:.2f}")
    elif delivery:
        print(f"\nDelivery Charge\t\t\t\t\tWaived!")
    
    # Calculates taxes
    tax = total * 0.13
    total += tax
    
    # Prints and properly formats the subtotal and tax part of the reciept
    print(f"\nSub Total\t\t\t\t\t${subtotal:.2f}")
    print(f"Tax (13%)\t\t\t\t\t${tax:.2f}")
    
    # Error checking for the tip amount 
    while whilegate == True:
        tip = int(input("\nHow much % would you to tip the delivery driver? (10%, 15%, 20%, or 0%): "))
    
        # The if, elif and else statements are for checking how much the tip amount is and whether its an invalid amount or not
        if tip == 10:
            tipAmount = .10 * total
            break
        elif tip == 15:
            tipAmount = .15 * total
            break
        elif tip == 20: 
            tipAmount = .20 * total
            break
        elif tip == 0:
            tipAmount = 0 * total
            break
        else:
            print ("Invalid Tip Amount!")
    
    # Adds the tip amount to the total depending on how much they want to to tip
    total += tipAmount
    print(f"Tip\t\t\t\t\t\t${tipAmount:.2f}")
    
    print(f"\nTOTAL\t\t\t\t\t\t${total:.2f}")

#main menu function
def startmenu():
    
    whilegate = True
    # Welcome message to the user
    print("Welcome to Arnold's Amazing Eats!\nThe online ordering site has been revamped and faster than ever, with 4 more options on the menu and a new and aesthetic reciept design!\n")

    # Dictionary for the customer details
    customer = {
        'firstName': input("Please enter your first name: "),
        'lastName': input("Please enter your last name: "),
        'phoneNumber': input("Please enter your phone number: ")
    }

    # Dictionary for the customer address
    address = {
        'streetNumber': input("Please enter your street number: "),
        'streetName': input("Please enter your street name: "),
        'unit': input("Please enter your unit number (leave blank if none): "),
        'city': input("Please enter your city: "),
        'province': input("Please enter your province: "),
        'postalCode': input("Please enter your postal code: "),
        'deliveryInstructions': input("Please enter any special delivery instructions: ")
    }

    # Dictionary for the menu
    menu = {
        1: {'name': 'Pizza Pockets', 'price': 4.69},
        2: {'name': 'Lasagna', 'price': 12.99},
        3: {'name': 'Spaghetti & Meatballs', 'price': 15.99},
        4: {'name': 'Shepherds Pie', 'price': 14.99},
        5: {'name': 'Scalops & Lobster', 'price': 18.99},
        6: {'name': 'Arnolds Armadillo Pizza', 'price': 32.99},
    }
    
    # using a for loop to to print the menu by running through each key in the "menu" dictionary
    print("\nThe Menu For Arnolds Amazing Eats!:")
    for num, item in menu.items():
        print(f"{num}. {item['name']} (${item['price']:.2f})")

    # While loop for error checking
    while whilegate == True:
        
        mealChoice = int(input("Please enter the number of the meal you want to order (1 - 6): "))
        if mealChoice > 0 and mealChoice < 7:
            break
        elif mealChoice < 1 or mealChoice > 6:
            print("Invalid Meal Choice!\n")
    
    # Defines variables for the keys in the "menu" dictionary
    item = menu[mealChoice]['name']
    price = menu[mealChoice]['price']
    quantity = int(input("How many of those meals are being ordered today?: "))
    # Puts the variables into a list containing a tuple
    order = [(item, price, quantity)]
    # Formatting the order header of the reciept
    print("\nYour Order:")
    print("Item\t\tAmt\tPrice\tTotal")
    print("-----\t\t---\t-----\t-----")
    
    # Prints and properly formats the users order accorinding to the reciept
    for item, price, quantity in order:
        itemTotal = calculatePrice(price, quantity)
        print(f"{item}\t\t{quantity}\t${price:.2f}\t${itemTotal:.2f}")

    # Gets the user to answer whether they are a student or not. if they are, it translates the "Y" to a "y"
    student = input("Are you a student? (Y/N): ").lower() == "y"
    
    # Prints the full receipt
    receipt(customer, address, order, student)
    # Prints the final goodbye message
    print("Enjoy our new iteration of Arnolds Eats and the new menu items!")

#calls the "startmenu" function which acts as the main body of the program
startmenu()
