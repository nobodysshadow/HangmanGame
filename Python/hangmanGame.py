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

#searchWord = Lib.start.getRandomWord()
#while tries <= 6:
#    Lib.start.displayBoard(Lib.game.get_wrong_guesses(guessed_letters, searchWord), Lib.game.get_word_stats(guessed_letters, searchWord))
#    output = Lib.game.guess(searchWord, guessed_letters)[:]
#    guess = output[0]
#    guessed_letters = output[1]
#    if Lib.game.player_guesses_the_word(guess, searchWord) == True:
#        print("You have won!")
#        break
#    else:
#        print(guessed_letters)

searchWord = Lib.start.getRandomWord()
while game == False:
    stats = Lib.game.stats(guessed_letters, searchWord)
    Lib.start.displayBoard(Lib.game.missed_letters(guessed_letters, searchWord), stats)
    if Lib.game.won(stats, searchWord):
        break
    print(searchWord)
    guessed_letters.append(Lib.game.guess())
