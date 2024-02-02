# ------------------------------------------------------------------------------------------------ #
#                                 List and Dictionary Comprehension                                #
# ------------------------------------------------------------------------------------------------ #

# -------------------------------------- List Comprehension -------------------------------------- #

# - List Comprehension is a case when a list is created from another list
# -- Can be done using a for loop (results in long code)

# List comprehension syntax
# SYNTAX#*     new_list = [new_item for item in list]
# -- new_list is the name of the new list
# -- new_item is the expression
# -- item can be named anything
# -- list is the name of the old list

# Examples: using list comprehension
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Harper"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [number * 2 for number in range(1, 5)]
print(range_list)

numbers2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num**2 for num in numbers2]
print(squared_numbers)

# -------------------------------- Conditional List Comprehension -------------------------------- #
# SYNTAX#*    new_list = [new_item for item in list if test]
# -- new_list is the name of the new list
# -- new_item is the expression
# -- item can be named anything
# -- list is the name of the old list
# -- if test will only execute expression if the test is passed

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

numbers3 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_nums = [num for num in numbers3 if num % 2 == 0]
print(even_nums)

# Challenge 1: Find the numbers common to both lists
list_1 = ["3", "6", "5", "8", "33", "12", "7", "4", "72", "2", "42", "13"]
list_2 = ["3", "6", "13", "5", "7", "89", "12", "3", "33", "34", "1", "344", "42"]
common_numbers = [int(num) for num in list_1 if num in list_2]
print(common_numbers)


# ----------------------------------- Dictionary Comprehension ----------------------------------- #
# SYNTAX#*    new_dict = {new_key:new_value for item in list}
# -- new_dict is the name of the new dict
# -- new_key:new_value are the new values to be used in the dict
# -- key,value are key values to be grabbed from the existing dict
# -- list/dict.items() is the name of the old list / old dictionary

# SYNTAX#*    new_dict = {new_key:new_value for (key,value) in dict.items()}
# SYNTAX#*    new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

names2 = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names2}
print(students_scores)

passed_students = {
    student: score for (student, score) in students_scores.items() if score >= 60
}
print(passed_students)

# Challenge 1:
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
len_of_words = {word: len(word) for word in sentence.split()}
print(len_of_words)

# Challenge 2:
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9 / 5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)

# ------------------------------- Iterating over a Pandas DataFrame ------------------------------ #

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# Looping through dictionaries
for key, value in student_dict.items():
    print(value)

# Looping through DataFrame
import pandas

student_data_frame = pandas.DataFrame(student_dict)
for key, value in student_data_frame.items():
    print(key)
    print(value)

# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    print(row.student)
    print(row.score)
