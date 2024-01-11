# ------------------------------------------------------------------------------------------------ #
#                            Dictionaries & Nesting Inside Dictionaries                            #
# ------------------------------------------------------------------------------------------------ #

# Dictionaries
# -Dictionaries have keys-value pairs
# --Keys serve as the reference point for the value
# --Values is the data

# Syntax
{"key1", "value1", "key2", "value2"}
# --variable name, followed by an assignment operator and curly braces
# --key/value pairs are separated by comma

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}

# -Accessing items in a dictionary
# --When accessing a value by its key, the correct data type needs to be passed into the brackets
# dictionaries are accessed by their key in square brackets (key needs to be spelled correctly)
print(programming_dictionary["Bug"])

# -Adding new items to a dictionary
# set the key name equal to the value
programming_dictionary[
    "Python"
] = "A programming language used for backend development and data analysis"
print(programming_dictionary)

# -Creating an empty dictionary
empty_dictionary = {}  # set a variable equal to an empty dictionary

# -Wiping an existing dictionary
dictionary1 = {1: "one", 2: "two", 3: "three"}  # creating a dictionary
dictionary1 = {}  # setting an existing dictionary equal to an empty one will wipe it
print(dictionary1)

# -Editing an item in a dictionary
# --Setting an existing key equal to a new value will update it
programming_dictionary[
    "Bug"
] = "An error in a program that prevents the program from running as expected. Named after a moth that entered a computer"
print(programming_dictionary)

# -Looping through a dictionary
for key in programming_dictionary:  # using a for loop to loop through a dictionary
    print(key)
    print(programming_dictionary[key])

# Example 1: grading program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    score = student_scores[key]
    if score >= 90:
        student_grades[key] = "Outstanding"
    elif score > 80:
        student_grades[key] = "Exceeds Expectations"
    elif score > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

# Nesting Lists and Dictionaries
# --Lists and Dictionaries can be nested inside a dictionary
{"key1": ["value1", "value2"], "key2": {"value3", "value4"}}

capitals = {"France": "Paris", "Germany": "Berlin"}

# --Nesting lists in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# --Nesting dictionaries in dictionaries
travel_log2 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10,
    },
}

# --Nesting dictionaries inside a list
travel_log3 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10,
    },
]


# Example 2: Creating a function to add cities
def add_new_country(country, visits, list_of_cities):
    travel_log3.append({"country": country, "visits": visits, "cities": list_of_cities})


# Adding item
add_new_country("India", 3, ["Kochi", "Hyderabad", "Bangalore"])
add_new_country("Japan", 4, ["Kyoto", "Kagoshima", "Tokyo"])

print(travel_log3)
