# ------------------------------------------------------------------------------------------------ #
#                                           Caesar Cipher                                          #
# ------------------------------------------------------------------------------------------------ #

from day_8_project_art import logo

print(logo)


def caesar(cipher_direction, start_text, shift_amount):
    end_text = ""
    for i in range(len(start_text)):
        if start_text[i] in alphabet:
            position = alphabet.index(start_text[i])
            if cipher_direction == "encode":
                new_position_forwards = position + shift_amount
                end_text += alphabet[new_position_forwards]
            elif cipher_direction == "decode":
                new_position_backwards = position - shift_amount
                end_text += alphabet[new_position_backwards]
        else:
            end_text += start_text[i]
    print(f"The {cipher_direction}d text is {end_text}")


should_continue = True

while should_continue:
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye")
