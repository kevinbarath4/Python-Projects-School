# the initial data
dict1 = {1:8, 2:25}
dict2 = {3:5, 4:7}
dict3 = {5:33, 6:27}

dict1.update(dict2)
dict1.update(dict3)

print("The {} numbers stored are as follows:".format(len(dict1)))

for aKey in dict1.keys():
    print("#{0}: {1}".format(aKey, dict1[aKey]))