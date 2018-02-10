def guess():
    guess = input("Guess a letter: ")
    return guess.upper()



def stats(guessed_letters, word):
    # Variables
    stats = []
    word = list(str(word).upper())

    for i in word:
        stats.append("_")
    
    for i in range(len(word)):
        for e in guessed_letters:
            if word[i] == e:
                stats[i] = e
    return stats



def missed_letters(guessed_letters, word):
    missed_letters = guessed_letters[:]
    word = list(str(word).upper())
    #print(guessed_letters, missed_letters)
    print(word)
    for i in guessed_letters:
        if i in word:
            print(i)
            print(missed_letters)
            missed_letters.remove(i)
            print (missed_letters)
    #print(guessed_letters, missed_letters)
    return missed_letters



def guess_right(guess, word):
    # Variables
    output = False

    if guess in word:
        print("The guess is correct")
        output = True
    else:
        print("The guess is false")
        output = False
    return output



def won(stats, word):
    output = False
    if ''.join(stats) == word.upper():
        print("You have won!")
        output = True
    return output



def check_valid_guess(guess, guessed_letters):
    output = False
    if guess != None:
        if guess in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") and guess not in guessed_letters:
            output = True
        elif len(list(guess)) > 1:
            output = True
    return output



def word_correct(guess, word):
    output = False
    word = word.upper()
    if guess == word:
        output = True
    return output

if __name__ == "__main__":
    print(stats(list("ABCDEFGHIJKT"), "Tanzen"))
