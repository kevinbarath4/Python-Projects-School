confirmPrompt = input("Please confirm [Yes/No]: ")

# The condition in the loop checks if user's entry is invalid
# by comparing it to each of the two of accepted values ('yes' and'no').
#
# The loop will repeat the code that displays the prompt and collects input from user
# as long as user is providing an invalid value.
while not(confirmPrompt.strip().upper() == "YES" or confirmPrompt.strip().upper() == "NO"):
    confirmPrompt = input("The value is invalid. Values accepted are 'yes' and 'no'. Please re-enter: ")    


print("Thank you!")