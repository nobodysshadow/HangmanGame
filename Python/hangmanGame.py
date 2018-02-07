"""
[hangmanGame.py] from the HangmanGame
Main application for the game
"""
# Import necessary modules and the wordlist
import Lib

# Start of the game
wrongGuess = ""
searchWord = Lib.start.getRandomWord()
status = Lib.start.initStatus(searchWord)
Lib.start.displayBoard(wrongGuess, status)
