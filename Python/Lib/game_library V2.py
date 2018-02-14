"""
The full game_library of the game hangmanGame.py
"""
# Guss a letter or a word
def guess(word, guessed_letters):
    """
    Get the guess from the player
    word: The secret word
    guessed_letters: The already guessed letters
    return: The new already guessed letters list
    """
    # Variables
    possible = False
    New_guessed_letters = guessed_letters
    #output = False

    # Get the guess
    while possible == False:
        guess = input("Guess a letter or a word: ")
        guess = guess.upper()
        # Check is it a word or a letter
        if len(list(guess)) > 1:
            # Word
            #output = player_guesses_the_word(guess, word)
            #New_guessed_letters.append(guess.upper())
            break
        else:
            # Letter
            # Is the guess already guessed?
            possible = guess_is_guessed(guessed_letters, guess)
            if possible == True:
                New_guessed_letters.append(guess.upper())
                is_guess_correct(guess, word)

    # Retrun the guess
    return guess, New_guessed_letters



def player_guesses_the_word(guess, word):
    """
    If the player has guessed a word, the function checks the player has won or not.
    guess: The player guess
    word: The secret word
    return: bool, The player has won.
    """
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
    """
    Prints a little message to show the player he guessed wrong.
    """
    # Print a little message
    print("You guessed wrong")



def not_possible():
    """
    Prints a little message to show the player he guessed this letter twice.
    """
    print("You already guessed this letter")



def guess_is_guessed(guessed_letters, guess):
    """
    This function checks the player hasn't guessed the letter twice.
    guessed_letters: The already guessed letters
    guess: The player guess
    return: bool, The guess is possible
    """
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
    """
    This function gets the latest word stats.
    guessed_letters: The already guessed letters
    word: The secret word
    return: The latest word stats
    """
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
    """
    This functions remove a try.
    tries: The tries the player has left
    return: The new tries count
    """
    return tries - 1



def get_wrong_guesses(guessed_letters, word):
    """
    This functions gets all the letters, that are wrong.
    guessed_letters: The already guessed letters
    word: The secret word
    return: The wrong letters
    """
    # Variables
    word = list(word.upper())
    letters = guessed_letters

    # Get wrong guesses
    for i in letters:
        if i in word:
            letters.remove(i)
    return letters


def is_guess_correct(guess, word):
    """
    Is the guess of the player correct?
    guess: The latest guess of the player
    word: The secret word
    """
    if guess in list(word):
        print("You have guessed correctly")
    else:
        wrong_guess()

def won(word_stats):
    """
    Has the player won?
    word_stats: The latest word stats
    return: bool, The player has won
    """
    # Variables
    output = False
    if all in word_stats != "_":
        output = True
    return output



if __name__ == "__main__":
    #guess("World", [])
    #print(get_word_stats(list("TANZEN"), "Tanzen"))
    print(get_wrong_guesses(list("GUMBADCKT"), "Gumba"))
