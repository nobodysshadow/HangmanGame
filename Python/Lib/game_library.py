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
    New_guessed_letters = guessed_letters

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
    else:
        New_guessed_letters.append(guess.upper())


    # Retrun the guess
    return New_guessed_letters



def player_guesses_the_word(guess, word):
    # Variables
    output = False
    # Is it the correct word
    if guess.upper() == word.upper():
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



def get_word_stats(guessed_letters, word):
    # Variables
    word_stats = []
    word = word.upper()

    # Replace letters in the word with a "_".
    for i in list(word):
        word_stats.append("_")

    # Replace the "_" with the right letter, when the letter is guessed.
    for i in range(len(list(word))):
        for e in guessed_letters:
            if list(word)[i] == e:
                word_stats[i] = e
    return word_stats



def remove_try(tries):
    return tries - 1



def get_wrong_guesses(guessed_letters, word):
    #Variables
    word = list(word.upper())
    letters = guessed_letters

    #Get wrong guesses
    for i in letters:
        if i in word:
            letters.remove(i)
    return letters



if __name__ == "__main__":
    #guess("World", [])
    #print(get_word_stats(list("TANZEN"), "Tanzen"))
    print(get_wrong_guesses(list("GUMBADCKT"), "Gumba"))
