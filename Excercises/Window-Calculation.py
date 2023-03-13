width = float(input("Enter window width: "))   
height = float(input("Enter window height: "))                        

# multipying by 3.25 to convert wood length from meters to feet, since it is is expressed in feet usually
woodLength = 2 * (width + height) * 3.28

# multiply area * 2 to account for double panes
# of glass when calculating glass area
glassArea = 2 * (width * height)

print("The length of the wood needed is " + str(woodLength) + " feet.")   
print("The area of the glass needed is " + str(glassArea) + " square metres.")