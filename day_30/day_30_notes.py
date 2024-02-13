# ------------------------------------------------------------------------------------------------ #
#                                 Errors, Exceptions, and JSON Data                                #
# ------------------------------------------------------------------------------------------------ #

# ---------------------------------------- Types of Errors --------------------------------------- #
###! FileNotFound
# with open("a_file.txt") as file:
#     file.read()

###! KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

###! IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

###! TypeError
# text = "abc"
# print(text + 5)

# ----------------------------------------- Try and Catch ---------------------------------------- #
### Try-Catch block
# -- `try` - executes something that might cause an exception (an error)
# -- `except` - executes if an error occurs in try-block
# -- `else` - executes if there were no exceptions (no problems occurred)
# -- `finally` - executes no matter what happens (whether execute or else runs)


try:  # Try out this block
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    value = a_dictionary["key"]
except FileNotFoundError:  # If FileNotFoundError exception happens, execute this block
    file = open("day_30/a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:  # Executes if there are not exceptions
    content = file.read()
    print(content)
finally:  # Execute regardless of whether there were exceptions or not
    file.close()
    print("File was closed")


# ------------------------------------ Raise Unique Exceptions ----------------------------------- #
# The raise keyword is used to raise a unique exception
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height**2
print(bmi)

### Exercise 1:
facebook_posts = [
    {"Likes": 21, "Comments": 2},
    {"Likes": 13, "Comments": 2, "Shares": 1},
    {"Likes": 33, "Comments": 8, "Shares": 3},
    {"Comments": 4, "Shares": 2},
    {"Comments": 1, "Shares": 1},
    {"Likes": 19, "Comments": 3},
]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError:
        pass

print(total_likes)


# Exercise 2: import pandas
import pandas

data = pandas.read_csv("day_30/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
