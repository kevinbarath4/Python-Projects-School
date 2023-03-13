myList = ["C++", "Python", "C#", "PHP", "Java", "C#"]
myTuple = ("Photoshop", "Illustrator", "Photoshop")

#1
theSet = set(myList)
print (theSet)
theSet = set(myTuple)
print (theSet)

#2
fruit = {"apple", "banana", "cherry"}
fruit.add ('kiwi')
print("")
for deez in fruit:
    print(deez)

#3
if "apple" in fruit:
    print("\n'apple' is found!")
if "kiwi" not in fruit:
    print("'kiwi' is not in fruit")

#4
print("")
nonTropical = {"apple", "banana", "cherry"}
tropical = {"pineapple", "papaya"}

tropical.update(nonTropical)

#5
print(tropical)

#6
print("")
fruit.pop
print (fruit)

#6
print("")
fruit.clear()
print (fruit)