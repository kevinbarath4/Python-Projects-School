text = "python is Easy to Learn."

print("\nusing capitalize() method:")
print(text.capitalize())                    # capitalize() returns "Python is easy to learn".

print("\nusing title() method:")
print(text.title())                         # title() returns "Python Is Easy To Learn."

print("\nusing startswith() method:")
print(text.startswith('python is Easy'))    # startswith() returns True

print("\nusing endswith() method:")
print(text.endswith('to Learn.'))           # startswith() returns True

print("\nusing count() method:")
print(text.count('y'))                      # count() returns 2


text1 = "python is Easy 2 Learn."

print("\nusing isspace() method:")
print(text1.isspace())                      # isspace() returns False

print("\nusing isalpha() method:")
# isspace() returns False because of the number 2, dot, whitespaces
print(text1.isalpha())

print("\nusing isalnum() method:")
# isalnum() returns False because of the whitespaces and dot
print(text1.isalnum())

text2 = "123.45"

print("\nusing isdecimal() method:")
print(text2.isdecimal())    # returns False, because of the dot

# However, we can do something like this...
if text2.count(".") == 1:               # searching for exactly 1 dot (a possible decimal point)
    text2 = text2.replace('.', '')		# removing the dot

    # checking the rest of the characters in the string, if they are digits; returns True    
    print(text2.isdecimal())			        