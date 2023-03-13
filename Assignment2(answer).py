# t2-practice-solution.py
# Author: 
# Date Created:
# Last Modified:
# Purpose: 
#  The program asks user to enter name and rating for 5 restaurants, then groups the restaurants
# by rating into 'good places to eat' and 'not so good places to eat'. This information is then
# displayed to the user.


# Function: getUserRatings()
# Description: Collects a name and a rating for five restaurants from user
# Param: None
# Return value:
#       restourantRatings (dictionary) - information collected from user
def getUserRatings():

    restourantRatings = {}
    print("Please enter name and rating of five restaurants.")   

    i = 1
    while i <= 5:        
        print("\nRestaurant #{}:".format(i))

        name = input("- Enter the name of the place: ")
        rating = int(input("- Enter the rating: " ))

        while True:   
            if not(rating > 0 and rating <= 5):
                rating = int(input("Invalid value: enter a whole number from 1 to 5, included: "))
            else:
                restourantRatings[name] = rating
                break
        i += 1

    return restourantRatings


# Function: groupPlacesByRating()
# Description: Sorts through the ratings info provided and figures out which of them are in the rating range provided.
# Param: 
#       allRatings (dictionary) - the rating info for all the restaurants 
#       minRating (int)         - minimum rating
#       maxRating (int)         - maximum rating
#
# Return value:
#       placesByRating (dictionary) - a dictionary containing info on restaurants (name and rating) that are in the rating range provided
def groupPlacesByRating(allRatings, minRating, maxRating):
    
    placesByRating = {}

    for aRestaurant, aRating in allRatings.items():
        if aRating >= minRating and aRating <= maxRating:
            placesByRating[aRestaurant] = aRating
    
    return placesByRating

# Function: displayRatings()
# Description: Displays information re: good or bad places to eat.
#
# Param: 
#       title (string)          - The title to be displayed
#       ratings (dictionary)    - The restourants' info (name and rating) to be displayed. 
#                                 It will be about either the 'good' or 'not so good' places
#
# Return value:                 - None
def displayRatings(title, ratings):

    print("\n{}".format(title))
    print("{:->40s}".format(''))

    for aPlace, aRating in ratings.items():
        print("{0:35s}{1}".format(aPlace, aRating * "*"))


restaurantRatings = getUserRatings()                            # collect restaurant names and rating for each from user
goodPlaces = groupPlacesByRating(restaurantRatings, 3, 5)       # figure out the 'good places to eat', based on a min and max rating
notSoGoodPlaces = groupPlacesByRating(restaurantRatings, 1, 2)  # figure out the 'not so good places to eat', based on a min and max rating

displayRatings("Good Places to Eat", goodPlaces)                # display back to the user all the good places to eat
displayRatings("Not as Good Places to Eat", notSoGoodPlaces)    # display back to the user all the not so good places to eat