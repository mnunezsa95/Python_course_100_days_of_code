from hangman_words import word_list # import hangman words 
from hangman_art import stages, logo # import stages array and logo var
import random # import random module

# create initial variables
lives = 6 # number of user lives
end_of_game = False # value to end game
display = [] # container for underscores equivalent to chosen word
guesses = [] # container for recent guesses

chosen_word = random.choice(word_list) # randomly choose a word from list

print(logo) # print logo for game

for _ in chosen_word: # create the container for chosen word
    display.append("_")

# While loop runs as long as game is not over
while not end_of_game:
    guess = input("Choose a letter. ").lower() # save user input to a variable
    guesses.append(guess) # add the guess to the guesses array
    
    print(f"Your recent guessed letters are: {guesses}") # print recent guesses for user
    
    if guess in display: # if the guess was already guessed, do not take life away
        print(f"You've already guessed the letter: {guess}")
    
    for i in range(len(chosen_word)): # iterate the chosen word 
        if chosen_word[i] == guess: # if guess exists in the chosen word, add it at that specific spot
            display[i] = guess
    print(display) # print the display
    
    if guess not in chosen_word: # if the guess is not in the word
        print(f"{guess} is not a letter in the word. You lose a life :(") # let user know they lost a life
        lives -= 1 # reduce number of lives
        if lives == 0: # if the lives get to zero, game ends, user loses
            end_of_game = True
            print("You lose!")
        
    if "_" not in display: # end game once all "_" are all removed in the display list
        end_of_game = True # game ends, user wins
        print("You win!")
        
        
    print(stages[lives]) # print the ASCII Art for the relevant position
