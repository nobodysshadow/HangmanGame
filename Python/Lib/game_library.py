"""
The main game library for the game "HangmanGame"
"""
def guess_a_letter(guessed_letters, tries):
    """
    Function to guess a letter, remove a try and add the letter to the letter list.
    guessed_letter: The guessed letters.
    tries: The Number of tries.
    """
    guess_possible = 0
    while guess_possible == 0:
        guess = input()
        for i in guessed_letters:
            if guess == i:
                checked = 1
        if checked == 0:
            guess_possible = 1
        else:
            print("You have guessed the letter twice!")
    tries = tries - 1 
    guessed_letters.append(guess)
    output = [tries, guessed_letters.append(guess)]
    return output

def show(guessed_letters, word):
    """
    Shows the letters.
    guessed_letters: The guessed letters.
    word: The secret word.
    """
    #Variables
    letter_list = []

    guessed_letters = list(str(guessed_letters).upper())
    word = str(word).upper()

    for i in word:
        letter_list.append("_")
    for i in range(len(list(word))):
        for e in guessed_letters:
            if e == word[i]:
                letter_list[i] = e
    print (str(letter_list).upper())
    return letter_list

def check_guess(guess, word, tries, guessed_letters, letter_list):
    """
    guess: The player guess.
    word: The secret word.
    tries: Number of tries.
    guessed_letters: The guessed letters.
    letter_list: The word with the gaps.
    """
    win = 0
    if len(list(guess)) > 0:
        if guess == word:
            win = 1
        else:
            lose(tries)
    else:
        for i in list(word):
            if i == guess:
                right_guess(word, guessed_letters, letter_list)
    return win

def lose(tries):
    """
    tries: The number of tries
    It show a little lose message and check the tries.
    """
    if tries == 0:
        print("Du hast verloren")
    else:
        print("Du hast falsch geraten")
    return None

def right_guess(word, guessed_letters, letter_list):
    """
    word: The secret word.
    guessed_letters: The guessed letters.
    letter_list: The word with the gaps.
    This function let you win.
    """
    win = 1
    win_list = []
    guessed_letters = list(str(guessed_letters).upper())
    word = str(word).upper()
    print("Du hast richtig geraten")
    for i in list(word):
        for letters in guessed_letters:
            if i == letters:
                win_list.append(1)
            else:
                win_list.append(0)
    for i in win_list:
        if i != 1:
            win = 0
    return win

show(list("abcdefghijklmnopqrstuvwxyz"), "Tanzen")