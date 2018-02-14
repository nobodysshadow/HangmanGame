"""
[hangmanGame.py] from the HangmanGame
Main application for the game
"""
# Import necessary modules and the wordlist
import random
import Lib

# Start of the game
# Variables
guessed_letters = []
game = False

searchWord = Lib.start.getRandomWord(random.randint(3, 6))
while game == False:
    possible = False
    guess = ""
    stats = Lib.game.stats(guessed_letters, searchWord)
    Lib.start.displayBoard(Lib.game.missed_letters(guessed_letters, searchWord), stats)
    if Lib.game.won(stats, searchWord):
        break
    while possible == False:
        guess = Lib.game.guess()
        possible = Lib.game.check_valid_guess(guess, guessed_letters)
    guessed_letters.append(guess)
    # print("Length of guess: ", len(Lib.game.missed_letters(guessed_letters, searchWord)))
    if len(list(guess)) > 1:
        if Lib.game.word_correct(guess, searchWord):
            print("You have won!")
            game = True
    elif len(Lib.game.missed_letters(guessed_letters, searchWord)) > 6:
        print("Sorry you loose!")
        print("The searched word was: ", searchWord)
        print()
        game = True
