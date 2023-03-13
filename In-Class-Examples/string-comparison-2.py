confirmation = input("Please confirm [Yes/No]: ")

# Validating user's entry. Case of the the value entered by user is
# ignored when checking it (comparing) against the valid values ("YES" and "NO")
if confirmation.upper() == "YES" or confirmation.upper() == "NO":
    print("Thank you!")
else:    
    print("Invalid entry. Run the program again and enter a valid value. Goodbye!")