# ------------------------------------------------------------------------------------------------ #
#                                       NATO Alphabet Project                                      #
# ------------------------------------------------------------------------------------------------ #

# 1. Create a dictionary in this format:
import pandas

data = pandas.read_csv("day_26/day_26_project/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
result = [phonetic_dict[letter] for letter in user_input]
print(result)
