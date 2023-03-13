demo = "     This is a demo string     "

print("The string is now in caps and still has the whitespace at the ends: **" + demo.upper() + "**")

# stacking upper() and strip() methods: upper() method is called 
# first and then strip() method is called on the resulting string
print("The string is now in caps and does not have the whitespace: **" + demo.upper().strip() + "**")