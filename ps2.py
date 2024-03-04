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
    total = int(0)
    length = int(len(secret_word))
    # letters_guessed = secret_word
    print(secret_word)
    for letter in letters_guessed:
        if letter in secret_word:
            print(f"letter {letter} in word!")
            length -= 1
            print(length)
            if length == 0:
                return True
        else:
            print(f"letter {letter} not in word.")
            print("Add limb.")
            total += 1
            if total == length:
                return False
    return False



        
            


wordlist = load_words()
word = choose_words(wordlist)
letters_guessed = ['a','t','e','o','v']
print(is_word_guessed(word, letters_guessed))

