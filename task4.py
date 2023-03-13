def convert_temperature(temp, unit):
    
    if unit.lower() == 'c':
        return (temp * 9/5) + 32
    elif unit.lower() == 'f':
        return (temp - 32) * 5/9
    else:
        return None  

def convert_speed(speed, unit):
   
    if unit.lower() == 'kmh':
        return speed / 1.609344
    elif unit.lower() == 'mph':
        return speed * 1.609344
    else:
        return None  

def startmenu():
    
    #gives the user an option to choose from either "temperature" or "speed"
    uOption = input("What do you want to convert?\n1) Temperature\n2) Speed\n> ")
    uOption = uOption.strip().lower()  # remove extra spaces and convert to lowercase
    
    #if statement for temperature conversion
    if uOption == '1':
        temp = float(input("Enter the temperature value to convert: "))
        temp_unit = input("Enter the current unit of temperature (C or F): ")
        temp_unit = temp_unit.strip().upper()  
        
        # Convert temperature
        converted_temp = convert_temperature(temp, temp_unit)
        if converted_temp is not None:
            print("{:.1f}{} is {:.1f}{}".format(temp, temp_unit, converted_temp, 'F' if temp_unit == 'C' else 'C'))
        else:
            print("Invalid input.")
    
    # Speed conversion
    elif uOption == '2':
        speed = float(input("Please enter the speed coefficient: "))
        speed_unit = input("Which unit of measurement do you want to use? (KMH or MPH): ")
        speed_unit = speed_unit.strip().upper()  # remove extra spaces and convert to uppercase
        
        # Convert speed
        converted_speed = convert_speed(speed, speed_unit)
        if converted_speed is not None:
            print("{:.1f}{} is {:.1f}{}".format(speed, speed_unit, converted_speed, 'MPH' if speed_unit == 'KMH' else 'KMH'))
        else:
            print("Invalid input")
    
    # Invalid input
    else:
        print("Invalid input")

startmenu()