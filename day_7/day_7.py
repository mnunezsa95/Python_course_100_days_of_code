#--1: Import the hangman_art and hangman_words
#--2: Update the word list to use 'word_list from hangman_words.py
#--3: Import the logo from hangman_art.py and print it at the start of the game.
#--4: Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#--5: Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
from hangman_words import word_list
from hangman_art import stages, logo
import random

print(logo)

chosen_word = random.choice(word_list)
lives = 6

print(f'The chosen word is: {chosen_word}.')

#--5: Create an empty List called display.
#------For each letter in the chosen_word, add a "_" to 'display'.

display = []
for _ in chosen_word: # Use _ to signify a placeholder variable (a placeholder specifies a variable that isn't used)
    display.append("_")

#--6: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#--7: If the user has entered a letter they've already guessed, print the letter and let them know.
#--7: Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#--8: Loop through each position in the chosen_word;
#------If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#--9: Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
#--10: Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".   
#--11: If guess is not a letter in the chosen_word, then reduce 'lives' by 1. If lives goes down to 0 then the game should stop and it should print "You lose."
#--12: Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining

end_of_game = False
guesses = []

while not end_of_game:
    guess = input("Choose a letter. ").lower()
    guesses.append(guess)
    
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)
    
    if guess not in chosen_word:
        print(f"{guess} is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
        
    if "_" not in display:
        end_of_game = True
        print("You win!")
        
    print(stages[lives])