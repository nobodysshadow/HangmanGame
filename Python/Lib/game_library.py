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
        print("Test")
        print(guessed_letters)
        for e in guessed_letters:
            if word[i] == e:
                stats[i] = e
    return stats



def missed_letters(guessed_letters, word):
    missed_letters = guessed_letters
    word = list(str(word).upper())
    for i in missed_letters:
        if i in word:
            missed_letters.remove(i)
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

if __name__ == "__main__":
    print(stats(list("ABCDEFGHIJKT"), "Tanzen"))
