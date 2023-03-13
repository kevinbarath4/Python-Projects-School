def myCountry(name="Biljana", country="Canada"):    
    #print("My name is " + name + ". I am from " + country)
    print("My name is {0}. I am from {1}.".format(name, country))

# calling the function without passing an argument for country or name; 
# the default parameter values are used
myCountry()

# calling the function and passing an argument for country only
myCountry(country="Australia")

# calling the function and passing an argument for both parameter
myCountry(name="Veronica", country="Australia")