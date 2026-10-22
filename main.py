# Python Wordle Game
# Author: Caleb Nelson

from wordle_functions import choose_word, get_guess, evaluate_guess, display_guess, has_won

# Welcome the player and give instructions
print("Welcome to Python Wordle!")
print("You will have 6 guesses to figure out the secret five letter word chosen by the computer. " \
"After each guess, the computer will return 'G' for each letter that is correct and in the correct position. " \
"It will return 'Y' for each letter that is correct but in the incorrect position.")

# Continue looping the game until the player asks to stop
continue_play = True
while continue_play == True:

    # Set some base variable values
    number_guesses = 0
    guess_index = []

    # Choose a random word
    word = choose_word().upper() 

    # Loop through six guesses
    while number_guesses <= 5:
    
    # Get a guess
        print("Attempt " + str(number_guesses + 1) + " of 6")
        guess_word = get_guess(guess_index)
        
        # Record the guess
        number_guesses += 1 
        guess_index.append(guess_word) # Store the guess for future reference
        
        # Evaluate and display the guess
        feedback = evaluate_guess(word, guess_word)
        display_guess(guess_word, feedback)

        # Check whether the player won
        if has_won(word, guess_word) == True:
            print ("Congrats! You guessed the word. It was " + word + "!")
            break

        # Check whether the player has run out of guesses
        if number_guesses == 6:
            print("You've run out of guesses. The word was " + word + ".")
            break
    
    # Ask the player if they want to play again
    user_desire = input("Would you like to play again? (T/F): ").upper()

    while user_desire != "T" and user_desire != "F":
        user_desire = input("Please enter 'T' or 'F'. Would you like to play again?: ").upper()

    if user_desire == "T":
        continue_play = True
    elif user_desire == "F":
        continue_play = False

# Display a final message
print("Thanks for playing!")