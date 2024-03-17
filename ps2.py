import random, string
import pprint

WORDLIST_FILENAME = "words.txt"

def load_words():
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(" ",len(wordlist), "words loaded.")
    return wordlist

def choose_words(wordlist):
     return random.choice(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    string = ""
    for letter in secret_word:
        if letter in letters_guessed:
            string += letter
        else:
            string += '_ '
    return string

def get_available_letters(letters_guessed):
    #enter a letter
    #if that letter is in alpha, take it out and return the rest of alpha
    my_string = ""
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alpha:
        if letter not in letters_guessed:
            my_string += letter
    return my_string



def hangman(word):
    length = len(word)
    guesses = 6
    warnings = 3
    print(word)
    letters_guessed = []
    while guesses > 0:
        print(f"The word contains {length} letters!")
        print(f"You have {guesses} guesses left!")
        print("Available letters: ",(get_available_letters(letters_guessed)))
        print()
        guess = (input("Guess a letter... "))
        guess = guess.lower()
        if guess in letters_guessed:
            print("Letter already guessed, try again!")
        elif len(guess) > 1:
            print("You can only guess once, try again.")
            warnings -= 1
            print(f"***{warnings} warnings left!***")
            if warnings == 0:
                guesses -= 1
                print("Lost a guess!")
                warnings = 3
                continue
        else:
            letters_guessed.append(guess)
            if not guess.isalpha():
                print("Character not in alphabet, try again!")
                warnings -= 1
                print(f"***{warnings} warnings left!***")
                if warnings == 0:
                    guesses -= 1
                    print("Lost a guess!")
                    warnings = 3
                    continue
            elif guess not in word:
                print("That letter is NOT in the word, try again!")
                guesses -= 1
            else:
                print("That letter is in the word")
                print(get_guessed_word(word, letters_guessed))
        if guesses == 0:
            print("----------")
            print("Better luck next time!")
            print(f"The word was {word}!")
        if is_word_guessed(word, letters_guessed) == False:
            continue
        else:
            print("  ** ** You guessed it!  **  **")
            print(f"Guesses left: {guesses}")
            break


wordlist = load_words()
word = choose_words(wordlist)
# word = "apple"
# letters_guessed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(is_word_guessed(word, letters_guessed))
# print(get_guessed_word(word, letters_guessed))
# print(get_available_letters(letters_guessed))
print(hangman(word))

