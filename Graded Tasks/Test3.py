import os

def startmenu():
    
    #Gets an input from the user to see how many passengers they would liked to document/record
    passengerRecord = int(input("How many passenger records would you like to enter?: "))
    
    #initiates an empty list that will contain the passenger information later
    passengers = []
    
    # for loop to go through the amount of times the user wants it to
    for i in range(passengerRecord):
        
        #gets all user information
        print(f"\nPASSENGER: {i+1}")
        flightId = input("What is the ID of your flight?: ")
        airlineName = input("What is the name of the airline?: ")
        locationFrom = input("Where is the location starting from?: ")
        locationTo = input("Where is the ending destination?: ")
        flightDuration = input("How long was/is the flight?: ")
        clientId = input("What is your client ID?: ")
        clientName = input("What is your name?: ")
        clientTicketNumber = input("What is your ticket number?: ")
    
        #dictionary for all the passenger information
        passengersDictionary = {
            
            "FlightID": flightId,
            "AirlineName": airlineName,
            "LocationFrom": locationFrom,
            "LocationTo": locationTo,
            "FlightDuration": flightDuration,
            "ClientID": clientId,
            "ClientName": clientName,
            "ClientTicketNumber": clientTicketNumber,
        }
            
        #adds the passengersDictionary to the passengers list
        passengers.append(passengersDictionary)
    
    #creates a working directory with the specified name
    filePath = os.path.join(os.getcwd(), "Passengers.txt")
    
    # opens the variable "filepath" as "p" for passsengers
    with open(filePath, "w") as p:
        
        #formats and writes all data to the specified file
        for i, passenger in enumerate(passengers):
            passenger = ", ".join(passenger.values())
            p.write(f"\nPASSENGER {i+1}: {passenger}")
    
    #final print statement for the user to confirm it is in the file
    print(f"Passenger data/information has been stored to {filePath}")
        
        

startmenu()