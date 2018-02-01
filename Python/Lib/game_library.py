"""
The main game library for the game "HangmanGame"
"""
def guess_a_letter(guessed_letters, tries):
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

def show(guessed_letters, number_of_letters, list_of_letters_in_the_word):
    letter_list = []
    while number_of_letters == 0:
        for i in guessed_letters:
            for l in list_of_letters_in_the_word:
                letter_list.append
    return None
