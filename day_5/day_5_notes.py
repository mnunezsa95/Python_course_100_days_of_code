# ------------------------------------------------------------------------------------------------ #
#                                 Section 5 - Day 5 - Python Loops                                 #
# ------------------------------------------------------------------------------------------------ #

### Python Loops (for lists)
fruits = ["Apple", "Peach", "Pear"]

# for loop will iterate through the list & do something to the indented code
for fruit in fruits: # the name "fruit" can be anything, but naming it something meaningful is important
    print(fruit)
    print(fruit + " Pie")

# Example 1: Using a for loop to calculate average height in a list
student_heights = [151, 145, 179]

total_height = 0
for height in student_heights:
  total_height += height

num_students = len(student_heights)
average_height = round(total_height / num_students)

print(f"total height = {total_height}")
print(f"number of students = {num_students}")
print(f"average height = {average_height}")

# Example 2: Using a for loop to determine the max score in a list
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is: {highest_score}")

### for loops with the range() function
for number in range(1, 10): # range() function creates a range from a to b (not including b)
  print(number) # 1, 2, 3, 4, 5, 6, 7, 8, 9

# Example 1: Using the range() function
total = 0
for number in range(1, 101):
  total += number
print(total)

# Example 2: Using range() function to calculate the sum of even numbers between 0 and target
target = 100

sum = 0
for number in range(0, target + 1, 2):
  sum += number
print(sum)

# Example 3: FizzBuzz Game
#--if number is divisible by 3 and 5, print "FizzBuzz"
#--if number is divisible by 5, print "Buzz"
#--if number is divisible by 3, print "Fizz"
#--if number is not divisible by any, print the number

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 5 == 0:
    print("Buzz")
  elif number % 3 == 0:
    print("Fizz")
  else:
    print(number)

