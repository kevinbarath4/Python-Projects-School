class Dog:
    species = "mammal"              
    
    def __init__(self, name, age):
        self.name = name            
        self.age = age

    def speak(self, sound):
        print("{} says {}".format(self.name, sound))

liam = Dog("Liam", 2)
liam.speak("Gruff gruff!")