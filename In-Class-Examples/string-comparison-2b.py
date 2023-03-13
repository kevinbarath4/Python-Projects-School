confirmation = input("Please confirm [Yes/No]: ")

# Validating user's entry, by checking each possible combination
if confirmation == "YES" or confirmation == "yes" or confirmation == "Yes" \
    or confirmation == "yES" or confirmation == "YeS" or confirmation == "YEs" \
    or confirmation == "NO" or confirmation == "no" or confirmation == "No" \
    or confirmation == "nO":

    print("Thank you!")
else:    
    print("Invalid entry. Run the program again and enter a valid value. Goodbye!")