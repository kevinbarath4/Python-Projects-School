
def forwardbackward(string):
    i = 0
    while i < len(string):
        print(string[i], end = "")
        i += 1
        print ("")

    i = len(string) - 1

    while i >= 0:
        print(string[i], end = "")
        i -= 1
        print("")
        

string = input("Please enter a string: ")
stringFinal = forwardbackward(string)
print(stringFinal)

