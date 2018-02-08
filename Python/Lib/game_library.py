"""
The full game_library of the game hangmanGame.py
"""
# Guss a letter or a word
def guess(word, guessed_letters):
    """
    Get the guess from the player
    """
    # Variables
    possible = False

    # Get the guess
    while possible == False:
        guess = input("Guess a letter or a word: ")
        # Check is it a word or a letter
        if len(list(guess)) > 1:
            # Word
            player_guesses_the_word(guess, word)
            break
        else:
            # Letter
            # Is the guess already guessed?
            possible = guess_is_guessed(guessed_letters, guess)
            print("")

    # Retrun the guess
    return guess

def player_guesses_the_word(guess, word):
    # Variables
    output = False
    # Is it the correct word
    if guess == word:
        output = True
    else:
        wrong_guess()

    # Retrun the output
    return output

def wrong_guess():
    # Print a little message
    print("You guessed wrong")

def not_possible():
    print("You already guessed this letter")

def guess_is_guessed(guessed_letters, guess):
    # Variables
    output = True

    for i in guessed_letters:
        if i == guess:
            output = False
    
    # Is guess already guessed?
    if output == False:
        not_possible()

    # Return output
    return output



if __name__ == "__main__":
    guess("World", [])
