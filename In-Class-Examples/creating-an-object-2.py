class Dog:

    species = "mammal"              
    
    def __init__(self, name, age):

        self.name = name            
        self.age = age

liam = Dog("Liam", 2)
jessi = Dog("Jessi", 3)

# accessing and displaying data from the 2 dog objects
print("{} is {}, and {} is {}.".format(liam.name, liam.age, jessi.name, jessi.age))
print("{} is a {}.".format(liam.name, liam.species))
print("{} is a {}, too.".format(jessi.name, jessi.species))