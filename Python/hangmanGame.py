"""
[hangmanGame.py] from the HangmanGame
Main application for the game
"""
# Import necessary modules and the wordlist
import Lib

# Start of the game
# Variables
guessed_letters = []
game = False

searchWord = Lib.start.getRandomWord()
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
    if len(list(guess)) > 1:
        if Lib.game.word_correct(guess, searchWord):
            print("You have won!")
            break   
    guessed_letters.append(guess)
