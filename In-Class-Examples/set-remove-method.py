fruit = {'apple', 'banana', 'cherry'}

removedItem = fruit.pop()
print("Removed item:", removedItem)

fruit.discard("kiwi")        # this will not raise an exception, will not stop the program
fruit.remove("kiwi")         # this will raise an exception and stop the program

fruit.clear()
del fruit

print(fruit) 