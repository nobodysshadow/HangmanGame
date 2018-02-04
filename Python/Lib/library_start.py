"""
[library_start.py] from the HangmanGame
Defines the function of GW for the game

HANGMAN_PICS            Definition of the Definition of the hangman pictures
getRandomWord(length)   Word selection function that return the to word to guess
displayBoard(missedLetter,wordStatus): Function that displays the game status 
                                       with the missed letters, the hangman 
                                       picture and the actual word status
"""
import random
import wordList

# Definition of the hangman pictures that simulate the failed trys. (max 6)
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

# Definition of standart functions
def getRandomWord(length = 6):
    '''
    Input length: Amount of letter (3-6) the word should contain.
                  Default is 6 letters (Highest difficult level).
    Return: a randomly chossen word of the wordlist.
    '''
    if length == 3:
        wordIndex = random.randint(0, len(wordList.WORDLIST3) - 1)
        return wordList.WORDLIST3[wordIndex]
    elif length == 4:
        wordIndex = random.randint(0, len(wordList.WORDLIST4) - 1)
        return wordList.WORDLIST4[wordIndex]
    elif length == 4:
        wordIndex = random.randint(0, len(wordList.WORDLIST5) - 1)
        return wordList.WORDLIST5[wordIndex]
    else:
        wordIndex = random.randint(0, len(wordList.WORDLIST6) - 1)
        return wordList.WORDLIST6[wordIndex]

def displayBoard(missedLetter,wordStatus):
    '''
    Input missedLetter: String of missed letters form previouse guesses
          wordStatus: The aktuell Status of the word to guess (_ _ _ _ _ _)
                      at the beginning.
    '''
    print("Your missed letters:  ",missedLetter)
    print(HANGMAN_PICS[len(missedLetter)])
    print()
    print(wordStatus)
    print()
