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

### Mathematical Operations 
print(3 + 5) # addition
print(7 - 3) # subtraction
print(3 * 2) # multiplication
print(6 / 3) # division; almost always ends up in a floating-point number
print(2 ** 3) # exponents

### Priority in math operations (PEMDAS)
# Parantheses are prioritized first
# Exponents are second
# Multiplication and Division are equal (read left-to-right)
# Addition and Subtraction are equal (read left-to-right)

print(3 * 3 + 3 / 3 - 3)

### Number manipulation
# round() function rounds a number accordingly
print(round(8 / 3, 4))

# floor division 
print(8 // 3) # floor division will floor a number (remove decimal places) & returns a int type
print(4 // 2) # floor division is useful when we don't want a floating-point number

# Shorthand manipuation
score = 0 
score += 3 # adds 3 to the previous value
score -= 1 # subtracts 1 to the previous value
score *= 5 # multiplies 5 to the previous value
score /= 1 # divides 1 to the previous value

# f-strings
height = 1.8
isWinning = True

# f-strings is useful for adding several values of different data types
print(f"Your score is {score} and your height is {height}, you are winning is {isWinning}")

