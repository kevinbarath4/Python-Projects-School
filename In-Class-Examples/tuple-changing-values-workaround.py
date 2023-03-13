x = ("apple", "banana", "cherry")   # starting with a tuple
y = list(x)                         # converting the tuple to a list amd saving it to a new variable

y[1] = "kiwi"                       # changing the list (the element at the 2nd position: “banana” to “kiwi”)
x = tuple(y)                        # converting the list back to the tuple, and reassigning it to the original variable.