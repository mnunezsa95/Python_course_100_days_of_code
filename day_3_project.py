# ------------------------------------------------------------------------------------------------ #
#                       Section 3: Day 3 - Control Flow and Logical Operators                      #
# ------------------------------------------------------------------------------------------------ #

### comparison operator
'''
> greater than
< less than
>= greater than or equal to
<= less than or equal to
== equal to
!= not equal to
''' 

### if/else 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120: # if statement executes when the expression/condition is met
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:  # if/else statements can be nested inside if/else statements
       print("Child tickets are $5.")
       bill = 5
    elif age <= 18 and age >= 12:
       print("Youth tickets are $7.")
       bill = 7
    else: 
       print("Adult tickets are $12.")
       bill = 12
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
       bill += 3
    print(f"Your final bill is ${bill}")
else: # else statement executes when the if condition/expression is NOT met
    print("You are not tall enough to ride the rollercoaster")

### modulo operator
number = 6
if number % 2 == 0: # the modulo operator returns the remainder of an expression
  print("This is an even number.")
else:
  print("This is an odd number.")

### logical operators

