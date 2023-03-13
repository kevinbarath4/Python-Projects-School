confirmation = input("Please confirm [Yes/No]: ")

# Validating user's entry:
# Case of the value entered by user is ignored when checking it (comparing) 
# against the valid values ("YES" and "NO")
# Any leading and trailing whitespace is stripped off the value as well
if confirmation.strip().upper() == "YES" or confirmation.strip().upper() == "NO":
    print("Thank you!")
else:    
    print("Invalid entry. Run the program again and enter a valid value. Goodbye!")