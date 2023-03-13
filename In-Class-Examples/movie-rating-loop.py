while True:             # will run at least once, as True will always be True
    rating = int(input("Enter your rating for the movie (a number 1 to 5): "))

    # checking if valid value is provided and 
    # if yes exit the loop (stop asking user the question)
    if rating >= 1 and rating <= 5:     
        break          # we need to use break, as the loop would otherwise run forever

print("Thanks!")