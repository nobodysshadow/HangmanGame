"""
[hangmanGame.py] from the HangmanGame
Main application for the game
"""
# Import necessary modules and the wordlist
<<<<<<< HEAD
=======
import random
>>>>>>> Bug1a2
import Lib

# Start of the game
# Variables
guessed_letters = []
game = False

<<<<<<< HEAD
searchWord = Lib.start.getRandomWord()
=======
searchWord = Lib.start.getRandomWord(random.randint(3, 6))
>>>>>>> Bug1a2
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
<<<<<<< HEAD
    if len(list(guess)) > 1:
        if Lib.game.word_correct(guess, searchWord):
            print("You have won!")
            break   
    guessed_letters.append(guess)
=======
    guessed_letters.append(guess)
    # print("Length of guess: ", len(Lib.game.missed_letters(guessed_letters, searchWord)))
    if len(list(guess)) > 1:
        if Lib.game.word_correct(guess, searchWord):
            print("You have won!")
            game = True
    # Amount of missed letters does not exceed the hangman pictures.
    elif len(Lib.game.missed_letters(guessed_letters, searchWord)) > 6:
        print("Sorry you loose!")
        print("The searched word was: ", searchWord)
        print()
        game = True
>>>>>>> Bug1a2
