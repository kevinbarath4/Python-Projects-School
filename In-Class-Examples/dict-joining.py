dict1 = {"a":10, "b":8, "c":6}
dict2 = {"d":4, "c":2}

dict2.update(dict1)
print(dict2)        # Outputs: {'d': 4, 'c': 6, 'a': 10, 'b': 8}