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

# Definition of the wordlists with 3 to 6 letters
WORDLIST3 = 'ant bat cat dog fly fox owl ram rat'.split(' ')
WORDLIST4 = 'bear clam crow deer duck frog goat hawk lion mole mule newt seal swan toad wolf'.split(' ')
WORDLIST5 = 'camel cobra eagle goose llama moose mouse otter panda raven rhino shark sheep skunk sloth snake stork tiger trout whale zebra'.split(' ')
WORDLIST6 = 'baboon badger beaver cougar coyote donkey ferret lizard monkey parrot pigeon python rabbit salmon spider turkey turtle weasel wombat'.split(' ')

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
def getRandomWord(length = 3):
    """Random word of predefined wordlist
    
    Select a random word of predefined wordlist
        length ([int], optional): Defaults to 3. 
                                  Amount of letter (3-6) the word should contain.
    
    Returns:
        [string]: a randomly chossen word of the wordlist.
    """
    if length == 3:
        wordIndex = random.randint(0, len(WORDLIST3) - 1)
        return WORDLIST3[wordIndex]
    elif length == 4:
        wordIndex = random.randint(0, len(WORDLIST4) - 1)
        return WORDLIST4[wordIndex]
    elif length == 4:
        wordIndex = random.randint(0, len(WORDLIST5) - 1)
        return WORDLIST5[wordIndex]
    else:
        wordIndex = random.randint(0, len(WORDLIST6) - 1)
        return WORDLIST6[wordIndex]

def displayBoard(missedLetter,wordStatus):
    """Display gaming status
    
    Display gaming status inkl. hangman picture
    
    Args:
        missedLetter ([string]): String of missed letters form previouse guesses
        wordStatus ([string]): The aktuell Status of the word to guess 
                               '_ _ _ _ _ _' at the beginning.
    """
    # Check that the amount of missed letters does not exceed the hangman pics
    if len(missedLetter) > len(HANGMAN_PICS):
        print("Sorry! you have used up all your guesses.")
        print("The searched word was: ", searchWord)
        print()
        break
    else:
        print("Your missed letters:  ",missedLetter)
        print(HANGMAN_PICS[len(missedLetter)])
        print()
        print(wordStatus)
        print()

def initStatus(searchWord):
    """Initialize Status
    
    Initialize the serach word status string
    
    Args:
        searchWord ([string]): the word to guess for the game
    Returns:
        [string]: Status string '_ _ _' for 3 letter words
    """
    statusString = ""
    for i in range(1,(len(searchWord)*2)):
        if i % 2:
            statusString += "_"
        else:
            statusString += " "
    return statusString