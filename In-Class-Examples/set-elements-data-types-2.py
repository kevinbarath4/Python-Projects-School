myList = ['C++','Python', 'C#', 'Java', 'PHP', "C#"]
myTuple = ('Photoshop', 'Illustrator')
mySet = {33, 44, 55}

theSet = {1, 5, 3, "hello", 8.34, 5, "hello", 5, 19, False}
print(theSet)       # unordered, duplicates removed

theSet.add(myTuple)         # this works
#theSet.add(myList)         # this does not work
#theSet.add(mySet)          # this does not work

print(theSet)