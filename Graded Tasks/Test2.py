#Date Created: Monday March 13
#Name: Kevin Barath
#Course: PROG1783
#Date Last Modified: Monday March 13

#PURPOSE:
# The purpose of this program is to get a total of 10 inputs from the user. (2 inputs per hill)
# These inputs contain a name for the ski hill and the snowfall for the skill hill (total 10 inputs)
# The user will then be prompted with a question to require a certain amount of snowfall for their needs,
# Depending on their choosing, it will sort and selected the best ski hills fitting that criteria
def qualifier():
    qualifier = float(input("\nWhat is the least amount of snowfall preffered?: "))
    return qualifier
    
def allhills():
    
    for num, hill in skiHills.items():
        print(f"{num}. {hill['hill']} (Average Snowfall: {hill['average-snowfall']})")

def qualifiedHills(q1): 
    q1 = qualifier
    for hill in skiHills.values():
        if hill['average-snowfall'] > qualifier:
            print(f"{hill['hill']}. " + f"{hill['average-snowfall']}CM") 
    
skiHills = {}
    
increment = 1
    
while increment < 6 and increment > 0:
        
    hillName = (input("Please enter the name of the hill (" + str(increment) +"): "))
    averageSnow = round(float(input("Please enter the average snowfall for the hill (" + str(increment) + "): ")), 2)
        
    if averageSnow < 51 and averageSnow > 0:
        skiHills[increment] = {"hill": hillName, "average-snowfall": averageSnow}
        increment = increment + 1
    else:
        print("Invalid Input, Please try again!")

qualifier = qualifier()
print("\n")
print("All Ski Hills:")
allhills = allhills()

    
print ('\n')
print(" Ski Hills to Visit This Weekend:")
print("---------------------------------")
qualifiedHills = qualifiedHills(qualifier)
    
        
