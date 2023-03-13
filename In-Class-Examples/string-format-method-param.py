#Using string format() method
item = "cake"
itemPrice = 3.98
quantity = 2

#using a zero-based index within placeholders to reference the position of the positional parameters to use
print("I would like to order {2} pieces of {0} at a price of ${1} per piece.".format(item, itemPrice, quantity))

print("I would like to order {} pieces of {} at a price of ${} per piece.".format(quantity, item, 
    itemPrice))