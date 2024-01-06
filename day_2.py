# ------------------------------------------------------------------------------------------------ #
#             Section 2: Day 2 - Understanding data types and how to manipulate strings            #
# ------------------------------------------------------------------------------------------------ #

### Python primitive data types

# Strings
"Hello" # strings are composed of individual characters
print("Hello"[0]) # characters can be accessed using the index
print("Hello"[-1]) # printing the last character of the string

# Numbers (Integers and Floats)
print(123 + 345) # integers are whole numbers
print(123_345_789) # large numbers can be split up using underscores (ignored by computer)
print(3.14159) # floating-point numbers are decimal numbers

# Boolean 
print(True) 
print(False) 

### Type Error, Type Checking and Type Conversion
num_char = len("Marlon")
print(type(num_char)) # the type() function checks the 'type' of the argument passed in

num_char = str(num_char) # the str() function converts the argument to a string type
print("Your name has " + num_char + " characters") 

a = float(123) # the float() function converts the argument to a floating-point number
print(type(a)) 

