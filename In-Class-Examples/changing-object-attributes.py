class Dog:
    species = "mammal"              
    
    def __init__(self, name, age):
        self.name = name            
        self.age = age

liam = Dog("Liam", 2)
jessi = Dog("Jessi", 3)

liam.age = 1
jessi.species = "mouse"

print("{} is {}, and {} is {}.".format(liam.name, liam.age, jessi.name, jessi.age))
print("{} is a {}.".format(liam.name, liam.species))
print("{} is a {}.".format(jessi.name, jessi.species))