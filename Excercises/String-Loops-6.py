print ("Enter an integer number greater than 0:")
num = int(input())
numOrig = num

sum = 0

# use a while loop to iterate until zero
while num > 0:
    sum += num
    num -= 1

print("The sum of the numbers 1 to", numOrig, "is", sum)